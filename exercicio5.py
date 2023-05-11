#Existe um aeroporto com apenas uma pista para pousos e decolagens. Faça um programa em Python onde os processos são
#aviões que pousam ou decolam neste aeroporto. Deve haver um controle do acesso a pista, que deve ser exclusiva, i.e., dois
#aviões não podem usá-la ao mesmo tempo. O programa deve simular uma situação onde os aviões (suponha dez) utilizam a
#pista para pousos ou decolagens.

from multiprocessing import Process
import os
import time
import random


def aviao(n, empresa):
    print('\no aviao ',n,' da '+empresa+' esta usando a pista')
    print('protocolo de funcionamento da pista (parent process): ', os.getppid())
    print('codigo do aviao atual (process id): ', os.getpid())
    p = random.randint(1,5)
    time.sleep(p)
    print('o aviao ',n,' da '+empresa+' usou a pista por ',p,'s. Pista liberada!')

if __name__=='__main__':
    print('log de utilizaçao da pista do aeroporto VoeBemAvioneiro\n')

    avioes = []

    for i in range(10):
        if i%2==0:
            a = Process(target=aviao, args=(i,'Azul'))
        if i%2==1:
            a = Process(target=aviao, args=(i,'Latam'))
        avioes.append(a)
        a.start()
        a.join() # o join não vai deixar que um avião use a pista se estiver ocupada
    
    print('ja voaram 10 avioes, tá bom por hoje, chega, vamos fechar a pista\n')
    print('relatorio com o protocolo da pista(parent process) e os codigos dos avioes (process id):')
    for j in range(10): print('\n',avioes[j])
    
