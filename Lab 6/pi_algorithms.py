from decimal import Decimal, getcontext
import time
import matplotlib.pyplot as plt


def chudnovsky(precision):
    getcontext().prec = precision + 2
    C = 426880 * Decimal(10005).sqrt()
    factorial_memo = [1]
    power_memo = [1]
    for i in range(1, 6*precision+1):
        factorial_memo.append(factorial_memo[-1] * i)
    for i in range(1, precision+1):
        power_memo.append(power_memo[-1] * -262537412640768000)
    sum = Decimal(0)
    for k in range(precision):
        M = factorial_memo[6*k] * ((545140134*k) + 13591409)
        X = factorial_memo[3*k] * (factorial_memo[k]**3) * power_memo[k]
        sum += Decimal(M) / X
    pi = C / sum
    return pi


def gauss_legendre(precision):
    getcontext().prec = precision + 2
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(0.25)
    p = Decimal(1)
    for i in range(precision):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) * (a - a_next)
        a = a_next
        p *= 2
    return (a + b) * (a + b) / (4 * t)


def arctan_power_series(x, precision):
    getcontext().prec = precision + 2
    x = Decimal(x)
    x_squared = x * x
    term = x
    arctan = term
    n = 3
    while term > 10 ** (-precision - 1):
        term *= x_squared
        arctan -= term / n
        n += 2
        term *= x_squared
        arctan += term / n
        n += 2
    return arctan


def machin(precision):
    getcontext().prec = precision + 2
    arctan_1_5 = arctan_power_series(1/5, precision)
    arctan_1_239 = arctan_power_series(1/239, precision)
    pi = 16 * arctan_1_5 - 4 * arctan_1_239
    return pi


def get_nth_digit_machin(n):
    pi = machin(n+1)
    str_pi = str(pi)
    return str_pi[n+1]


def get_nth_digit_chudnovsky(n):
    pi = chudnovsky(n+1)
    str_pi = str(pi)
    return str_pi[n+1]


def get_nth_digit_gauss_lagendre(n):
    pi = gauss_legendre(n+1)
    str_pi = str(pi)
    return str_pi[n+1]


nums = [50, 100, 500, 1000]
chudnovsky_time = []
gauss_legendre_time = []
machin_time = []


for i in nums:
    start = time.time()
    temp = get_nth_digit_chudnovsky(i)
    end = time.time()
    chudnovsky_time.append(end - start)

    start = time.time()
    temp = get_nth_digit_gauss_lagendre(i)
    end = time.time()
    gauss_legendre_time.append(end - start)

    start = time.time()
    temp = get_nth_digit_machin(i)
    end = time.time()
    machin_time.append(end - start)

plt.figure(1)
plt.plot(nums, chudnovsky_time, linewidth=2.0, color='green')
plt.title('Chudnovsky Algorithm Runtime')
plt.ylabel('Time in seconds')
plt.xlabel('N-th digit')

plt.figure(2)
plt.plot(nums, gauss_legendre_time, linewidth=2.0, color='red')
plt.title('Gauss-Legendre Algorithm Runtime')
plt.ylabel('Time in seconds')
plt.xlabel('N-th digit')

plt.figure(3)
plt.plot(nums, machin_time, linewidth=2.0, color='blue')
plt.title('Machin Algorithm Runtime')
plt.ylabel('Time in seconds')
plt.xlabel('N-th digit')

plt.figure(4)
plt.plot(nums, chudnovsky_time, linewidth=2.0,
         color='green', label='Chudnovsky')
plt.plot(nums, gauss_legendre_time, linewidth=2.0,
         color='red', label='Gauss-Legendre')
plt.plot(nums, machin_time, linewidth=2.0, color='blue', label='Machin')

plt.title('Comparison of Algorithm Runtimes')
plt.ylabel('Time in seconds')
plt.xlabel('N-th digit')
plt.legend(loc='upper left')
plt.show()

plt.show()
