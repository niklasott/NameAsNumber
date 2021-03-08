import string

#   function to return each letter of the alphabet
alphabet = string.ascii_lowercase
#   dictionary: letter -> number
alphabetNumbered = {alphabet[x-1]:x for x in range(1, 27)}

#   Test -  print out the dictionary
#   print (alphabetNumbered)

#   Asking user to input name
nameInput = input("Enter name: ")


#   Function to sum up the Values
def addValues(name):
    #   transform since no case-sensitivity
    name = name.lower()
    sum = 0
    for x in name:
        # checks if letter entered is valid, and ignores if not
        if(x in alphabetNumbered):    
            sum += alphabetNumbered[x]
        else:
            pass
                
    return sum

print(addValues(nameInput))


#   TESTS
print("TEST OUTPUTS:")
print(addValues("A"))
print(addValues("Z"))
print(addValues("Az"))
print(addValues("Test"))
print(addValues("Te st"))
print(addValues("Ivan"))
print(addValues("12drei"))
print(addValues("äa"))
print(addValues("#-'"))
