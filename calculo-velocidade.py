"""
Cálculo de Velocidade média e Aceleração média em Python by Gabriel Lima
"""
print('Bem-vindo a calculadora Velocidade média e Aceleração média em Python!')


def inicio():
    while True:
        calcular = int(input('O que deseja calcular?\n'
                             'Converter km/h em m/s: Digite 1\n'
                             'Converter m/s em km/h: Digite 2\n'
                             'Velocidade Média: Digite 3\n'
                             'Aceleração Média: Digite 4\n'
                             'Encerrar Programa: Digite 5\n'))
        if calcular not in [1, 2, 3, 4, 5]:
            print("Escolha um valor válido \n")
            continue
        if calcular == 5:
            exit()
        if calcular == 1:
            converter1()
        if calcular == 2:
            converter2()
        if calcular == 3:
            vel_media()
        if calcular == 4:
            aceleracao_media()


# km por hora em metro por segundo
def converter1():
    km = float(input('Qual km/h deseja converter para m/s?: '))
    ms = km / 3.6
    print(f'{km} km/h é {ms} m/s \n')


# metro por segundo em km por hora
def converter2():
    ms = float(input('Qual m/s deseja converter para km/h?: '))
    km = ms * 3.6
    print(f'{ms} m/s é {km} km/h \n')


def vel_media():
    var_espaco = ''
    var_tempo = ''
    while True:
        um_espaco = int(input('Qual a unidade de medida do espaço?:\n'
                              'Km: Digite 1\n'
                              'Metros: Digite 2\n'
                              'Voltar para o Inicio: Digite 3\n'))
        if um_espaco not in [1, 2, 3]:
            print("Escolha um valor válido \n")
            continue
        if um_espaco == 3:
            inicio()
        if um_espaco == 1:
            var_espaco = 'km'
        if um_espaco == 2:
            var_espaco = 'm'
        if um_espaco in [1, 2]:
            while True:
                um_tempo = int(input('Qual a unidade de medida do tempo?:\n'
                                     'Horas: Digite 1\n'
                                     'Segundos: Digite 2\n'
                                     'Voltar para o Inicio: Digite 3\n'))
                if um_tempo not in [1, 2, 3]:
                    print("Escolha um valor válido \n")
                    continue
                if um_tempo == 1:
                    var_tempo = 'h'
                if um_tempo == 2:
                    var_tempo = 's'
                if um_tempo != um_espaco:
                    print("ERRO: Unidades diferentes! \n")
                    inicio()
                if um_tempo == um_espaco:
                    while True:
                        calc = int(input('O que deseja calcular?: \n'
                                         'Espaço: Digite 1\n'
                                         'Tempo: Digite 2\n'
                                         'Velocidade média: Digite 3\n'
                                         'Voltar para inicio: Digite 4\n'))
                        if calc not in [1, 2, 3, 4]:
                            print("Escolha um valor válido \n")
                            continue
                        if calc == 4:
                            inicio()
                        if calc == 1:
                            tempo = float(input(f'Qual a variação do tempo em {var_tempo}?:\n '))
                            vm = float(input(f'Qual a velocidade média em {var_espaco}?:\n '))
                            esp = vm * tempo
                            print(f'A variação de espaço percorrido é de {esp} {var_espaco}')
                            inicio()
                        if calc == 2:
                            vm = float(input(f'Qual a velocidade média em {var_espaco}?:\n '))
                            espaco = float(input(f'Qual a variação do espaço em {var_espaco}?:\n'))
                            temp = espaco / vm
                            print(f'A variação de tempo é de {temp} {var_tempo}')
                            inicio()
                        if calc == 3:
                            espaco = float(input(f'Qual a variação do espaço em {var_espaco}?:\n'))
                            tempo = float(input(f'Qual a variação do tempo em {var_tempo}?:\n '))
                            vm = espaco / tempo
                            print(f'A velocidade média é de {vm} {var_espaco}/{var_tempo})')
                            inicio()
                if um_tempo == 3:
                    inicio()


def aceleracao_media():
    while True:
        um_velocidade = int(input('Sua variação de velocidade já está em m/s ?\n'
                                  'Sim: Digite 1\n'
                                  'Não: Digite 2\n'
                                  'Voltar para o Inicio: Digite 3\n'))
        if um_velocidade not in [1, 2, 3]:
            print("Escolha um valor válido \n")
            continue
        if um_velocidade == 3:
            inicio()
        if um_velocidade == 2:
            print('Favor converter para m/s!')
            converter1()
        if um_velocidade == 1:
            while True:
                um_tempo = int(input('Sua variação de tempo já está em segundos?\n'
                                     'Sim: Digite 1\n'
                                     'Não: Digite 2\n'
                                     'Voltar para o Inicio: Digite 3\n'))
                if um_tempo not in [1, 2, 3]:
                    print("Escolha um valor válido \n")
                    continue
                if um_tempo == 3:
                    inicio()
                if um_tempo == 2:
                    print('Favor converter para segundos!')
                    continue
                if um_tempo == 1:
                    while True:
                        calc = int(input('O que deseja calcular?: \n'
                                         'Aceleração Média: Digite 1\n'
                                         'Variação da velocidade: Digite 2\n'
                                         'Variação do tempo: Digite 3\n'
                                         'Voltar para inicio: Digite 4\n'))
                        if calc not in [1, 2, 3, 4]:
                            print("Escolha um valor válido \n")
                            continue
                        if calc == 4:
                            inicio()
                        if calc == 1:
                            tempo = float(input(f'Qual a variação do tempo ?:\n '))
                            vm = float(input(f'Qual a variação da velocidade em metros?:\n '))
                            a = vm / tempo
                            print(f'A aceleração média é de {a} m/s²')
                            inicio()
                        if calc == 2:
                            a = float(input(f'Qual a aceleração média ?:\n '))
                            temp = float(input(f'Qual a variação do tempo ?:\n'))
                            vel = a * temp
                            print(f'A variação de velocidade é de {vel} m/s')
                            inicio()
                        if calc == 3:
                            vel = float(input(f'Qual a variação da velocidade em metros?:\n'))
                            a = float(input(f'Qual a aceleração média ?:\n '))
                            temp = vel / a
                            print(f'A variação do tempo tempo é de {temp} s)')
                            inicio()


inicio()
