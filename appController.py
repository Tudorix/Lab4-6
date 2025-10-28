class Contoller:

    def print_initial(self):
        """
        Prints the introduction message of the app
        """
        print("Welcome to your Complex Numbers Editor Program(C.N.E.P) \n" \
        "What do you want to do today?")

    def print_exit(self):
        """
        Prints the end message of the app
        """
        print("Have a nice day!")

    def print_menu(self):
        """
        Prints the menu of the app
        """
        print("1. Show list")
        print("2. Add element at the end of list")
        print("3. Add element at a specified index")
        print("4. Delete element at a specified index")
        print("5. Delete element from a specified range")
        print("6. Replace elements with a specified value")
        print("7. Show the imaginary part of specivied range")
        print("8. Show the numbers with the abs value greater than 10")
        print("9. Show the numbers with the abs value is equal to 10")
        print("10. Show the sum of the numbers in the range")
        print("11. Show the multiplication of the numbers in the range")
        print("12. Show a sorted range of numbers")
        print("13. Filter out all numbers with a whole prime number")
        print("14. Filter out all numbers that have the absolute value <,=,> that another number")
        print("15. Undo")
        print("0. Close app")

def getComplexNumber():
    correct = False
    x = 0
    while not correct:
        correct = True
        x = input("Insert a complex number : ")
        x = x.split()
        if len(x) != 2: 
            correct = False
            print("The input was incorrect")
        else:
            try:
                x[0] = int(x[0])
                x[1] = int(x[1])
            except:
                correct = False
                print("The input was incorrect")

    return x

def getNumber():
    correct = False
    x = 0
    while not correct:
        correct = True
        x = input("What should it be compared to? (number) :")
        try:
            x = int(x)
        except:
            correct = False
            print("The input was incorrect")

    return x

def getCase():
    correct = False
    x = 0
    while not correct:
        correct = True
        x = input("How should the number be? (< ; = ; >) :")
        if x != ">" and x != "=" and x != "<": 
            correct = False
            print("The input was incorrect")
        else:
            match x:
                case "<": x = 1
                case "=": x = 2
                case ">": x = 3

    return x

def getIndex(start , fin):
    correct = False
    x = 0
    while not correct:
        correct = True
        x = input("Insert a index number : ")
        try:
            x = int(x)
            if x > fin and x <= start:
                correct = False
                print("The input was incorrect")
        except:
            correct = False
            print("The input was incorrect")

    return x