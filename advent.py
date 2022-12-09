import requests
import subprocess
import re


def clip(data):
    data = str(data)
    subprocess.run("pbcopy", text=True, input=data)


def get_input(day, year="2022"):
    if day == 0:
        with open("sample.txt", "r") as f:
            ret = f.read()
        return ret
    else:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        cookies = {
            "session": ""
        }
        return requests.get(url, cookies=cookies).text


def re_input(regex, day, year='2022'):
    inputs = get_input(day, year).splitlines()
    return [re.match(regex, i).groups() for i in inputs]

