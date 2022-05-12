from time import sleep
glossário={'Input':'aguarda o desenvolvedor digitar algo (valor) com uma sequência de caracteres','If':' para executar em caso de a condição testada ser verdadeira','Else':' para executar em caso de a condição testada ser falsa.',
           'Range':'cria uma linha sequencial de números','Int':'converte um objeto em número inteiro'}
for i in glossário:
    sleep(1)
    print('\n-----------------------------------------------------------------------------------')
    print(f'{i} é {glossário[i]}')