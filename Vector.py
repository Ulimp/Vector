class vector():
    def __init__(self, x = [0]):
        self.x = x
 
    def __add__(self, b):
        c = vector(list(self.x))
        for i in range(0,len(c.x)):
            c.x[i] = c.x[i] + b.x[i]
        return c
 
    def __sub__(self, b):
        c = vector(list(self.x))
        for i in range(0,len(c.x)):
            c.x[i] = c.x[i] - b.x[i]
        return c
 
    def mult(self, b):
        c = 0
        for i in range(0,len(self.x)):
            c += self.x[i] * b.x[i]
        return c
 
 
t1 = [int(i) for i in input().split()]
a = vector(t1)
t2 = [int(i) for i in input().split()]
b = vector(t2)
print((a+b).x)
print((a-b).x)
print(a.mult(b))
      

