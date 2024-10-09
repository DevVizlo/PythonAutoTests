from email.policy import default

numOne = 15
numTwo = 155
numThree = 8;
numbersList = [1, -5, 4, -21, 67]
strMonth = "April"

# ------------- Задача 1

def task_one(numberOne, numberTwo):
    if numberOne > numberTwo:
        print("Большее число является", numberOne)
    elif numberOne == numberTwo:
        print("Числа", numberOne, "и", numberTwo, "равны!")
    else:
        print("Большее число является: ", numberTwo )

task_one(numOne,numTwo)

# ------------- Задача 2
# Я думал мейби в питоне есть что то для разницы 135 или т.п., но в итоге пришлось делать обычным ифом

differenceNum = 135;
def task_two(numberOne, numberTwo):
    if (numberOne + differenceNum or numberOne - differenceNum) == numberTwo:
        print("Yes")
    else:
        print("No")

task_two(numOne,numTwo)

# ------------- Задача 3
# Ну, обычными ифами это скучно, да и никто так делать не будет. Искал что то на подобие свитча, имеют опыт на C#, но тут это больше сделано, как словарь,
# но суть та же...

def january():
    return  "Ныне на улице зима"

def february():
    return "Ныне на улице зима"

def march():
    return "Оу, да у нас тут весна!"

def april():
    return "Оу, да у нас тут весна!"

def august():
    return "А все, лето проскочило, опять в школу..."\

def november():
    return "Скоро сессия... Хочу лета..."

switch = {
    "January": january,
    "February": february,
    "March": march,
    "April": april,
    "August": august,
    "November": november
}

print (switch.get(strMonth, default)())

# ------------- Задача 4
# Тут я уже решил не мудрить и сделать просто несколько условий...

minValue = 10;
def task_four(numberOne, numberTwo, numberThree):
    if numberOne > minValue and numberTwo > minValue and numberThree > minValue:
        print("Yes")
    else:
        print("No")

task_four(numOne, numTwo, numThree)

# ------------- Задача 5
# Это было чуть интереснее делать)

def task_5(numList):
    for num in numList:
        if(num > 0):
            print(num)

task_5(numbersList)
