import lista
import appController
import math

lista = lista.ListaComplexe()
app = appController.Contoller()

def main():
    app.print_initial()
    running = True
    
    while running :
        app.print_menu()
        option = int(input(">>>"))
        
        match option:
            case 1:
                print(lista.lista_numere)
            case 2:
                x = input("Insert a complex number to add (format: a+bi) : ")
                while not lista.checkComplexNumber(str(x)):
                    print("The input was not correct. Please try again")
                    x = input("(format: a+bi) : ")
                
                lista.lista_numere = lista.addAtTheEnd(lista_curenta=lista.lista_numere, item=x)
            case 3:
                x = input("Insert a complex number to add (format: a+bi) : ")
                while not lista.checkComplexNumber(str(x)):
                    print("The input was not correct. Please try again")
                    x = input("(format: a+bi) : ")

                y = -1
                aux = True
                while aux:
                    try:
                        y = int(input("Insert the index where the number should be placed: "))

                        if y >= 0 and y <= len(lista.lista_numere):
                            aux = False
                            print("Input invalid or out of range, Please try again")
                    except:
                        pass
                lista.lista_numere = lista.addAtIndex(lista_curenta=lista.lista_numere,item=x , index=y)
            case 4:
                if len(lista.lista_numere) > 0:
                    y = -1
                    aux = True
                    while aux:
                        try:
                            y = int(input("Insert the index where the number should be deleted: "))

                            if y >= 0 and y <= len(lista.lista_numere):
                                aux = False
                        except:
                            print("Input invalid or out of range, Please try again")
                            pass
                    lista.lista_numere = lista.deleteAtIndex(lista_curenta=lista.lista_numere,index=y)
                else:
                    print("The list has no numbers currently")
            case 5:
                if len(lista.lista_numere) > 0:
                    y = -1
                    aux = True
                    while aux:
                        try:
                            y = int(input("Insert the index where the deletion should start: "))

                            if y >= 0 and y <= len(lista.lista_numere):
                                aux = False
                        except:
                            print("Input invalid or out of range, Please try again")

                    z = -1
                    aux = True
                    while aux:
                        try:
                            z = int(input("Insert the index where the deletion should end: "))

                            if z > y and z <= len(lista.lista_numere):
                                aux = False
                        except:
                            print("Input invalid or out of range, Please try again")

                    lista.lista_numere = lista.deleteInterval(lista_curenta=lista.lista_numere,indexS=y, indexF=z)
                else:
                    print("The list has no numbers currently")
            case 6:
                x = input("Insert a complex numer to replace (format: a+bi) : ")
                while not lista.checkComplexNumber(str(x)):
                    print("The input was not correct. Please try again")
                    x = input("(format: a+bi) : ")

                y = input("Insert the new value (format: a+bi) : ")
                while not lista.checkComplexNumber(str(x)):
                    print("The input was not correct. Please try again")
                    x = input("(format: a+bi) : ")
                
                lista.lista_numere = lista.replaceItem(lista_curenta=lista.lista_numere,oldItem=x, newItem=y)
            case 7:
                y = -1
                aux = True
                while aux:
                    try:
                        y = int(input("Insert the index where the deletion should start: "))

                        if y >= 0 and y <= len(lista.lista_numere):
                            aux = False
                    except:
                        print("Input invalid or out of range, Please try again")

                z = -1
                aux = True
                while aux:
                    try:
                        z = int(input("Insert the index where the deletion should end: "))

                        if z >= y and z <= len(lista.lista_numere):
                            aux = False
                    except:
                        print("Input invalid or out of range, Please try again")
                
                for i in range(y , z + 1):
                    unpacked = lista.unpackNumber(lista.lista_numere[i])
                    if(len(unpacked) == 2):
                        print(unpacked[1],'i')
                    else:
                        print("0 i")
                
            case 8:
                for i in range(0 , len(lista.lista_numere)):
                    unpacked = lista.unpackNumber(lista.lista_numere[i])
                    absVal = 0
                    if(len(unpacked) == 2):
                        absVal = math.sqrt(pow(unpacked[0] , 2) + pow(unpacked[1] , 2))
                    else:
                        absVal = math.sqrt(pow(unpacked[0] , 2))

                    if absVal < 10:
                        print (lista.lista_numere[i])
                   
            case 9:
                for i in range(0 , len(lista.lista_numere)):
                    unpacked = lista.unpackNumber(lista.lista_numere[i])
                    absVal = 0
                    if(len(unpacked) == 2):
                        absVal = math.sqrt(pow(unpacked[0] , 2) + pow(unpacked[1] , 2))
                    else:
                        absVal = math.sqrt(pow(unpacked[0] , 2))

                    if absVal == 10:
                        print (lista.lista_numere[i])

            #Iteratie 2     
            case 10:
                y = -1
                aux = True
                while aux:
                    try:
                        y = int(input("Insert the index where the deletion should start: "))

                        if y >= 0 and y <= len(lista.lista_numere):
                            aux = False
                    except:
                        print("Input invalid or out of range, Please try again")

                z = -1
                aux = True
                while aux:
                    try:
                        z = int(input("Insert the index where the deletion should end: "))

                        if z >= y and z <= len(lista.lista_numere):
                            aux = False
                    except:
                        print("Input invalid or out of range, Please try again")
                
                sumW = 0
                sumI = 0
                for i in range(y , z + 1):
                    unpacked = lista.unpackNumber(lista.lista_numere[i])
                    sumW += unpacked[0]
                    if len(unpacked) == 2:
                        sumI += unpacked[1]

                print(f"\nThe sum is: {sumW} {sumI}i\n")
            
            case 11:
                y = -1
                aux = True
                while aux:
                    try:
                        y = int(input("Insert the index where the deletion should start: "))

                        if y >= 0 and y <= len(lista.lista_numere):
                            aux = False
                    except:
                        print("Input invalid or out of range, Please try again")

                z = -1
                aux = True
                while aux:
                    try:
                        z = int(input("Insert the index where the deletion should end: "))

                        if z >= y and z <= len(lista.lista_numere):
                            aux = False
                    except:
                        print("Input invalid or out of range, Please try again")
                
                multiplier = lista.lista_numere[y]
                for i in range(y + 1 , z + 1):
                    unpacked1 = lista.unpackNumber(multiplier)
                    unpacked2 = lista.unpackNumber(lista.lista_numere[i])
                    
                    whole = (unpacked1[0] * unpacked1[0] - unpacked1[1] * unpacked2[1])
                    imaginary = (unpacked1[0] * unpacked2[1] - unpacked1[1] * unpacked2[0])

                    multiplier = f"{whole}+{imaginary}i"

                print(f"\nThe multiplication is: {multiplier}\n")

            case 12:
                y = -1
                aux = True
                while aux:
                    try:
                        y = int(input("Insert the index where the deletion should start: "))

                        if y >= 0 and y <= len(lista.lista_numere):
                            aux = False
                    except:
                        print("Input invalid or out of range, Please try again")

                z = -1
                aux = True
                while aux:
                    try:
                        z = int(input("Insert the index where the deletion should end: "))

                        if z >= y and z <= len(lista.lista_numere):
                            aux = False
                    except:
                        print("Input invalid or out of range, Please try again")
                
                list_to_sort = []
                for k , v in lista.lista_numere.items():
                    list_to_sort.append(v)

                list_to_sort = list_to_sort[y:z + 1]
                
                for i in range(y , z):
                    for j in range(i , z + 1):
                        elem1 = lista.unpackNumber(list_to_sort[i])
                        elem2 = lista.unpackNumber(list_to_sort[j])
                        if elem1[1] > elem2[1]:
                            list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]

                print(f"\n{list_to_sort}\n")

            case 13:
                lista.lista_numere = lista.filterPrimeNums(lista_curenta=lista.lista_numere , lista=lista)
                print(f"\n{lista.lista_numere}\n")
            case 0:
                running = False

    app.print_exit()

main()