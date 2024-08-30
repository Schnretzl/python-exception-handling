# 1. Exceptional Weather Forecast

# Task 1: Start
# Task 2: Temperature Conversion
# Task 3: User Experience
# Task 4: Finally
def convert_temperature():
    while True:
        try:
            temperature = float(input("Enter temperature in Fahrenheit: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        else:
            celsius = (temperature - 32) * 5.0 / 9.0
            print(f"Temperature in celsius: {celsius:.2f}°C")
            break
        #end try
    #end while
#end function








#================================================================

convert_temperature()