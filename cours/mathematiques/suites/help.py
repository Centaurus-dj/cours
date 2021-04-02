def myFunction(n: int) -> int:
  u = 50
  for i in range(0, n):
    u = (-0.5*u)+5
  print("u:", u)
  return u

if __name__ == "__main__":
  myFunction(int(input("Donnez n: ")))
