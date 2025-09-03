"""
Authors: Winnie Li, Ritwik Chakradhar
Creation date: 09/03/2025
Speeding ticket - detect speeding ticket amount based on automobile velocity
"""

def countchars(st):
    exclude = {' ','.','!',','} # setup exclude character list
    count = 0
    for c in st:
        if c not in exclude: # ensure characters are only counted if not in exclude list
            count +=1 # increment count for each valid character
    return count

if __name__ == "__main__":
    st = input()
    print(countchars(st))