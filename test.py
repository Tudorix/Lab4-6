import lista

lista_test = lista.ListaComplexe()

def test_CheckComplex():
    assert lista_test.checkComplexNumber("4+5i")
    assert not lista_test.checkComplexNumber("4+ri")
    assert not lista_test.checkComplexNumber("fr+i")
    assert lista_test.checkComplexNumber("45")
    assert not lista_test.checkComplexNumber("465+ 84i")

def test_addAtTheEnd():
    assert lista_test.addAtTheEnd(lista_curenta={0:"5" , 1 : "6"} , item=str(7)) == {0:"5" , 1 : "6" , 2 : '7'}

def test_addAtIndex():
    assert lista_test.addAtIndex(lista_curenta={0:"5" , 1 : "6"} , item=str(7), index=1) == {0:"5" , 1 : "7" , 2 : '6'}

def test_replaceItem():
    assert lista_test.replaceItem(lista_curenta={0:"5" , 1 : "6"} , oldItem="6", newItem="20") == {0:"5" , 1 : "20"} 
    assert lista_test.replaceItem(lista_curenta={0:"5" , 1 : "6" , 2 : "6"} , oldItem="6", newItem="20") == {0:"5" , 1 : "20" , 2 : "20"} 

def test_deleteIndex():
    assert lista_test.deleteAtIndex(lista_curenta={0:"5" , 1 : "6"} , index=1) == {0:"5"} 

def test_deleteInterval():
    assert lista_test.deleteInterval(lista_curenta={0:"5" , 1 : "6"} , indexS=0, indexF=1) == {} 

def test_unpackNumebr():
    assert lista_test.unpackNumber("5+6i") == [5,6]
    assert lista_test.unpackNumber("5") == [5]

test_CheckComplex()
test_addAtTheEnd()
test_addAtIndex()
test_deleteIndex()
test_deleteInterval()
test_replaceItem()
test_unpackNumebr()