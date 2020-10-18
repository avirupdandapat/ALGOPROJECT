def __init__(self):
    self.container = list()
    self.mins = list()


# @param x, an integer
def push(self, x):
    self.container.append(x)
    if not self.mins or self.mins[-1] >= x:
        self.mins.append(x)


# @return nothing
def pop(self):
    if self.container:
        x = self.container.pop()
        if self.mins and self.mins[-1] == x:
            self.mins.pop()


# @return an integer
def top(self):
    if self.container:
        return self.container[-1]
    else:
        return -1


# @return an integer
def getMin(self):
    if self.container and self.mins:
        return self.mins[-1]
    else:
        return -1