def add(a1, a2):
  return a1 + a2

def multiply(a1,a2):
  return a1 * a2

a,b = map(int, input("Enter two numbers: ").split())
print("Addition is ",add(a,b))
print("Multiplication is ",multiply(a, b))
