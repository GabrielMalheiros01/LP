mq = int(input("Digite a área a ser pintada"))

litros = mq/3

latas = (int(litros/18))
if(litros%18 !=0):
    latas+=1
print("A quantidade de lata gasta foi:",latas)
print("O valor total é:",latas*80)

