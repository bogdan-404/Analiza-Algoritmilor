import decimal
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable


# recursive algorithm
def fibonacci_recursive(num):
    if num <= 1:
        return num
    else:
        return(fibonacci_recursive(num-1) + fibonacci_recursive(num-2))


# iterative algorithm
def fibonacci_iterative(num):
    if num <= 1:
        return num
    else:
        a = 0
        b = 1
        for i in range(2, num+1):
            c = a + b
            a = b
            b = c
        return b


# dynamic algorithm
def fibonacci_dynamic(num):
    fibonacci = [0, 1]
    for i in range(2, num+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci[num]


# binets formula algorithm
def fibonacci_binets(num):
    decimal.getcontext().prec = 100
    phi = (decimal.Decimal(1) + decimal.Decimal(5).sqrt()) / decimal.Decimal(2)
    psi = (decimal.Decimal(1) - decimal.Decimal(5).sqrt()) / decimal.Decimal(2)
    return int((phi**num - psi**num) / decimal.Decimal(5).sqrt())


# matrix multiplication algorithm
def fibonacci_matrix(num):
    matrix = [[1, 1], [1, 0]]
    if num == 0:
        return 0
    power(matrix, num-1)
    return matrix[0][0]


def power(matrix, num):
    if num == 0 or num == 1:
        return
    power(matrix, num//2)
    multiply(matrix, matrix)
    if num % 2 != 0:
        multiply(matrix, [[1, 1], [1, 0]])


def multiply(matrix, matrix2):
    x = matrix[0][0] * matrix2[0][0] + matrix[0][1] * matrix2[1][0]
    y = matrix[0][0] * matrix2[0][1] + matrix[0][1] * matrix2[1][1]
    z = matrix[1][0] * matrix2[0][0] + matrix[1][1] * matrix2[1][0]
    w = matrix[1][0] * matrix2[0][1] + matrix[1][1] * matrix2[1][1]
    matrix[0][0] = x
    matrix[0][1] = y
    matrix[1][0] = z
    matrix[1][1] = w


values = [5, 7, 10, 15, 20, 25, 30, 35, 40]
values2 = [20000, 30000, 40000, 60000, 100000, 125000, 150000, 200000]

recursive = []
iterative = []
dynamic = []
binets = []
matrix = []


start = time.time()
for i in values:
    fibonacci_recursive(i)
    end = time.time()
    recursive.append(round(end-start, 8))

start = time.time()
for i in values2:
    fibonacci_iterative(i)
    end = time.time()
    iterative.append(round(end-start, 8))

start = time.time()
for i in values2:
    fibonacci_dynamic(i)
    end = time.time()
    dynamic.append(round(end-start, 8))

start = time.time()
for i in values2:
    fibonacci_binets(i)
    end = time.time()
    binets.append(round(end-start, 8))

start = time.time()
for i in values2:
    fibonacci_matrix(i)
    end = time.time()
    matrix.append(round(end-start, 8))

table_recursive = PrettyTable(values)
table_recursive.add_row(recursive)
print(table_recursive)

headers = values2
table_all = PrettyTable(headers)
table_all.add_row(iterative)
table_all.add_row(dynamic)
table_all.add_row(binets)
table_all.add_row(matrix)
print(table_all)


plt.figure(1)
plt.plot(values, recursive, label='Recursive algorithm', color='red')
plt.scatter(values, recursive, color='red')
plt.title('Recursive algorithm')
plt.xlabel('n-th fibonacci number')
plt.ylabel('time in seconds')

plt.figure(2)
plt.plot(values2, iterative, label='Iterative algorithm', color='blue')
plt.scatter(values2, iterative, color='blue')
plt.title('Iterative algorithm')
plt.xlabel('n-th fibonacci number')
plt.ylabel('time in seconds')


plt.figure(3)
plt.plot(values2, dynamic, label='Dynamic algorithm', color='green')
plt.scatter(values2, dynamic, color='green')
plt.title('Dynamic algorithm')
plt.xlabel('n-th fibonacci number')
plt.ylabel('time in seconds')


plt.figure(4)
plt.plot(values2, binets, label='Binets formula algorithm', color='yellow')
plt.scatter(values2, binets, color='yellow')
plt.title('Binets formula algorithm')
plt.xlabel('n-th fibonacci number')
plt.ylabel('time in seconds')

plt.figure(5)
plt.plot(values2, matrix, label='Matrix multiplication algorithm', color='orange')
plt.scatter(values2, matrix, color='orange')
plt.title('Matrix multiplication algorithm')
plt.xlabel('n-th fibonacci number')
plt.ylabel('time in seconds')

plt.figure(6)
plt.plot(values2, iterative, label='Iterative algorithm', color='blue')
plt.plot(values2, dynamic, label='Dynamic algorithm', color='green')
plt.plot(values2, binets, label='Binets formula algorithm', color='yellow')
plt.plot(values2, matrix, label='Matrix multiplication algorithm', color='orange')
plt.legend()
plt.xlabel('n-th fibonacci number')
plt.ylabel('time in seconds')
plt.show()
