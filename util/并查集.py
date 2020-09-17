class UnionFind:
def __init__(self):
    self.parent = list(range(26))

def find(self, index):
    if index == self.parent[index]:
        return index
    self.parent[index] = self.find(self.parent[index])
    return self.parent[index]

def union(self, index1, index2):
    self.parent[self.find(index1)] = self.find(index2)
