def towers(n, source, auxiliary, target):
    if n == 1:
        print(f"Перемістити диск 1 зі стрижня {source} на стрижень {target}")
        return
    towers(n-1, source, target, auxiliary)
    print(f"Перемістити диск {n} зі стрижня {source} на стрижень {target}")
    towers(n-1, auxiliary, source, target)

def main():
    n = int(input("Введіть кількість дисків: "))
    towers(n, 'A', 'B', 'C')

if __name__ == "__main__":
    main()
