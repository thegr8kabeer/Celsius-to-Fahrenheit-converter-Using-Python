# A simple python function made by Thegr8kabeer to convert °C to °F
# Easy to understand syntax for the person who knows the basics Python
# Feel free to edit my code and do some experiments!!!
# Don't forget to follow me on instagram at https://instagram.com/thegr8kabeer/


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)

user_input = int(input())
temp = celsius_to_fahrenheit(user_input)
print(temp, "°F")
