from random import randint
N = 100
C = 20
with open("data.txt", "w") as f:
    f.write(str(C) + "\n")
    f.write(str(N) + "\n")
    for i in range(100):
        f.write(f"{randint(0, 100)} {randint(0, 100)}\n")