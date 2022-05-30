class Andrew():
    def __init__(self, be_googler=True):
        self.kakao = "Fuck"
        self.be_googler = True

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