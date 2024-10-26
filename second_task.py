import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)

def snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    # Запит рівня рекурсії у користувача
    order = int(input("Введіть рівень рекурсії (0-5): "))
    
    # Налаштування вікна
    window = turtle.Screen()
    window.bgcolor("white")

    # Налаштування
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість
    t.color("green")

    # Розташування
    t.penup()
    t.goto(-150, 90)  # Центруємо сніжинку
    t.pendown()

    # Малюємо сніжинку Коха
    snowflake(t, order, 300)

    # Завершення малювання
    t.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()