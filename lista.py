class ListaComplexe:
    lista_numere = {}
    
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
        if n < 2: return False
        if n % 2 == 0 and n != 2: return False
        for i in range(3 , int(n/2) + 1):
            if n % i == 0:
                return False
        return True
    
    def filterPrimeNums(self, lista_curenta , lista):
        filtered_dict = {}
        index = 0
        i = 0
        lim = len(lista_curenta)
        while i < lim:
            unpacked = lista.unpackNumber(lista_curenta[i])
            if not lista.isPrime(unpacked[0]):
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

    def checkComplexNumber(self,number):
        """
        Check if the input is a correct complex number of format: "a" or "a+bi"
        number - string
        Return - true if the number is correct, false ohterwise
        """
        if " " in number: return False
        if '+' in number:
            parts = number.split('+')
            
            try:
                parts[0] = int(parts[0])
            except:
                return False
            
            if not "i" in parts[1]:
                return False
            
            parts[1] = parts[1].split('i')
            
            try:
                parts[1][0] = int(parts[1][0])
            except:
                return False

        else:
            try:
                number = int(number)
            except:
                return False
            
        return True
    
    def unpackNumber(self, x):
        """
        Covert the complex number to integers
        x - string
        Return - list of integers
        """
        parts = x.split('+')
        parts[0] = int(parts[0])
            
        if len(parts) == 2:
            parts[1] = parts[1].split("i")
            parts[1] = int(parts[1][0]) 
        else:
            parts.append(0)
            
        return parts
        


