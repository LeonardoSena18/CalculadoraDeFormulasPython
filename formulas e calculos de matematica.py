from time import sleep
sleep(1)
opcao = int(input('=-=-=-=-=-=-=-=-=-Menu=-=-=-=-=-=-=-=-=-\n'
                  '[1] Álgebra 1 \n'
                   '[2] Geometria plana\n'
                   '[3] Trigonometria\n'
                   '[4] Álgebra 2\n'
                   '[5] Estatística e matemática financeira\n'
                   '[6] Geometria espacial\n'
                   '[7] Geometria analítica\n'
                   '[8] Álgebra 3\n'
                   '[0] Sair\n'
                   'Digite a opção: '))
while opcao != 0:
    if opcao == 1:
        sleep (1)
        formulas1 = int(input('\n'
                              '=-=-=-=-=-=-=-=-Álgebra 1=-=-=-=-=-=-=-=-\n'
                              '[1] Fórmula da resolução da equação do segundo grau\n'
                              '[2] Fórmula da progressão aritmética\n'
                              '[3] Fórmula da soma dos termos de uma P.A.\n'
                              '[4] Fórmula da progressão geométrica\n'
                              '[5] Para voltar ao menu inicial\n'
                              'Digite a opção: '))
        if formulas1 == 1:
            sleep(1)
            print('\n'
                  '=-=-=-=-=-=-=-=-Fórmula de Braska=-=-=-=-=-=-=-=-\n'
                  '            __________\n'
                  '     -b + \/(b² - 4ac)\n'
                  'x¹ = ___________________\n'
                  '             2a               \n'
                  '            __________\n'
                  '     -b - \/(b² - 4ac)\n'
                  'x² = ___________________\n'
                  '              2a            ')
            calcfor1 = int(input('\n'
                                 '=-=-=-=-=-=-=-=-=-=-mais opções=-=-=-=-=-=-=-=-=-=-\n'
                                 '[1] Calcular\n'
                                 '[2] Voltar\n'
                                 'Digite a opção: '))
            if calcfor1 == 1:
                sleep(1)
                print('\n')
                print('=' * 22)
                print('Calculadora de Bhraska')
                print('=' * 22)
                a = float(input('Informe o valor de A: '))
                b = float(input('Informe o valor de B: '))
                c = float(input('Informe o valor de C: '))
                delta = (b ** 2) - 4 * a * c
                if delta < 0:
                    print('Delta vale {}'.format(delta))
                    print('Não existe valores reais de x para delta negativo. ')
                else:
                    x1 = ((-b) + (delta ** (1 / 2))) / (2 * a)
                    x2 = ((-b) - (delta ** (1 / 2))) / (2 * a)
                    print('O valor de delta é igual a {}'.format(delta))
                    print('O primeiro valor de x vale {}'.format(x1))
                    print('E o segundo valor de x vale {}'.format(x2))
            elif calcfor1 == 2:
                sleep(1)
                print('>' * 50)
            else:
                print('\n'
                      'OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n'
                      '\n')
                sleep(1)
                calcfor1 = int(input('\n'
                                 '=-=-=-=-=-=-=-=-=-=-mais opções=-=-=-=-=-=-=-=-=-=-\n'
                                 '[1] Calcular\n'
                                 '[2] Voltar\n'
                                 'Digite a opção: '))
        elif formulas1 == 2:
            sleep(1)
            print('\n'
                  '=-=-=-=-=-=-=-=-=-=-P.A.=-=-=-=-=-=-=-=-=-=-\n'
                  'an = a1 + (n - 1)r\n'
                  'sendo:\n'
                  'a1: primeiro termo\n'
                  'an: ultimo termo\n'
                  'n: o número de termos\n'
                  'r: a razão')
            calcfor2 = int(input('\n'
                                  '=-=-=-=-=-=-=-=-=-=-mais opções=-=-=-=-=-=-=-=-=-=-\n'
                                  '[1] Calcular\n'
                                  '[2] Voltar  \n'
                                  'Digite a opção: '))
            if calcfor2 == 1:
                print('\n')
                print('=' * 20)
                print('Progressão Aritmética')
                print('=' * 20)
                apri = int(input('Informe o primeiro termo: '))
                raz = int(input('Informe a razão termo: '))
                num = int(input('Informe o número de termos: '))
                ault = apri + (num - 1) * raz
                print('O último termo é igual a {}'.format(ault))
            elif calcfor2 == 2:
                sleep(1)
                formulas1 = int(input('\n'
                                      '=-=-=-=-=-=-=-=-Álgebra 1=-=-=-=-=-=-=-=-\n'
                                      '[1] Fórmula da resolução da equação do segundo grau\n'
                                      '[2] Fórmula da progressão aritmética\n'
                                      '[3] Fórmula da soma dos termos de uma P.A.\n'
                                      '[4] Fórmula da progressão geométrica\n'
                                      '[5] Para voltar ao menu inicial\n'
                                      'Digite a opção: '))
            else:
                sleep(1)
                print('\n'
                      'OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n'
                      '\n')
                sleep(1)
                calcfor2 = int(input('\n'
                                 '=-=-=-=-=-=-=-=-=-=-mais opções=-=-=-=-=-=-=-=-=-=-\n'
                                 '[1] Calcular\n'
                                 '[2] Voltar\n'
                                 'Digite a opção: '))
        elif formulas1 == 3:
            print('\n')
            print('=-=-=-=-=-=-=-=-=-=-soma do número de termos=-=-=-=-=-=-=-=-=-=-'
                  '       (a1 + an)r\n'
                  'Sn = _______________\n'
                  '            2       '
                  'sendo:\n'
                  'a1: primeiro termo\n'
                  'an: ultimo termo\n'
                  'n: o número de termos\n'
                  'r: a razão\n'
                  'Sn: o total da soma dos termos')
            calcfor3 = int(input('\n'
                                 '=-=-=-=-=-=-=-=-=-=-mais opções=-=-=-=-=-=-=-=-=-=-\n'
                                 '[1] Calcular\n'
                                 '[2] Voltar\n'
                                 'Digite a opção: '))
            if calcfor3 == 1:
                print('\n')
                print('=' * 30)
                print('Soma dos termos de uma P.A.')
                print('=' * 30)
                primeiroterm = int(input('Informe o primeiro termo: '))
                ultimoterm = int(input('Informe o último termo: '))
                razao = int(input('Informe a razão: '))
                sn = ((primeiroterm + ultimoterm) * razao) / 2
                print('A soma dos {} termos dessa P.A. é igual a {}'.format(ultimoterm, sn))
            elif calcfor3 == 2:
                formulas1 = int(input('\n'
                                      '=-=-=-=-=-=-=-=-Álgebra 1=-=-=-=-=-=-=-=-\n'
                                      '[1] Fórmula da resolução da equação do segundo grau\n'
                                      '[2] Fórmula da progressão aritmética\n'
                                      '[3] Fórmula da soma dos termos de uma P.A.\n'
                                      '[4] Fórmula da progressão geométrica\n'
                                      '[5] Para voltar ao menu inicial\n'
                                      'Digite a opção: '))
            else:
                print('\n'
                      'OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n'
                      '\n')
                sleep(1)
                calcfor3 = int(input('\n'
                                 '=-=-=-=-=-=-=-=-=-=-mais opções=-=-=-=-=-=-=-=-=-=-\n'
                                 '[1] Calcular\n'
                                 '[2] Voltar\n'
                                 'Digite a opção: '))
        elif formulas1 == 4:
            print('\n')
            print('=-=-=-=-=-=-=-=-=-=-P.G.=-=-=-=-=-=-=-=-=-=-'
                  '            n-1  \n'
                  'an = a1 * q      \n'
                  'sendo:'
                  'an: último termo\n'
                  'a1: primeiro termo\n'
                  'n: número de termos\n'
                  'q: a razão da P.G')
            calcfor4 = int(input('\n'
                                 '=-=-=-=-=-=-=-=-=-=-mais opções=-=-=-=-=-=-=-=-=-=-\n'
                                 '[1] Calcular\n'
                                 '[2] Voltar\n'
                                 'Digite a opção: '))
            if calcfor4 == 1:
                print('\n')
                print('=' * 30)
                print('Soma dos termos de uma P.A.')
                print('=' * 30)
                primeiroterm = int(input('Informe o primeiro termo: '))
                ultimoterm = int(input('Informe o último termo: '))
                razao = int(input('Informe a razão: '))
                sn = ((primeiroterm + ultimoterm) * razao) / 2
                print('A soma dos {} termos dessa P.A. é igual a {}'.format(ultimoterm, sn))
            elif calcfor4 == 2:
                sleep(1)
                formulas1 = int(input('\n'
                                      '=-=-=-=-=-=-=-=-Álgebra 1=-=-=-=-=-=-=-=-\n'
                                      '[1] Fórmula da resolução da equação do segundo grau\n'
                                      '[2] Fórmula da progressão aritmética\n'
                                      '[3] Fórmula da soma dos termos de uma P.A.\n'
                                      '[4] Fórmula da progressão geométrica\n'
                                      '[5] Para voltar ao menu inicial\n'
                                      'Digite a opção: '))
            else:
                print('\n'
                      'OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n'
                      '\n')
                sleep(1)
                calcfor3 = int(input('\n'
                                     '=-=-=-=-=-=-=-=-=-=-mais opções=-=-=-=-=-=-=-=-=-=-\n'
                                     '[1] Calcular\n'
                                     '[2] Voltar\n'
                                     'Digite a opção: '))
        elif formulas1 == 5:
            print('\n')
            opcao = int(input('=-=-=-=-=-=-=-=-=-Menu=-=-=-=-=-=-=-=-=-\n'
                              '[1] Álgebra 1 \n'
                              '[2] Geometria plana\n'
                              '[3] Trigonometria\n'
                              '[4] Álgebra 2\n'
                              '[5] Estatística e matemática financeira\n'
                              '[6] Geometria espacial\n'
                              '[7] Geometria analítica\n'
                              '[8] Álgebra 3\n'
                              '[0] Sair\n'
                              'Digite a opção: '))
        else:
            print('\n'
                  '=' * 20)
            print('Opção inválida, tente novamente. ')
            print('=' * 20)
            formulas1 = int(input('=-=-=-=-=-=-=-=-Álgebra 1=-=-=-=-=-=-=-=-\n'
                                  '[1] Fórmula da resolução da equação do segundo grau\n'
                                  '[2] Fórmula da progressão aritmética\n'
                                  '[3] Fórmula da soma dos termos de uma P.A.\n'
                                  '[4] Fórmula da progressão geométrica\n'
                                  '[5] Para voltar ao menu inicial\n'
                                  'Digite a opção: '))

    elif opcao == 2:
        formulas2 = int(input(''))
    elif opcao == 3:
        formulas3 = int(input(''))
    elif opcao == 4:
        formulas4 = int(input(''))
    elif opcao == 5:
        formulas5 = int(input(''))
    elif opcao == 6:
        formulas6 = int(input(''))
    elif opcao == 7:
        formulas7 = int(input(''))
    elif opcao == 8:
        formulas8 = int(input(''))
    else:
        sleep(1)
        opcao = int(input('\n'
                          '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
                          'Opcão inválida, tente novamente\n'
                          '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
                          '[1] Álgebra 1 \n'
                          '[2] Geometria plana\n'
                          '[3] Trigonometria\n'
                          '[4] Álgebra 2\n'
                          '[5] Estatística e matemática financeira\n'
                          '[6] Geometria espacial\n'
                          '[7] Geometria analítica\n'
                          '[8] Álgebra 3\n'
                          '[0] Sair\n'
                          'Digite a opção: '))
print('Finalizando...')
sleep(2)
print('Programa cancelado pelo usuário. ')
#começar na linha 236 na area da geometria plana
