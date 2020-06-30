# A simple python function made by Thegr8kabeer to convert °C to °F
# Easy to understand syntax for the person who knows the basics of Python
# Feel free to edit my code and do some experiments!!!
# Don't forget to follow me on instagram at https://instagram.com/thegr8kabeer/

# making a function to convert
def celsius_to_fahrenheit(temps_c):
    # Telling the program the real anatomy behind the conversion that is the formula
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)

# Taking the input from the user
user_input = int(input())
temp = celsius_to_fahrenheit(user_input)
# printing the input
print(temp, "°F")
