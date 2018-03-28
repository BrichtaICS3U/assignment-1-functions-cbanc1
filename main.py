# Assignment 1
# ICS3U
# <Cade Bancroft>
# March 28, 2018

def CtoF(temperatureC):
    F = ((1.8) * temperatureC) + 32
    return F

def FtoC(temperatureF):
    C = (0.55556) * (temperatureF - 32)
    return C


print("#-----------------Select One---------------------#")
print("[1]Celcius to Fahrenheit  [2]Fahrenheit to Celcius")
tempSelect = int(input(">>> "))
counter = int(0)
counter2 = int(0)

while (counter < 1):
    if (tempSelect < 1) or (tempSelect > 2):
        print("That is not a selection, input either a 1 or a 2")
        print("")
        print("")
        print("#-----------------Select One---------------------#")
        print("[1]Celcius to Fahrenheit  [2]Fahrenheit to Celcius")
        tempSelect = int(input(">>> "))
    else:
        counter = 2

while (counter == 2):
    if tempSelect == 1:
        temperature = float(input("Enter your Degrees in Celcius: "))
        if temperature < (-273.15):
            print("That isn't possible, the lowest degree possible is 273.15")
        else:
            tempF = CtoF(temperature)
            print(temperature, "in Fahrenheit is:", tempF)
            print("Would You Like To Continue?  [1]Yes  [2]No")
            cont = int(input(">>> "))
            while (counter2 < 1):
                if (cont < 1) or (cont > 2):
                    print("You can't choose that number, please select 1 or 2")
                else:
                    counter2 = 2
            if cont == 1:
                counter = 0 ####THIS IS WHERE I LEFT OFF QUESTION 5
    else:
        temperature = float(input("Enter your Degrees in Fahrenheit: "))
        if temperature < (-459.67):
            print("That isn't possible, the lowest degree possible is 459.67")
        else:
            tempC = FtoC(temperature)
            print(temperature, "in Celcius is:", tempC)
            print("Would You Like To Continue?  [1]Yes  [2]No")
            cont = int(input(">>> "))
