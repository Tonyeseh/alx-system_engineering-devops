#!/usr/bin/python3
"""
returns information for a given employee ID about his/her TODO list progress
"""
import csv
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

    user_dict = []
    for todo in user_todos:
        dic = {}
        dic["id"] = todo["userId"]
        dic["name"] = user_data["username"]
        dic["status"] = todo["completed"]
        dic["title"] = todo["title"]
        user_dict.append(dic)

    with open(f"{argv[1]}.csv", "w", newline="") as f:
        if user_dict is None or user_dict == []:
            f.write("[]")
        else:
            fieldname = ["id", "name", "status", "title"]
            writer = csv.DictWriter(f, fieldnames=fieldname)
            for todo in user_dict:
                writer.writerow(todo)