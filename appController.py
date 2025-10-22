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
        print("0. Close app")