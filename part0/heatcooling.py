"""
Authors: Winnie Li, Ritwik Chakradhar
Creation date: 09/03/2025
Heat cooling - count heating days and cooling days
"""

def heatcooling():
    # ask user to input first temperature
    temp = float(input())
    # initiate heat and cool days counts
    heat = 0
    cool = 0
    # if temperature > -460, continue, if not return
    while temp > -460:
        # if above 80, count as cool day
        if temp > 80:
            cool+=1
        # if less then 60, count as heat day
        elif temp <60:
            heat+=1
        temp = float(input())
    print('Heating days:', heat)
    print('Cooling days:', cool)

if __name__ == "__main__":
   heatcooling()


