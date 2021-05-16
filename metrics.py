import random

#nxn 2d list generating method
def myList(rows, cols):
    matrix = []
    #The loop that fills the sent row and column up to 2d list with 100-200 random numbers
    for r in range(0, rows):
        matrix.append([random.randrange(100,200) for c in range(0, cols)])
    return matrix

print("-----Write List-----")    
#The function that prints the list as a table according to the value sent
def writeList(r,c):
    print(myList(r, c))

#call writeList function
writeList(5,5)

print("-----Write diagonal list-----")

#function that prints the list diagonally
def writeDiagonalList(r,c):
   for i in range(len(myList(r,c))):
    for j in range(len(myList(r,c)[i])):
            print(myList(r,c)[i][j], end=' ')
    print()

#call writeDiagonalList function
writeDiagonalList(5,5)

print("-----Write Odd Number List-----")

#The function that writes the odd numbers in a list of random numbers
def writeOddList(r,c):
   for i in range(len(myList(r,c))):
    for j in range(len(myList(r,c)[i])):
        num = myList(r,c)[i][j]
        if (num % 2) == 1:  
            print(num, end=' ')
    print()

#call writeOddNumber function
writeOddList(5,5)