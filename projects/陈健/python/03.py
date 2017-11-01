#输出前n位斐波那契数列

x = int(input("请输入一个数："))

def Fibonacci(n):
    if (n == 0 or n == 1) :
        return 1
    else :
        return Fibonacci(n-1)+Fibonacci(n-2)

for i in range(0,x) :
    print(Fibonacci(i))
