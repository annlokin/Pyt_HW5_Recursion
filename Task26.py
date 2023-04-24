# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

n = int(input("Введите число "))
pow = int(input("Введите степень "))
def pow_number (n,pow):
  if (pow == 0):
   return 1
  return (n * pow_number (n, pow - 1))

print(pow_number(n,pow))
