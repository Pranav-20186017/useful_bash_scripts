def getNthFib(n):
  if n == 1:
    return 0
  if n == 2:
    return 1
  elif n > 2:
    return fib(n -2) + fib(n - 1)


def main():
    n = 40
    print(fib(n))
if __name__ == "__main__":
    main()
