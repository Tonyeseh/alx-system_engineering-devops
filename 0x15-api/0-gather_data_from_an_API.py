#!/usr/bin/python3
"""
returns information for a given employee ID about his/her TODO list progress
"""
import json
import requests
from sys import argv


def get_completed_tasks(todos):
    """ gets the number of completed todo of a user"""
    completed = 0
    for todo in todos:
        if todo.get("completed"):
            completed += 1

    return completed


def print_tasks(todos):
    """ prints the each tasks and appends a tab before it """
    for todo in todos:
        if todo.get("completed"):
            print("\t {}".format(todo.get("title")))


if __name__ == "__main__":
    user_data = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    user_data = json.loads(user_data.text)
    user_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId={}"
        .format(user_data.get("id")))
    user_todos = json.loads(user_todos.text)
    print(
        "Employee {} is done with tasks({}/{}):"
        .format(user_data.get("name"),
                get_completed_tasks(user_todos),
                len(user_todos)))
    print_tasks(user_todos)
