import matplotlib.pyplot as plt
import time
from prettytable import PrettyTable


def eratosthenes_sieve_1(n):
    c = [True for i in range(n+1)]
    c[1] = False
    i = 2
    while i <= n:
        if c[i] == True:
            j = 2 * i
            while j <= n:
                c[j] = False
                j += i
        i += 1
    primes = []
    for i in range(2, n+1):
        if c[i] == True:
            primes.append(i)

    return primes


def eratosthenes_sieve_2(n):
    c = [True for i in range(n+1)]
    c[1] = False
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1
    primes = []
    for i in range(2, n+1):
        if c[i] == True:
            primes.append(i)

    return primes


def eratosthenes_sieve_3(n):
    c = [True for i in range(n+1)]
    c[1] = False
    i = 2
    while i <= n:
        if c[i] == True:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1
    primes = []
    for i in range(2, n+1):
        if c[i] == True:
            primes.append(i)
    return primes


def erastosthenes_sieve_4(n):
    c = [True for i in range(n+1)]
    c[1] = False
    i = 2
    while i <= n:
        j = 2
        while j < i:
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    primes = []
    for i in range(2, n+1):
        if c[i] == True:
            primes.append(i)
    return primes


def eratosthenes_sieve_5(n):
    c = [True for i in range(n+1)]
    c[1] = False
    i = 2
    while i <= n:
        j = 2
        while j <= i**0.5:
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    primes = []
    for i in range(2, n+1):
        if c[i] == True:
            primes.append(i)
    return primes


input = [1000, 10000, 20000]

results = []
for i in input:
    start = time.time()
    eratosthenes_sieve_1(i)
    end = time.time()
    results.append(end - start)
    start = time.time()
    eratosthenes_sieve_2(i)
    end = time.time()
    results.append(end - start)
    start = time.time()
    eratosthenes_sieve_3(i)
    end = time.time()
    results.append(end - start)
    start = time.time()
    erastosthenes_sieve_4(i)
    end = time.time()
    results.append(end - start)
    start = time.time()
    eratosthenes_sieve_5(i)
    end = time.time()
    results.append(end - start)


results_1 = results[0:5]
results_2 = results[5:10]
results_3 = results[10:15]

table = PrettyTable()
table.field_names = ["1000", "10000", "20000"]
table.add_row([results_1[0], results_2[0], results_3[0]])
print(table)

table = PrettyTable()
table.field_names = ["1000", "10000", "20000"]
table.add_row([results_1[1], results_2[1], results_3[1]])
print(table)

table = PrettyTable()
table.field_names = ["1000", "10000", "20000"]
table.add_row([results_1[2], results_2[2], results_3[2]])
print(table)

table = PrettyTable()
table.field_names = ["1000", "10000", "20000"]
table.add_row([results_1[3], results_2[3], results_3[3]])
print(table)

table = PrettyTable()
table.field_names = ["1000", "10000", "20000"]
table.add_row([results_1[4], results_2[4], results_3[4]])
print(table)


plt.figure(1)
plt.bar(['Algorithm 1', 'Algorithm 2', 'Algorithm 3',
        'Algorithm 4', 'Algorithm 5'], results_1, color='green')
plt.title('Computing prime numbers up to 1000')
plt.xlabel('Algorithms')
plt.ylabel('Time in seconds')

plt.figure(2)
plt.bar(['Algorithm 1', 'Algorithm 2', 'Algorithm 3',
        'Algorithm 4', 'Algorithm 5'], results_2, color='blue')
plt.title('Computing prime numbers up to 10000 ')
plt.xlabel('Algorithms')
plt.ylabel('Time in seconds')

plt.figure(3)
plt.bar(['Algorithm 1', 'Algorithm 2', 'Algorithm 3',
        'Algorithm 4', 'Algorithm 5'], results_3, color='red')
plt.title('Computing prime numbers up to 20000')
plt.xlabel('Algorithms')
plt.ylabel('Time in seconds')

plt.show()
