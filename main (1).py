# 1.1 Implement a recursive function to calculate the factorial of a given number
def recur_factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * recur_factorial(n - 1)


num = int(input("Enter a number: "))
res = recur_factorial(num)
print("The factorial of {} is {}".format(num, res))
