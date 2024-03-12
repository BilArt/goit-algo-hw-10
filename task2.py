import numpy as np

# Визначення функції
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Генерація точок
n = 10000
x_rand = np.random.uniform(a, b, n)
y_rand = np.random.uniform(0, f(b), n)

# Обчислення кількості точок, які попали під криву
count = sum(1 for i in range(n) if y_rand[i] <= f(x_rand[i]))

# Обчислення площі під кривою
area = (count / n) * (b - a) * f(b)

print("Площа під кривою (за допомогою методу Монте-Карло):", area)

# Перевірка за допомогою функції quad з SciPy
import scipy.integrate as spi

result, _ = spi.quad(f, a, b)
print("Точне значення інтеграла:", result)
