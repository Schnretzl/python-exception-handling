# 1. Exceptional Weather Forecast

# Task 1: Start
def get_temperature():
    while True:
        try:
            temperature = float(input("Enter temperature in Fahrenheit: "))
            return temperature
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
#end function


# Task 2: Temperature Conversion
def convert_temperature(temperature):
    celsius = (temperature - 32) * 5.0 / 9.0
    return celsius
#end function


# Task 3: User Experience


# Task 4: Finally

#================================================================

temp = get_temperature()
celsius = convert_temperature(temp)
print(f"Celsius: {celsius:.1f}")