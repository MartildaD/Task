celsius_input = float(input("Enter a temperature in celsius: "))
for temperature  in range(5):
    celsius = celsius_input + temperature

    if celsius < -273:
        print(f"{celsius}C is impossible! NOthing can be colder than _273C.")
    else:
        farenheit = (celsius * 9/5) + 32
        print(f"{celsius}C = {farenheit}F")
