#!/usr/bin/python3
"""Script that uses a REST API to conform a JSON
"""
import json
import requests


def get_dump():
    """GET user todos at given id"""
    url = "https://jsonplaceholder.typicode.com/"
    a = requests.get(url + "users/").json()
    b = requests.get(url + "todos/").json()
    tmp_dict = {}

    for users in a:
        the_users = []
        for tasks in b:
            if users.get("id") == tasks.get("userId"):
                o = {}
                o["task"] = tasks.get("title")
                o["completed"] = tasks.get("completed")
                o["username"] = users.get("username")
                the_users.append(o)
        tmp_dict[users.get("id")] = the_users
    """Dump!"""
    with open('todo_all_employees.json', 'w') as file:
        json.dump(tmp_dict, file)


if __name__ == '__main__':
    """Excecute it"""
    get_dump()
