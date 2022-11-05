pesoPeixe=float(input("Digite os kgs do peixe:"))
excesso=0
multa=0.0

if(pesoPeixe<=50):
    print("Não haverá multa.")
else:
    while(pesoPeixe>50):
        excesso+=1
        multa+=4
        pesoPeixe-=1
print("O valor da multa foi:",multa,"R$")
print("O excesso foi:",excesso,"kg")
