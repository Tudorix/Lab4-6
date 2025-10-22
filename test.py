import lista

lista_test = lista.ListaComplexe()

def test_CheckComplex():
    """
        test function for the chechComplexNumber method
    """
    assert lista_test.checkComplexNumber("4+5i")
    assert not lista_test.checkComplexNumber("4+ri")
    assert not lista_test.checkComplexNumber("fr+i")
    assert lista_test.checkComplexNumber("45")
    assert not lista_test.checkComplexNumber("465+ 84i")

def test_addAtTheEnd():
    """
        test function for the addAtTheEnd method
    """
    assert lista_test.addAtTheEnd(lista_curenta={0:"5" , 1 : "6"} , item=str(7)) == {0:"5" , 1 : "6" , 2 : '7'}

def test_addAtIndex():
    """
        test function for the addAtIndex method
    """
    assert lista_test.addAtIndex(lista_curenta={0:"5" , 1 : "6"} , item=str(7), index=1) == {0:"5" , 1 : "7" , 2 : '6'}

def test_replaceItem():
    """
        test function for the replace method
    """
    assert lista_test.replaceItem(lista_curenta={0:"5" , 1 : "6"} , oldItem="6", newItem="20") == {0:"5" , 1 : "20"} 
    assert lista_test.replaceItem(lista_curenta={0:"5" , 1 : "6" , 2 : "6"} , oldItem="6", newItem="20") == {0:"5" , 1 : "20" , 2 : "20"} 

def test_deleteIndex():
    """
        test function for the deleteAtIndex method
    """
    assert lista_test.deleteAtIndex(lista_curenta={0:"5" , 1 : "6"} , index=1) == {0:"5"} 

def test_deleteInterval():
    """
        test function for the deleteInterval method
    """
    assert lista_test.deleteInterval(lista_curenta={0:"5" , 1 : "6"} , indexS=0, indexF=1) == {} 

def test_unpackNumebr():
    """
        test function for the unpackNumber method
    """
    assert lista_test.unpackNumber("5+6i") == [5,6]
    assert lista_test.unpackNumber("5") == [5,0]

def test_isPrime():
    """
        test function for the isPrime method
    """
    assert lista_test.isPrime(7)
    assert lista_test.isPrime(2)
    assert not lista_test.isPrime(1)
    assert not lista_test.isPrime(4)

def test_filterPrimeNums():
    """
        test function for the filterPrimeNums method
    """
    assert lista_test.filterPrimeNums(lista_curenta={0: '2', 1: '3', 2: '5', 3: '6', 4: '8'} , lista=lista_test) == {0: '6', 1: '8'}

#Execution Block
test_filterPrimeNums()
test_isPrime()
test_CheckComplex()
test_addAtTheEnd()
test_addAtIndex()
test_deleteIndex()
test_deleteInterval()
test_replaceItem()
test_unpackNumebr()