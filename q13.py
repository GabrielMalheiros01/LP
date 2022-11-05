num = float(input("Digite sua altura:"))
sex = float(input("Digite seu sexo: M/F"))

if(sex=='M'):
    print("Seu peso ideal é:",(72.7*num)-58)
elif(sex=='F'):
    print("Seu peso ideal é:",(62.1*num)-44.7)

