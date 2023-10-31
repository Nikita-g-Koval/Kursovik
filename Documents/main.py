import numpy as np
# Задаем функцию
def f(x1, x2):
    return np.exp(x1**2 - x2) + np.exp(x2)
# Задаем градиент функции
def gradient_f(x1, x2):
    df_dx1 = 2 * x1 * np.exp(x1**2 - x2)
    df_dx2 = -np.exp(x1**2 - x2) + np.exp(x2)
    return np.array([df_dx1, df_dx2])
# Параметры метода
epsilon1 = 1e-6  # Критерий окончания 1
epsilon2 = 1e-6  # Критерий окончания 2
M = 1000  # Максимальное число итераций
alpha = 0.1  # Величина шага
# Инициализация начальной точки
X0 = np.array([-1.0, -1.0])

# Шаг 2. Начальная итерация
k = 0

while True:
    # Шаг 3. Вычисляем градиент функции в текущей точке
    gradient = gradient_f(X0[0], X0[1])

    # Шаг 4. Проверка критерия окончания 1
    if np.linalg.norm(gradient) < epsilon1:
        X_star = X0
        break

    # Шаг 5. Проверка критерия окончания 2
    if k >= M:
        X_star = X0
        break

    # Шаг 6. Задаем величину шага
    alpha_k = alpha

    # Шаг 7. Обновление точки
    X1 = X0 - alpha_k * gradient

    # Шаг 8. Проверка условия убывания функции
    if f(X1[0], X1[1]) - f(X0[0], X0[1]) < -epsilon2 * np.dot(gradient, gradient):
        X0 = X1
    else:
        alpha_k = 0.5 * alpha_k  # Уменьшаем шаг

    # Шаг 9. Проверка условий окончания
    if np.linalg.norm(X1 - X0) < epsilon1 and abs(f(X1[0], X1[1]) - f(X0[0], X0[1])) < epsilon2:
        X_star = X1
        break
    X0 = X1
    k += 1
print("Минимум функции найден в точке:", X_star)
print("Значение минимума функции:", f(X_star[0], X_star[1]))