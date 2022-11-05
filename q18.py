mb = float(input("Digite o tamanho do arquivo"))
velocidade = float(input("Digite a velocidade da sua net"))
print('Tempo aproximado de download: %.0f Minutos ' %((mb / velocidade) * 60))