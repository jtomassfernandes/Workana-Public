# Programa de IMC, mas mais elaborado :)
# depois a ser transportado/traduzido para C em inglês :) :) :)
# 
# Formula para IMC
# (IMC (kg/m2) = peso (kg)/altura2(m))
# atenção as unidades usadas
# 
# https://www.sns24.gov.pt/tema/doencas-cronicas/obesidade/
# https://www.adexo.pt/images/imc/TabelaCalculoIMC.jpg
# https://www.adexo.pt/tratamento/imc
# https://bvsms.saude.gov.br/bvs/dicas/215_obesidade.html

import sys
opcao = ""

print("/////////////////////////////////////////////////////////////////////////////////")    
print("/////////////////////////////////////////////////////////////////////////////////")
print("Programa de Calculo de Índice de Massa Corporal")
print()
input("\n--------------------Pressiona ENTER para continuar...-------------------- \n")

print("Para calcular o IMC de acordo com a tabela de IMC é necessário ter dois fatores em conta: ")
print("\n          Altura \n          Peso \n")
input("\n--------------------Pressiona ENTER para continuar...-------------------- \n")
print("As informações que aqui inserires vão ser automaticamente destruídas quando o programa terminar.")
input("\n--------------------Pressiona ENTER para continuar...-------------------- \n")
print("/////////////////////////////////////////////////////////////////////////////////")
print("/////////////////////////////////////////////////////////////////////////////////")
print()
print("Comecemos!")

while not(opcao == "sair" or opcao == "SAIR" or opcao == "exit" or opcao == "EXIT"):
    # inputs
    print("Qual é o teu nome? ")
    nome = str(input())
    if nome == "sair" or nome == "SAIR" or nome == "exit" or nome == "EXIT":
        sys.exit()

    print()
    print(nome + ", qual é o teu peso? \n (Usa ponto '.' para separar os quilos (kg) do restante)")
    peso = float(input())
    while peso <= 0:
        print("Peso invalido!")
        peso = float(input("Qual é o teu peso?"))
        continue

    print()
    print("E qual é a tua altura? \n(Em metros. Usa ponto '.' para separar os metros (m) do restante)")
    altura = float(input())
    while not altura >= 0.5 :
        print("Altura inválida. Programa irá considerar como válido uma altura igual ou superior a 0.5 m (meio metro)")
        altura = float(input("Qual é a tua altura?"))
        if altura == str("sair") or altura == str("SAIR") or altura == str("exit") or altura == str("EXIT"):
            sys.exit()
        continue

    print()
    print("/////////////////////////////////////////////////////////////////////////////////")
    print("/////////////////////////////////////////////////////////////////////////////////")
    print("/////////////////////////////////////////////////////////////////////////////////")
    print("/////////////////////////////////////////////////////////////////////////////////")
    print()
    print()

    IMC = round(peso / (altura*altura),2)

    if IMC <= 18.5:
        print("Estás em 'Baixo Peso', " + nome + ". Tem atenção ao teu peso...\n")
        print("Peso: ", peso)
        print("Altura: ", altura)
        print("O teu IMC é:", IMC)
        
    elif IMC > 18.5 and IMC < 24.9:
        print("Estás em 'Peso Normal', " + nome + ". Continua assim!\n")
        print("Peso: ", peso)
        print("Altura: ", altura)
        print("O teu IMC é:", IMC)

    elif IMC >= 25 and IMC < 29.9:
        print("Estás com 'Excesso de Peso', " + nome +". Tem atenção ao teu peso...\n")
        print("Peso: ", peso)
        print("Altura: ", altura)
        print("O teu IMC é:", IMC)
    elif IMC > 30:
        if IMC > 30 and IMC < 34.9:
            print(nome + ". Estás em 'Obesidade Classe 1'. Vai com uma nutricionista com relativa urgência e tenta ser humilde com a tua própria situação.\n")
            print("Peso: ", peso)
            print("Altura: ", altura)
            print("O teu IMC é:", IMC)
            print("https://www.sns24.gov.pt/tema/doencas-cronicas/obesidade/")
            
        elif IMC > 35 and IMC < 39.9:
            print(nome + ". Estás em 'Obesidade Classe 2'. Vai com uma nutricionista sê humilde com a tua própria situação. \n")
            print("Peso: ", peso)
            print("Altura: ", altura)
            print("O teu IMC é:", IMC)
            print("https://www.sns24.gov.pt/tema/doencas-cronicas/obesidade/")
        elif IMC > 40 :
            print(nome + ". Estás em 'Obesidade Classe 3'. Vai com um médico e com uma nutricionista! Não evites nenhum, mesmo que um deles ache que não precises do outro.")
            print("Sê humilde contigo mesmo e reconhece a tua situação. Não penses que estás bem, só pelo facto de estares confortável. \n")
            print("Peso: ", peso)
            print("Altura: ", altura)
            print("O teu IMC é:", IMC)
            print("https://www.sns24.gov.pt/tema/doencas-cronicas/obesidade/")

    print("\n\nObrigado por utilizares o programa, ", nome, ". E boa sorte na tua jornada de saúde!!\n\n")
    print("/////////////////////////////////////////////////////////////////////////////////")
    print("/////////////////////////////////////////////////////////////////////////////////")
    print("/////////////////////////////////////////////////////////////////////////////////")
    print("/////////////////////////////////////////////////////////////////////////////////")

    opcao = str(input("Para sair escreve 'sair' ou 'exit'. Para voltar ao inicio do programa pressiona ENTER: "))
    print("/////////////////////////////////////////////////////////////////////////////////")
    print("/////////////////////////////////////////////////////////////////////////////////")
    print()
    continue
    