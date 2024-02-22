#!/usr/bin/python3
"""
A script that, using this REST API, for a given
employee ID, returns information about his/her
TODO list progress.
"""
import csv
import requests
import sys


def get_todo(id=None):
    """
    A method to get an eployee's todo list.
    """
    if (id is not None):
        r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(id))
        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(id))
        done = []
        all = []
        if (r.status_code == 200):
            user = user.json()
            for val in r.json():
                val['userName'] = user['name']
                all.append(val)
            csv_file = '{}.csv'.format(user['id'])
            fieldnames = ['userId', 'userName', 'completed', 'title']
            with open(csv_file, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames,
                                        quoting=csv.QUOTE_ALL)
                for row in all:
                    filtered_row = {key: value for key, value
                                    in row.items() if key in fieldnames}
                    writer.writerow(filtered_row)


if __name__ == '__main__':
    if (len(sys.argv) >= 2):
        id = sys.argv[1]
        get_todo(id)
