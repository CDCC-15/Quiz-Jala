from json import JSONEncoder


<<<<<<< HEAD
class Store:
    def __init__(self, title, answers):
        self.title = title
        self.answers = answers

    def save_data(self):
        data = {}
=======
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
>>>>>>> 90b8ccff3ce47341b3d767a3529804b87111e4d1


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


<<<<<<< HEAD
store = Store(4, 5)
json = MyEncoder().encode(store)
=======
myclass = MyClass(4, 5)
json = MyEncoder().encode(myclass)
>>>>>>> 90b8ccff3ce47341b3d767a3529804b87111e4d1
f = open("myform.json", "w")
f.write(json)
f.close()
