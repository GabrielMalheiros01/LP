mq = int(input("Digite a área a ser pintada"))

litros = mq/6
latas = litros/18

if(latas%18 !=0):
    latas+=1
preco = latas*80
galoes = litros/3.6
if(galoes%3.6):
    galoes+=1
preco2 = galoes*25

mistura_lata = int(litros/18.0)
mistura_galao = int((litros - (mistura_lata*18))/3.6)

if(litros - (mistura_lata*18)%3.6 !=0):
    mistura_galao+=1
print("Apenas latas de 18 litros: %s"%latas,'preco:%s'%preco)
print('Apenas galões de 3.6 litros:%s'%galoes,'preco: %s'%preco2)
print('Mistura: %d latas e %d galoes = %.2f' % (
    mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25))))