#!/usr/bin/python3
"""
returns information for a given employee ID about his/her
TODO list progress in json
"""
import json
from sys import argv
import requests


if __name__ == "__main__":
    user_data = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
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

    user_dict = {"{}".format(argv[1]): user_list}

    with open("{}.json".format(argv[1]), "w", encoding="utf-8") as f:
        if user_dict is None or user_dict == []:
            f.write("[]")
        else:
            f.write(json.dumps(user_dict))
