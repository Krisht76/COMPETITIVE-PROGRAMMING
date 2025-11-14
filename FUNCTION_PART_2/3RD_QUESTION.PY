# 3. What is Error in this code and how can we correct this code?
#  def pythagoras(a,b):
#  return square(a) + square(b)
#  c2 = pythagoras(3,4)
#  def square(x):
#  return x * x
#  print("c2 = ", c2)
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    def square(x):
        return x * x
    def pythagoras(a, b):
        return square(a) + square(b)
    c2 = pythagoras(a, b)
    print("c2 =", c2)
    