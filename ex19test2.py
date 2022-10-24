#Spiritual Routine
from typing import ChainMap


def spiritual_routine(bible_reading, meditation, name01):
    print(f"""
    Hi, {name01},You read the bible {bible_reading} times 
    and meditated {meditation} times today.
    You have done well {name01}""")
    print(f"    Really.... {name01}")



#Using variables
reading = 3
meditation  = 4
name = "Champ" 
spiritual_routine(reading, meditation, name)

#substituting parameters directly
spiritual_routine(10, 6, "Keiko")

#Mathematics
spiritual_routine(4+2, 3+5, "Davo")

#Using variables + Maths
spiritual_routine(reading+2, meditation+8, "Brett")