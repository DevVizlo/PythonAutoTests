# -------------- Задача 1

namePlayer: str = "Nikolai"
oldPlayer: int = 22;
heightPlayer: float = 184.05
familyPlayer: list = ["Dima", "Oksana", "Anton"]
isManPlayer: bool = True

def task_1(name, old, height, family, isMan):
    return  name, old, height, family, isMan

print(task_1(namePlayer, oldPlayer, heightPlayer, familyPlayer, isManPlayer))

# ------------------ Задача 2
a: list = [1, 2, 3, 5, 8, 13, 21]

def task_2(listA):
  return listA;

print(task_2(a[0:3]), type(a))

# ------------- Задача 3
inputNumber = 6

def task_3(number) -> int:
    return number ** 2;

print(task_3(inputNumber))
