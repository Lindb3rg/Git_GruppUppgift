

# det finns en lista med årtal
# [1952,1958,1962,1977,1980,1990]
# skriva en loop som tar fram hur många som år mellan 1950 och 1960
#  skriv ut svaret

lista = [1952,1958,1962,1977,1980,1990]
antal = 0 
for tal in lista :
    if tal > 1950 and tal < 1960:
        antal = antal +1
print(antal)        