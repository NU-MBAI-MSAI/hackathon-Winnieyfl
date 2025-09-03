"""
Authors: Winnie Li, Ritwik Chakradhar
Creation date: 09/03/2025
Speeding ticket - detect speeding ticket amount based on automobile velocity
"""

def ticket_amount():
    limit = int(input()) # input limit value
    speed = float(input()) # input spped limit
    if(speed-limit<=-10): # check for lower speed case
        return 50
    elif((speed-limit)>=6 and (speed - limit)<=20): #check case between 6 and 20mph
        return 75
    elif ((speed - limit) >= 21 and (speed - limit) <= 40): #check case between 21 and 40 mph
        return 150
    elif ((speed - limit) > 40): # check for speed > 40mph than limit
        return 300
    else:
        return 0

if __name__ == "__main__":
    print(ticket_amount())