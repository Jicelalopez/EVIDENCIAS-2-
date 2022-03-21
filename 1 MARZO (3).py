def validar(email):
    caracterBuscado="@"
    emailValido=False
    for c in email:
        if c==caracterBuscado:
            return False
        
        
direccion=input("tu email")
if validar(direccion):
    print("Direccion valida")
else:
    print("Dirección invalida")