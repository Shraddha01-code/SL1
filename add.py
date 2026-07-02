def add(a1, a2):
  return a1 + a2

def multiply(a1,a2):
  return a1 * a2

a,b = map(int, input("Enter two numbers for addition: ").split())
print(add(a,b))
print(multiply(a, b))
