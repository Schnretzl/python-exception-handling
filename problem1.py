# 1. Exceptional Weather Forecast

# Task 1: Start
# Task 2: Temperature Conversion
# Task 3: User Experience
# Task 4: Finally
def convert_temperature():
    try:
        temperature = float(input("Enter temperature in Fahrenheit: "))
    except ValueError:
        print("Invalid entry.  Input must be a number.")
    except Exception as e:
        print(f"An error occurred: {e}.")
    else:
        celsius = (temperature - 32) * 5.0 / 9.0
        print(f"Temperature in celsius: {celsius:.2f}°C")
    finally:
        print("Thank you for using the temperature converter.")
    #end try
#end function

#================================================================

convert_temperature()