#!/usr/bin/python3
"""
A script that, using this REST API, for a given
employee ID, returns information about his/her
TODO list progress.
"""
import json
import requests
import sys


def get_todo(id=None):
    """
    A method to get an employee's todo list.
    """
    if id is not None:
        r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(id))
        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(id))
        if r.status_code == 200 and user.status_code == 200:
            user = user.json()
            tasks = []
            for val in r.json():
                task_info = {
                    "task": val['title'],
                    "completed": val['completed'],
                    "username": user['username']
                }
                tasks.append(task_info)
            json_data = {str(user['id']): tasks}
            json_file = '{}.json'.format(user['id'])
            with open(json_file, mode='w') as file:
                json.dump(json_data, file)
        else:
            print("Error: Failed to retrieve TODO list for user ID:", id)
    else:
        print("Error: No user ID provided.")


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        id = sys.argv[1]
        get_todo(id)
    else:
        print("Usage: script user_id")
