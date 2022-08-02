#WIP
"""
Author: alxwen711 (Alex Wen)

Basic stack class template



"""





class stack:
    def __init__(self):
        self.s = list()

    def push(self,x) -> None:
        self.s.append(x)

    def top(self):
        return self.s[-1]

    def pop(self):
        x = self.s.pop(-1)
        return x



if __name__ == "__main__":
    x = stack()
    x.push(1)
    x.push(2)
    x.push(3)
    print(x.pop())
