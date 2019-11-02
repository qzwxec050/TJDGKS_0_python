class Stack(list):

    push = list.append

    def is_empty(self):
        if not self:
            return True
        else:
            return False

    def peek(self):
        return self[-1]

if __name__== "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    while s:
        data = s.pop()
        print(data, end=' ')