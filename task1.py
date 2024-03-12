from pulp import *

x1 = LpVariable("Lemonade_units", lowBound=0, cat='Integer')  # кількість одиниць Лимонаду
x2 = LpVariable("Juice_units", lowBound=0, cat='Integer')  # кількість одиниць Фруктового соку

# Створення моделі
model = LpProblem("Production_Optimization", LpMaximize)

# Додавання функції максимізації (кількість продуктів)
model += x1 + x2, "Total_Products"

# Додавання обмежень
model += 2*x1 + x2 <= 100  # Вода
model += x1 + x2 <= 50      # Цукор
model += x1 <= 30           # Лимонний сік
model += 2*x2 + x1 <= 40   # Фруктове пюре

# Розв'язання задачі
model.solve()

print("Optimal Production:")
for var in model.variables():
    print(f"{var.name} = {var.varValue}")

print("Total Products =", value(model.objective))
