class Ex1():
    def __init__(self, value, value2):
        self.value = value
        self.occurrence = []
        self.add(value2)

    def add(self, value):
        self.value += value
        self.occurrence.append(value)

    def subtract(self, value):
        self.value -= value
        self.occurrence.append(value)

    def __repr__(self):
        return str(self.value) + "," + str(self.occurrence)


a = Ex1(5, 6)
a.subtract(3)
print(a)
