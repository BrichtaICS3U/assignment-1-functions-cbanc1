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

def selection(count):
    try:
        counter = count
        print("#-----------------Select One---------------------#")
        print("[1]Celcius to Fahrenheit  [2]Fahrenheit to Celcius")
        tempSelect = int(input(">>> "))
        print("")
    except:
        print("Nice try, please enter a number!")
        print("")
        tempSelect = 0
    
    while (counter < 1):
        try:
            if (tempSelect < 1) or (tempSelect > 2):
                print("#-----------------Select-------------------------#")
                print("That is not a selection, input either a 1 or a 2")
                print("[1]Celcius to Fahrenheit  [2]Fahrenheit to Celcius")
                tempSelect = int(input(">>> "))
                print("")
            else:
                return tempSelect
        except:
            print("Nice try, please enter a number!")
            print("")

counter = selection(0)
counter2 = 0
counter3 = 0
tempSelect = counter

while (counter >= 1):
    if tempSelect == 1:
        while (counter3 < 1):
            try:
                temperature = float(input("Enter your Degrees in Celcius: "))
                counter3 = 1
            except:
                print("Nice try, please enter a number!")
                print("")
        if temperature < (-273.15):
            print("That isn't possible, the lowest degree possible is -273.15")
            print("")
            counter3 = 0
        else:
            tempF = CtoF(temperature)
            print(temperature, "in Fahrenheit is:", round(tempF, 2))
            print("Would You Like To Continue?  [1]Yes  [2]No")
            cont = int(input(">>> "))
            while (counter2 < 1):
                if (cont < 1) or (cont > 2):
                    print("")
                    print("You can't choose that number, please select 1 or 2")
                    print("Would You Like To Continue?  [1]Yes  [2]No")
                    cont = int(input(">>> "))
                else:
                    counter2 = 3
            if cont == 1:
                print("")
                counter = selection(0)
                tempSelect = counter
                cont = 0
            else:
                print("Ok, Goodbye!")
                break
    else:
        counter3 = 0
        while (counter3 < 1):
            try:
                temperature = float(input("Enter your Degrees in Fahrenheit: "))
                counter3 = 1
            except:
                print("Nice try, please enter a number!")
                print("")
        if temperature < (-459.67):
            print("That isn't possible, the lowest degree possible is -459.67")
            print("")
            counter3 = 0
        else:
            tempC = FtoC(temperature)
            print(temperature, "in Celcius is:", round(tempC, 2))
            print("Would You Like To Continue?  [1]Yes  [2]No")
            cont = int(input(">>> "))
            while (counter2 < 1):
                if (cont < 1) or (cont > 2):
                    print("")
                    print("You can't choose that number, please select 1 or 2")
                    print("Would You Like To Continue?  [1]Yes  [2]No")
                    cont = int(input(">>> "))
                else:
                    counter2 = 3
            if cont == 1:
                print("")
                counter = selection(0)
                tempSelect = counter
                cont = 0
            else:
                print("Ok, Goodbye!")
                break
