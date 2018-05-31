import os

os.chdir('C:\\Users\VF034781\Desktop\Sandbox')

import census2010

def safeget(dct, *keys):
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct

cont = "Yes"

while cont == "Yes":

    state = input("Enter a State: ")
    county = input("Enter a county: ")

    print(safeget(census2010.allData, state, county))

    cont = input("Continue? ")



