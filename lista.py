import math

class ListaComplexe:
    lista_numere = {}
    list_stack = {}
    
    def addAtTheEnd(self,lista_curenta, item) -> dict:
        """
        Adds the element "item" at end of "lista_curenta"
        lista_curenta - dict
        item - string
        Return - modified dictionary
        """
        lista_curenta[len(lista_curenta)] = item
        return lista_curenta
    
    def isPrime(self, n):
        """
        Checks if a number is prime
        n - int
        """
        if n < 2: return False
        if n % 2 == 0 and n != 2: return False
        for i in range(3 , int(n/2) + 1):
            if n % i == 0:
                return False
        return True
    
    def filterPrimeNums(self, lista_curenta , lista):
        """
        Filteres out the elements with a prime whole number
        lista_curenta - dict
        lista - type = Lista
        """
        filtered_dict = {}
        index = 0
        i = 0
        lim = len(lista_curenta)
        while i < lim:
            if not lista.isPrime(lista_curenta[i][0]):
                filtered_dict[index] = lista_curenta[i]
                index += 1
            i += 1
                
        return filtered_dict
    
    def filterCondition(self, lista_curenta , lista, case, number):
        """
        Filteres out the elements that are <,=,> that a given number
        lista_curenta - dict
        lista - type = Lista
        case - int
        number - int
        """
        filtered_dict = {}
        index = 0
        i = 0
        lim = len(lista_curenta)
        while i < lim:
            w = lista_curenta[i][0]
            z = lista_curenta[i][1]

            absVal = math.sqrt(pow(w , 2) + pow(z , 2))
            if (case == 1 and absVal >= number) or (case == 2 and absVal != number) or (case == 3 and absVal <= number):
                filtered_dict[index] = lista_curenta[i]
                index += 1
            i += 1
                
        return filtered_dict
    
    def addAtIndex(self,lista_curenta, item , index) -> dict:
        """
        Adds the element "item" at the position "index" in "lista_curenta"
        lista_curenta - dict
        index - int
        item - string
        Return - modified dictionary
        """
        items = list(lista_curenta.items())
        items.insert(index , (index , item))
        for i in range(index + 1 , len(items)):
            key, value = items[i]
            key = key + 1       
            items[i] = (key, value) 

        return dict(items)
    
    def deleteAtIndex(self,lista_curenta, index) -> dict:
        """
        Deletes the element from "lista_curenta" that has the index "index"
        lista_curenta - dict
        index - int
        Return - modified dictionary
        """
        items = list(lista_curenta.items())
        del items[index]
        for i in range(index + 1 , len(items)):
            key, value = items[i]
            key = key - 1       
            items[i] = (key, value) 

        return dict(items)
    
    def deleteInterval(self,lista_curenta, indexS , indexF) -> dict:
        """
        Deletes the elements from "lista_curenta" that have the index starting from "indexS" to "indexF"
        lista_curenta - dict
        indexS - int
        indexF - int
        Return - modified dictionary
        """
        items = list(lista_curenta.items())
        del items[indexS : indexF + 1]
        for i in range(indexS , len(items)):
            key, value = items[i]
            key = key - (indexF - indexS + 1)       
            items[i] = (key, value) 

        return dict(items)
    
    def replaceItem(self, lista_curenta, oldItem, newItem) -> dict:
        """
        Replaces the elements from "lista_curenta" of valuea "oldItem" with the value "newValue"
        lista_curenta - dict
        oldItem - string
        newItem - string
        Return - modified dictionary
        """
        for k , v in lista_curenta.items():
            if v == oldItem:
                lista_curenta[k] = newItem

        return lista_curenta   
