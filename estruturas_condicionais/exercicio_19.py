"""
    Crie um programa que simule um jogo de sorteio com duas bolas: uma vermelha
    e outra azul. Após dez execuções, informe qual cor foi a mais sorteada e as
    quantidades de cada uma.
"""
import random

vermelhas = 0
azuis = 0

for i in range(10):
    sorteio = random.randint(0, 1)
    if(sorteio == 0):
        vermelhas += 1
    elif(sorteio == 1):
        azuis += 1
        
if(vermelhas > azuis):
    print(f'A cor mais sorteada foi vermelha com {vermelhas} bolas e azuis com\
 {azuis} bolas')
 
elif(azuis > vermelhas):
    print(f'A cor mais sorteada foi azul com {azuis} bolas e vermelhas com\
 {vermelhas} bolas')
 
else:
    print(f'Ambas tiveram a mesma quantidade {azuis}')