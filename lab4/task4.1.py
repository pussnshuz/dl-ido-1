import json
filename = 'input.json'

def task() -> float:
    with open(filename, 'r') as file:
        data = json.load(file)
        sum_item = 0
        for item in data:
            score = item.get('score')
            weight = item.get('weight')
            sum_item += score*weight
    return round(sum_item, 3)

print(task())
