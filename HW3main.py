# HW 3, Name Finder Program based on most popular 2021 names, By Alex Jimenez

# User input validation to make sure y or n is entered
def yes_or_no():
    repeat = input("Enter y to search through the most popular names of 2021 or n to not: ")
    while (repeat != "y" and repeat != "n"):
        print("Invalid letter")
        repeat = input("Enter y to search through the most popular names of 2021 or n to not: ")
    return repeat

# User input validation to make sure s or t is entered and determines if s or 2 is returned
def searchType():
    search = input("Enter s to search a specific name or t to search a top # of names: ")
    while (search != "s" and search != "t"):
        print("Invalid letter")
        search = input("Enter s to search a specific name or t to search a top # of names: ")
    if (search == "s"):
        name = input("Enter the name you wish to search for (first letter capitalized): ")
        return name
    else:
        option = 2
        return option

# Function searches the female list for a specific name or searches for the top # of names
def searchFemale(search, girlNames, girlTotal):
    if (search == 2):
        amount = validNumber()
        print("The top", amount, "popular female names are:")
        for i in range(amount):
            print(girlNames[i], ":", end=" ")
            print(girlTotal[i], "babies were given this name")
    else:
        i = 0
        found = False
        while (i < len(girlNames) and not found):
            if (girlNames[i] == search):
                found = True
                print(girlTotal[i], "babies were given the name", girlNames[i])
            i = i + 1
        if (found == False):
            print(search, "was not in the top 100 most popular female names.")

# Function searches the male list for a specific name or searches for the top # of names
def searchMale(search, boyNames, boyTotal):
    if (search == 2):
        amount = validNumber()
        print("The top", amount, "popular male names are:")
        for i in range(amount):
            print(boyNames[i], ":", end=" ")
            print(boyTotal[i], "babies were given this name")
    else:
        i = 0
        found = False
        while (i < len(boyNames) and not found):
            if (boyNames[0] == search):
                found = True
                print(boyTotal[i], "babies were given the name", boyNames[i])
            i = i + 1
        if (found == False):
            print(search, "was not in the top 100 most popular male names.")

# User input validation to make sure only numbers 1-100 is entered
def validNumber():
    amount = int(input("Enter the # of names (1-100) that you want to see: "))
    while (amount < 1 or amount > 100):
        print("Invalid number")
        amount = int(input("Enter the # of names (1-100) that you want to see: "))
    return amount

# User input validation to make sure m or f is entered
def validGender():
    gender = input("Which names do you wish to see m(male) or f(female): ")
    while (gender != "m" and gender != "f"):
        print("Invalid, please enter m, f, or b")
        gender = input("Which names do  you wish to see m(male) or f(female): ")
    return gender

# Function searches and reads in the top 100 female names then stores it into two parallel lists
def femaleData(names, total):
    infile = open("data.txt", "r")
    i = 0
    while (i < 100):
        line = infile.readline().rstrip().split(",")
        names.append(line[0])
        total.append(line[2])
        i = i + 1

# Function searches and reads in the top 100 male names then stores it into two parallel lists
def maleData(names, total):
    infile = open("data.txt", "r")
    line = infile.readline().rstrip().split(",")
    i = 0
    while (line[1] == "F"):
        line = infile.readline().rstrip().split(",")
    names.append(line[0])
    total.append(line[2])
    while (i < 99):
        line = infile.readline().rstrip().split(",")
        names.append(line[0])
        total.append(line[2])
        i = i + 1

# Main calls functions to store data in 4 lists then determines if name searching occurs
def main():
    girlNames = []
    girlTotal = []
    femaleData(girlNames, girlTotal)

    boyNames = []
    boyTotal = []
    maleData(boyNames, boyTotal)
    repeat = yes_or_no()
    while (repeat != "n"):
        gender = validGender()
        search = searchType()
        if (gender == "m"):
            searchMale(search, boyNames, boyTotal)
        else:
            searchFemale(search, girlNames, girlTotal)
        repeat = input("Enter y to search through the most popular names of 2021 or n to not: ")

# Call to main
main()