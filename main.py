def fact_recc(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_recc(n - 1)
    number = int(input('enter a value:'))
    res = fact_rec(number)
  print("the factorial of{} is{}".format(number, res))
