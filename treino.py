#Script para treinos feito por Fragoso dia 14/05/2019

import os
import sys
import time
from datetime import date   

print('Preparando para escalar as máquinas.')
os.system('eb use app-worker')
os.system('eb scale 10')
print('Finalizado a escalada das máquinas')
time.sleep(180)

os.system('eb use app-web')


bg_id = os.environ['K_BG_ID']
hoje = date.today()
data1 = str(hoje)
data2 = str(date.fromordinal(hoje.toordinal()+1))

lojas_id = ['loja_id']

treino = 0

print(f'\nPreparando o treinamento das lojas para o grupo economico {bg_id}')

for loja in lojas_id:
    os.system("eb ssh -n 1 -c 'sudo docker exec -t $(sudo docker ps -q) bash -c \"bundle exec rake kikker:supply:by_store["+bg_id+","+loja+","+data1+","+data2+"]\"'")
    time.sleep(60)
    treino = treino + 1

    if (treino == 3):
        print('\nAguardando treinos sendo iniciados.\n')
        time.sleep(600)
        treino = 0
        #print('\nDando continuidade nos treinos.\n')


print('\nTreinos iniciados, acompanhe pelo Sidekiq e aguarde a próxima etapa...')
time.sleep(300)

#print('Iniciando treino do CD...')
#os.system("eb ssh -c 'sudo docker exec -t $(sudo docker ps -q) bash -c \"bundle exec rake kikker:supply:cd["+bg_id+","+data1+","+data2+"]\"'")

#print('\nAguardando finalização do treino do CD.')
time.sleep(120)

print('\nTreino das lojas finalizados')

print('\nDiminuindo as máquinas')

os.system('eb use app-worker')
os.system('eb scale 1')

print('\nProcesso de treinamento finalizado.')


