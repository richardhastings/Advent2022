import requests
import subprocess


def clip(data):
    data = str(data)
    subprocess.run("pbcopy", text=True, input=data)


def get_input(day, year="2022"):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {
        "session": ""
    }
    return requests.get(url, cookies=cookies).text
