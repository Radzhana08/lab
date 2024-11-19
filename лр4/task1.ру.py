# TODO решите задачу
import json


def task() -> float:
    Score = []
    Weight = []
    with open('input.json', "r") as file:
        k = file.read()
    data = json.loads(k)
    for i in data:
        Score.append(i["score"])
        Weight.append(i["weight"])
    sum = 0
    for i in range (0, len(Score)):
        sum = sum + Score[i]*Weight[i]
    return round(sum,3)
print(task())

