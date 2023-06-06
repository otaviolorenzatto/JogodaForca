import funcoes 
funcoes.limpaTela()
print('**Bem-vindo ao jogo da Forca**\n')
while True:
    desafiante=input('Digite o nome do desafiador: ')
    desafiado=input('Digite o nome do desafiado: ')
    funcoes.jogadores(desafiante, desafiado)
    funcoes.limpaTela()
    palavraChave=input('Digite a palavra chave: ')
    respostaDicas=['Dica 1: ', 'Dica 2: ', 'Dica 3: ']
    dicas=[]
    for r in range (len(respostaDicas)):
        print(respostaDicas[r])
        dicas.append(input())
    funcoes.limpaTela()
    print('A palavra é composta por', len(palavraChave),'letras')
    for r in range (len(palavraChave)):
        print(end='')
    erros= 0
    tentativas=[]
    acertos=[]
    vencedor=[]
    while True:
        print('Digite (1) para comerçar a jogar')
        print('Digite (2) para solicitar uma dica',)
        print('Erro: ', erros) 
        opcao=input()
        if opcao=='1':
            letra=input('Digite uam letra: ')
            if letra in tentativas:
                print('Letra já utilizada')
            elif letra not in palavraChave:
                print('Letra não pertence a palavra')
                tentativas.append(letra)
                erros+=1
                funcoes.desenhoforca(erros)
            else:
                print('Letra pertence a palavra')
                acertos.append(letra)
                palavra=''
                for letra in palavraChave:
                    if letra in acertos:
                        palavra+=letra
                    else:
                        palavra+='_'
                print(palavra)
                if palavra==palavraChave:
                    print('Você acertou!!!')
                    vencedor=desafiado
                    break
        elif opcao=='2':
            try:
                print(dicas[0])
                del dicas [0]
            except:
                print('Impossibiltado de pedir mais dicas!')
        else:
            print('Opção inválida')
        if erros >=5:
            print('Você perdeu!')
            break
    print('\n(1)Sair')
    print('(2)Jogar Novamente')
    opcao=input()
    if opcao=='1':
        break
    elif opcao=='2':
        pass
        funcoes.limpaTela()
    else:
        print('Opção inválida')
      
        

        

          

                

