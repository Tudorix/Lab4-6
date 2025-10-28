import lista
import appController
from appController import *
import math

lista = lista.ListaComplexe()
app = appController.Contoller()

def main():
    app.print_initial()
    running = True
    stack_index = 0
    
    while running :
        app.print_menu()
        option = int(input(">>>"))
        
        match option:
            case 1:
                print(lista.lista_numere)
            case 2:
                print(lista.lista_numere)
                lista.list_stack[stack_index] = lista.lista_numere.copy()
                stack_index += 1

                x = getComplexNumber()
                lista.lista_numere = lista.addAtTheEnd(lista_curenta=lista.lista_numere, item=x)
            case 3:
                print(lista.lista_numere)
                lista.list_stack[stack_index] = lista.lista_numere.copy()
                stack_index += 1

                x = getComplexNumber()
                y = getIndex(0 , len(lista.lista_numere))
                lista.lista_numere = lista.addAtIndex(lista_curenta=lista.lista_numere,item=x , index=y)
            case 4:
                if len(lista.lista_numere) > 0:
                    print(lista.lista_numere)
                    lista.list_stack[stack_index] = lista.lista_numere.copy()
                    stack_index += 1

                    y = getIndex(0 , len(lista.lista_numere))
                    lista.lista_numere = lista.deleteAtIndex(lista_curenta=lista.lista_numere,index=y)
                else:
                    print("The list has no numbers currently")
            case 5:
                if len(lista.lista_numere) > 0:
                    print(lista.lista_numere)
                    lista.list_stack[stack_index] = lista.lista_numere.copy()
                    stack_index += 1
                    y = getIndex(0 , len(lista.lista_numere))
                    z = getIndex(y , len(lista.lista_numere))
                        
                    lista.lista_numere = lista.deleteInterval(lista_curenta=lista.lista_numere,indexS=y, indexF=z)
                else:
                    print("The list has no numbers currently")
            case 6:
                if len(lista.lista_numere) > 0:
                    print(lista.lista_numere)
                    lista.list_stack[stack_index] = lista.lista_numere.copy()
                    stack_index += 1
                    x = getComplexNumber()
                    y = getComplexNumber()
                    
                    lista.lista_numere = lista.replaceItem(lista_curenta=lista.lista_numere,oldItem=x, newItem=y)
                else:
                    print("The list has no numbers currently")
            case 7:
                if len(lista.lista_numere) > 0:
                    y = getIndex(0, len(lista.lista_numere))
                    z = getIndex(y, len(lista.lista_numere))

                    print("\n")
                    for i in range(y , z + 1):
                        print(lista.lista_numere[i][1])
                    print("\n")
                else:
                    print("The list has no numbers currently")
            case 8:
                if len(lista.lista_numere) > 0:
                    for i in range(0 , len(lista.lista_numere)):
                        w = lista.lista_numere[i][0]
                        z = lista.lista_numere[i][1]

                        absVal = 0
                        absVal = math.sqrt(pow(w , 2) + pow(z , 2))

                        if absVal < 10:
                            print (lista.lista_numere[i])
                else:
                    print("The list has no numbers currently")
                   
            case 9:
                if len(lista.lista_numere) > 0:
                    for i in range(0 , len(lista.lista_numere)):
                        w = lista.lista_numere[i][0]
                        z = lista.lista_numere[i][1]

                        absVal = 0
                        absVal = math.sqrt(pow(w , 2) + pow(z , 2))

                        if absVal == 10:
                            print (lista.lista_numere[i])
                else:
                    print("The list has no numbers currently")

            #Iteratie 2     
            case 10:
                if len(lista.lista_numere) > 0:
                    y = getIndex(0, len(lista.lista_numere))
                    z = getIndex(y, len(lista.lista_numere))

                    sumW = 0
                    sumI = 0
                    for i in range(y , z + 1):
                        sumW += lista.lista_numere[i][0]
                        sumI += lista.lista_numere[i][1]

                    print(f"\nThe sum is: {sumW} {sumI}i\n")
                else:
                    print("The list has no numbers currently")
            
            case 11:
                if len(lista.lista_numere) > 0:
                    y = getIndex(0, len(lista.lista_numere))
                    z = getIndex(y, len(lista.lista_numere))

                    num1 = lista.lista_numere[y]
                    for i in range(y + 1 , z + 1):
                        num2 = lista.lista_numere[i]
                        
                        whole = (num1[0] * num2[0] - num1[1] * num2[1])
                        imaginary = (num1[0] * num2[1] + num1[1] * num2[0])

                        multiplier = [whole, imaginary]

                    print(f"\nThe multiplication is: {multiplier}\n")
                else:
                    print("The list has no numbers currently")
            case 12:
                if len(lista.lista_numere) > 0:
                    y = getIndex(0, len(lista.lista_numere))
                    z = getIndex(y, len(lista.lista_numere))
            
                    list_to_sort = []
                    for k , v in lista.lista_numere.items():
                        list_to_sort.append(v)

                    list_to_sort = list_to_sort[y:z + 1]
                    
                    for i in range(y , z):
                        for j in range(i , z + 1):
                            elem1 = list_to_sort[i]
                            elem2 = list_to_sort[j]
                            if elem1[1] > elem2[1]:
                                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]

                    print(f"\n{list_to_sort}\n")
                else:
                    print("The list has no numbers currently")
            case 13:
                print(lista.lista_numere)
                lista.list_stack[stack_index] = lista.lista_numere.copy()
                stack_index += 1

                filtered_list = lista.filterPrimeNums(lista_curenta=lista.lista_numere , lista=lista)
                print(f"\n{filtered_list}\n")
            case 14:
                print(lista.lista_numere)
                lista.list_stack[stack_index] = lista.lista_numere.copy()
                stack_index += 1

                x = getCase()
                y = getNumber()
                filtered_list = lista.filterCondition(lista_curenta=lista.lista_numere , lista=lista, case=x, number=y)
                print(f"\n{filtered_list}\n")
            #Iteratie 3
            case 15:
                stack_index -= 1
                lista.lista_numere = lista.list_stack[stack_index]
            case 0:
                running = False

    app.print_exit()
main()