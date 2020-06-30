# A simple python function made by Thegr8kabeer to convert °F to °C
# Easy to understand syntax for the person who knows the basics Python
# Feel free to edit my code and do some experiments!!!
# Don't forget to follow me on instagram at https://instagram.com/thegr8kabeer/

def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 3)

#converting boiling point of input
user_input = int(input())
temp = fahrenheit_to_celsius(user_input)
print(temp, "°C")
