#Autor: Julia Gonçalves Oliveira
#Componente Curricular: MI Algoritmos 
#Concluido em: 21/04/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.


meia_entrada = 0 
m_e_estudante = 0
m_e_idoso = 0
entrada_inteira = 0
entrada_ecomp = 0
cortesia_DACon = 0
ingressos_emitidos = 0
mediaidade = 0
dinheiro = 0 #dinheiro arrecadado em total
dinheiro_int = 0 #dinheiro arrecadado com as inteiras
dinheiro_mei = 0 #dinheiro arrecadado com as meia entradas
dinheiro_ecomp = 0 #dinheiro arrecadado com as entradas ecomp
cort_curs1 = 0 #cortesias do curso 1
cort_curs2 = 0 #cortesias do curso 2
ing_curs1 = 0 #ingressos vendidos pelo curso 1
ing_curs2 = 0 #ingressos vendidos pelo curso 2
enc_venda = 1 #variável usada para encerrar o código


print('\nConfigurações\n') #Configurações iniciais 
num_ingressos = int(input('\tQuantos ingressos serão vendidos? '))
valor_inteira = int(input('\tQual o valor da inteira? '))
valor_meia = valor_inteira//2
valor_ecomp = int(input('\tQual o valor para EComp? '))
curso1 = input('\tQual o primeiro curso comissionado? ')
curso2 = input('\tQual o segundo curso comissionado? ')


while ingressos_emitidos < num_ingressos and enc_venda > 0:
  print(f'\nIngressos disponíveis: {num_ingressos-ingressos_emitidos}')

  pergunta05 = input(f"\nEscolha uma das opções:\n \n\t[1] Vendedor de {curso1}. \n\t[2] Vendedor de {curso2}. \n\t[3] Vendedor de EComp. \nDigite sua resposta: ")
  if pergunta05 == ' ' or not pergunta05 in ['1','2','3','4']:
          print('Por favor faça uma escolha válida.')

  if pergunta05 == '1':
      ing_curs1 += 1
      #Verificação para que o número de cortesias do curso 1 não exceda o número total de ingressos.
      if ing_curs1 % 10 == 0 and ingressos_emitidos < num_ingressos - 1: 
        cort_curs1 += 1
        ingressos_emitidos += 1
      elif ingressos_emitidos >= num_ingressos - 1:
        print ('Número de cortesias para cursos comissionados chegou ao limite.')

  elif pergunta05 == '2':
      ing_curs2 += 1
      #Mesma verificação que o curso 1.
      if ing_curs2 % 10 == 0 and ingressos_emitidos < num_ingressos - 1: 
          cort_curs2 += 1
          ingressos_emitidos += 1
      elif ingressos_emitidos >= num_ingressos - 1:
        print ('Número de cortesias para cursos comissionados chegou ao limite.')

  #Verificação de idade e nome do comprador
  idade = int(input('\nIdade do Comprador: '))
  if idade == ' ' or not int:
     print('Digite uma idade válida.') 
  mediaidade += idade
  nome = (input('Nome do Comprador: '))

  #Escolha de tipo de ingresso e atualização das variáveis acumuladoras
  pergunta1 = str(input(f'\nEscolha seu tipo de ingresso:\n \n\t[1] Inteira - {valor_inteira} reais.  \n\t[2] Meia - {valor_meia} reais. \n\t[3] EComp - {valor_ecomp} reais. \n\t[4] DA/Convidados  \nDigite sua resposta: '))
  if pergunta1 == ' ' or not pergunta1 in ['1','2','3','4']:
            print('Por favor faça uma escolha válida.')
    
  elif pergunta1 == '1':
      print(f'\nSeu ingresso custará {valor_inteira} reais.')
      ingressos_emitidos += 1
      dinheiro_int += valor_inteira
      entrada_inteira += 1


  elif pergunta1 == '2':
    meia_entrada += 1
    ingressos_emitidos += 1
    dinheiro_mei += valor_meia
    #Verificação entre os tipos de meia-entrada
    comp = input("\n[1] Meia-entrada para estudante.\n[2] Meia-entrada para idosos.\nDigite sua resposta: ")
    if comp == ' ' or not comp in ['1','2']:
        print('Por favor faça uma escolha válida.')
    elif comp == '1':
      m_e_estudante += 1
    elif comp == '2':
      m_e_idoso +=1
    print(f'\nSeu ingresso custará {valor_meia} reais')
  
  elif pergunta1 == '3':
      print(f'\nSeu ingresso custará {valor_ecomp} reais')
      ingressos_emitidos += 1
      dinheiro_ecomp += valor_ecomp
      entrada_ecomp += 1
    
  elif pergunta1 == '4':
      print('\nSeu ingresso não custará nada')
      ingressos_emitidos += 1
      cortesia_DACon += 1
      #Retificação caso aja escolha de vendedor, pois cortesias de DA/Convidados não são vendidas
      if pergunta05 == '1':
        print(f'Sua escolha de vendedor não será computada por ser um ingresso cortesia.')
        ing_curs1 -= 1
      elif pergunta05 == '2':
        ing_curs2 -= 1
        print(f'Sua escolha de vendedor não será computada por ser um ingresso cortesia.')
      
  encerrar = input ("\nDeseja encerrar as vendas? \nSim [1] ou Não [2]: ")
  if encerrar == '1':
    enc_venda -= 1
  
# Verificação de ingresso mais vendido
if entrada_inteira > entrada_ecomp and entrada_inteira > meia_entrada:
  print(f'\nO ingresso mais vendido foi de inteiras com {entrada_inteira} ingresso(s).')
elif meia_entrada > entrada_inteira and meia_entrada > entrada_ecomp:
  print(f'\nO ingresso mais vendido foi de meia-entradas com {meia_entrada} ingresso(s).')
elif entrada_ecomp > entrada_inteira and entrada_ecomp > meia_entrada:
  print(f'\nO ingresso mais vendido foi de EComp com {entrada_ecomp} ingresso(s).')

#Verificação de empates entre vendas de ingresso
if meia_entrada == entrada_inteira and meia_entrada + entrada_inteira > entrada_ecomp:
   print('\nHouve empate dos ingressos mais vendidos entre as entradas inteiras e meia-entradas.') 
elif entrada_inteira == entrada_ecomp and entrada_inteira + entrada_ecomp > meia_entrada:
   print('\nHouve empate dos ingressos mais vendidos entre as entradas inteiras e entradas EComp.')
elif entrada_ecomp == meia_entrada and entrada_ecomp + meia_entrada > entrada_inteira:
   print('\nHouve empate dos ingressos mais vendidos entre as meia-entradas e entradas EComp.')
elif entrada_ecomp == meia_entrada and meia_entrada == entrada_inteira:
   print('\nHouve empate entre todos os tipos de ingresso.')

#Informações finais
print (f"Ingressos emitidos: {ingressos_emitidos} \nIngressos não emitidos:{ num_ingressos-ingressos_emitidos}")
print (f'A média de idade dos compradores é de:{mediaidade/ingressos_emitidos:.1f}')
print (f"O total de dinheiro arrecadado foi de: {dinheiro_int + dinheiro_mei + dinheiro_ecomp}")
print (f"O total de inteiras é: {entrada_inteira} \nO total de entradas EComp foi de: {entrada_ecomp}")
print (f'O total de meia entradas foi de: {meia_entrada} \n\tMeia-entradas para estudantes foi: {m_e_estudante} \n\tMeia entrada para idosos: {m_e_idoso}')
print ('A quantidade de cortesias para DA e convidados foi de:', cortesia_DACon)
print (f'O total de ingressos vendidos por {curso1} é de: {ing_curs1}\nO total de ingressos vendidos por {curso2} é de: {ing_curs2}')
print (f'Cortesias de {curso1}: {cort_curs1}\nCortesias de {curso2}: {cort_curs2}')
quit()