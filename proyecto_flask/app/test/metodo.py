
def calculo_primo(n):
    cantidad = 0
    primos = ''
    for i in range(1, n + 1):
        for j in range(1,i+1):
            if i % j == 0 :
                cantidad += 1
            if cantidad > 2 :
                break
            if j == i :
                #print('El número '+str(i)+' es primo')
                primos += str(i)+', '
        
        cantidad = 0
    return primos    
    

#print(calculo_primo(3))
def test_opciones():
    assert calculo_primo(3) == '1, 2, 3, ', 'Error no coinciden'

if __name__ == '__main__':
    test_opciones()
