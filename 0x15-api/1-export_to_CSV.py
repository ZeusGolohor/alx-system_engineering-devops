#!/usr/bin/python3
"""
A script that, using this REST API, for a given
employee ID, returns information about his/her
TODO list progress.
"""
import requests
import sys


def get_todo(id=None):
    """
    A method to get an eployee's todo list.
    """
    if (id is not None):
        res = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(id))
        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(id))
        done = []
        all = []
        if (res.status_code == 200):
            user = user.json()
            print(res.json())


if __name__ == '__main__':
    if (len(sys.argv) >= 1):
        id = sys.argv[1]
        get_todo(id)
