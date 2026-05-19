# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !



from datetime import date

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def draw_cake(candles):
    candle_row = " " * 4 + "_" * (candles // 2) + "i" * candles + "_" * (candles // 2)
    print(candle_row)
    print("    |:H:a:p:p:y:|")
    print("  __|___________|__")
    print(" |^^^^^^^^^^^^^^^|")
    print(" |:B:i:r:t:h:d:a:y:|")
    print(" |               |")
    print("  ~~~~~~~~~~~~~~~")

birthdate = input("Enter your birthdate (DD/MM/YYYY): ")

day, month, year = map(int, birthdate.split("/"))

today = date.today()
age = today.year - year - ((today.month, today.day) < (month, day))

candles = age % 10

print(f"\nYou are {age} years old, so your cake has {candles} candle(s)!\n")

draw_cake(candles)

if is_leap_year(year):
    print("\nYou were born on a leap year! Here's a second cake!\n")
    draw_cake(candles)