import lista

lista_test = lista.ListaComplexe()

def test_addAtTheEnd():
    """
        test function for the addAtTheEnd method
    """
    assert lista_test.addAtTheEnd(lista_curenta={0:[5,0] , 1 : [6,0]} , item=[7,0]) == {0:[5,0] , 1 : [6,0], 2 : [7,0]}

def test_addAtIndex():
    """
        test function for the addAtIndex method
    """
    assert lista_test.addAtIndex(lista_curenta={0:[5,0] , 1 : [6,0]} , item=[7, 0], index=1) == {0:[5,0] ,1: [7,0] ,2 : [6,0]}

def test_replaceItem():
    """
        test function for the replace method
    """
    assert lista_test.replaceItem(lista_curenta={0:[5,0] , 1 : [6,0]} , oldItem=[6 , 0], newItem=[20 , 0]) == {0:[5,0] , 1 : [20,0]}
    assert lista_test.replaceItem(lista_curenta={0:[5,0] , 1 : [6,0], 2 : [6,0]} , oldItem=[6 , 0], newItem=[20 , 0]) == {0:[5,0] , 1 : [20,0], 2 : [20,0]}

def test_deleteIndex():
    """
        test function for the deleteAtIndex method
    """
    assert lista_test.deleteAtIndex(lista_curenta={0:[5,0] , 1 : [6,0]} , index=1) == {0:[5 , 0]} 

def test_deleteInterval():
    """
        test function for the deleteInterval method
    """
    assert lista_test.deleteInterval(lista_curenta={0:[5,0] , 1 : [6,0]}, indexS=0, indexF=1) == {} 

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
    assert lista_test.filterPrimeNums(lista_curenta={0: [2,0], 1: [3,0], 2: [5,0], 3: [6,0], 4: [8,0]} , lista=lista_test) == {0: [6,0], 1: [8,0]}

def test_filterCondition():
    """
        test function for the filterCondition method
    """
    assert lista_test.filterCondition(lista_curenta={0: [2,0]}  , lista=lista_test, case = 1, number = 10) == {}

#Execution Block
test_filterPrimeNums()
test_isPrime()
test_addAtTheEnd()
test_addAtIndex()
test_deleteIndex()
test_deleteInterval()
test_replaceItem()
test_filterCondition()
