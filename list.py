class List():
    def __init__(self, data):
        self.data = data

    def append(self, value):
        self.data = self.data + [value]
        return None

    def pop(self):
        self.data = self.data[:-1]
        return None

a = [1,2,3,4]
a.pop()
a.append(6)
print(a)