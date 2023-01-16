#!/usr/bin/python3
"""
returns information for a given employee ID about his/her
TODO list progress in json
"""
import json
from sys import argv
import requests


if __name__ == "__main__":
    all_dict = {}
    for user_id in range(1, 11):
        user_data = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(user_id))
        user_data = json.loads(user_data.text)
        user_todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos/?userId={}"
            .format(user_data.get("id")))
        user_todos = json.loads(user_todos.text)

        user_list = []
        for todo in user_todos:
            dic = {}
            dic["task"] = todo["title"]
            dic["completed"] = todo["completed"]
            dic["username"] = user_data["username"]
            user_list.append(dic)

        all_dict["{}".format(user_id)] = user_list
#        user_data = requests.get(
#            "https://jsonplaceholder.typicode.com/users/{}".format(user_id))

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        if all_dict is None or all_dict == []:
            f.write("[]")
        else:
            f.write(json.dumps(all_dict))
