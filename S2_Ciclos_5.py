total=0

monto=float(input("Total de la compra: "))

while monto!=0:
    if monto<0:
        print("Monto no válido.")
    else:
        total+=monto
    monto=float(input("Total de la compra: "))

if total>1000:
    total-=total*0.1
    print("Aplica un descuento del 10% a su compra")
    
print("Total a pagar: $", total)