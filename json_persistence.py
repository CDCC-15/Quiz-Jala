from json import JSONEncoder


class Store:
    def __init__(self, title, answers):
        self.title = title
        self.answers = answers

    def save_data(self):
        pass


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


store = Store(4, 5)
json = MyEncoder().encode(store)

f = open("quizs.json", "w")
f.write(json)
f.close()
