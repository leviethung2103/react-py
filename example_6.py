tasks = [
    {"text": "Make breakfast", "priority": 0},
    {"text": "Feed the dog", "priority": 0},
    {"text": "Do laundry", "priority": 2},
    {"text": "Go on a run", "priority": 1},
    {"text": "Clean the house", "priority": 2},
    {"text": "Go to the grocery store", "priority": 2},
    {"text": "Do some coding", "priority": 1},
    {"text": "Read a book", "priority": 1},
]

sorted_list = list(sorted(tasks, key=lambda x: x["priority"]))
print(sorted_list)