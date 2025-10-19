class ListaComplexe:
    lista_numere = {}

    def addAtTheEnd(self,lista_curenta, item) -> dict:
        lista_curenta[len(lista_curenta)] = item
        return lista_curenta
    
    def addAtIndex(self,lista_curenta, item , index) -> dict:
        items = list(lista_curenta.items())
        items.insert(index , (index , item))
        for i in range(index + 1 , len(items)):
            key, value = items[i]
            key = key + 1       
            items[i] = (key, value) 

        return dict(items)
    
    def deleteAtIndex(self,lista_curenta, index) -> dict:
        items = list(lista_curenta.items())
        del items[index]
        for i in range(index + 1 , len(items)):
            key, value = items[i]
            key = key - 1       
            items[i] = (key, value) 

        return dict(items)
    
    def deleteInterval(self,lista_curenta, indexS , indexF) -> dict:
        items = list(lista_curenta.items())
        del items[indexS : indexF + 1]
        for i in range(indexS , len(items)):
            key, value = items[i]
            key = key - (indexF - indexS + 1)       
            items[i] = (key, value) 

        return dict(items)
    
    def replaceItem(self, lista_curenta, oldItem, newItem) -> dict:
        for k , v in lista_curenta.items():
            if v == oldItem:
                lista_curenta[k] = newItem

        return lista_curenta   

    def checkComplexNumber(self,number):
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
        parts = x.split('+')
        parts[0] = int(parts[0])
            
        if len(parts) == 2:
            parts[1] = parts[1].split("i")
            parts[1] = int(parts[1][0]) 
            
        return parts
        


