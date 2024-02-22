#!/usr/bin/python3
"""
A script to get tasks from all employees
and exports the data to JSON files.
"""
import json
import requests


def get_todo_for_all_users():
    """
    A method to get tasks from all employees
    """
    # user id range for look up.
    user_ids = range(1, 11)
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    fileName = 'todo_all_employees.json'
    all = []

    for user_id in user_ids:
        r = requests.get(url.format(user_id))
        if r.status_code == 200:
            user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                .format(user_id))
            if user.status_code == 200:
                user_data = user.json()
                tasks = []
                for task in r.json():
                    task_info = {
                        "username": user_data['username'],
                        "task": task['title'],
                        "completed": task['completed']
                    }
                    tasks.append(task_info)
                json_data = {str(user_id): tasks}
                all.append(json_data)
            else:
                print("Error: Failed to retrieve user data for user ID:",
                      user_id)
        else:
            print("Error: Failed to retrieve TODO list for user ID:", user_id)
    with open(fileName, mode='w') as file:
        json.dump(all, file)


if __name__ == '__main__':
    get_todo_for_all_users()
