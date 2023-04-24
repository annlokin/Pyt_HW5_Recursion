num_a = int(input("Введите число a "))
num_b = int(input("Введите число b "))
def sum_num(a, b):
    if b == 0:
        return a
    return sum_num(a+1,b-1)
print (sum_num(num_a,num_b))