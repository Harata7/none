import os

def ClearScreen():
    os.system('cls')

while True:
    print("________________________________________")
    print("         Temperature Converter        ")
    print("________________________________________")
    print("[1] Celsius\n[2] Kelvin\n[3] Fahrenheit\n[4] Reamur")
    Input = input("Select:")


    if Input == '1':
        ClearScreen()
        InputCelsius = float(input("Temperature in celsius->"))
        Reamur = 4/5 * InputCelsius
        Fahrenheit = 9/5 * InputCelsius + 32
        Kelvin = InputCelsius + 273
        print(f"The temperature in reamur is  {Reamur} \nThe temperature in fahrenheit is {Fahrenheit} \nThe temperature in kelvin is {Kelvin}")
        input("...")
    elif Input == '2':
        ClearScreen()
        InputKelvin = float(input("Temperature in kelvin->"))
        Celsius = InputKelvin - 273
        Fahrenheit2 = 9/5 * (InputKelvin - 273) + 32
        Reamur2 = 4/5 * (InputKelvin - 273)
        print(f"The temperature in celsius is {Celsius} \nThe temperature in fahrenheit is {Fahrenheit2} \nThe temperature in reamur is {Reamur2}")
        input("...")
    elif Input == '3':
        ClearScreen()
        InputFahrenheit = float(input("The temperature in Fahrenheit->"))
        Celsius3 = 5/9 * (InputFahrenheit - 32)
        Kelvin3 = 5/9 * (InputFahrenheit - 32) + 273
        Reamur3 = 4/9 * (InputFahrenheit - 32)
        print(f"The temperature in celsius is {Celsius3} \nThe temperature in kelvin is {Kelvin3} \nThe temperature in reamur is {Reamur3}")
        input("...")
    elif Input == '4':
        ClearScreen()
        InputReamur = float(input("The temperature in reamur->"))
        Celsius4 = 5/4 * InputReamur
        Kelvin4 = 5/4 * InputReamur + 273
        Fahrenheit4 = 9/4 * InputReamur + 32
        print(f"The temperature in celsius is {Celsius4} \nThe temperature in kelvin is {Kelvin4} \nThe temperature in fahrenheit is {Fahrenheit4}")
        input("...")
    else:
        print("The option you input is not available\nPress enter...")
    







