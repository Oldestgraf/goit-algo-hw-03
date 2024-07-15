import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)
        t.right(120)
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)

def koch_snowflake(t, length, levels):
    for i in range(3):
        koch_curve(t, length, levels[i])
        t.right(120)

def main():
    # Отримуємо рівні рекурсії для кожної сторони від користувача
    levels = []
    for i in range(3):
        level = int(input(f"Введіть рівень рекурсії для сторони {i + 1}: "))
        levels.append(level)

    # Налаштування вікна turtle
    window = turtle.Screen()
    window.bgcolor("white")

    # Налаштування turtle
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання

    # Малюємо сніжинку Коха
    length = 200.0  # Довжина сторони сніжинки
    t.penup()
    t.goto(-length/2, length/3)
    t.pendown()
    koch_snowflake(t, length, levels)

    t.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()
