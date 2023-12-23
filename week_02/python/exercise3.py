def is_triangle(a,b,c):
  if (a > b + c) or (b > a + c) or (c > a + b):
    print("No")
  else:
    print("Yes")

def prompt_user_is_triangle():
  print("Enter the following values to check if they make a triangle:")
  a = int(input("Enter a: "))
  b = int(input("Enter b: "))
  c = int(input("Enter c: "))
  is_triangle(a,b,c)

prompt_user_is_triangle()