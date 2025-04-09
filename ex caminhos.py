print("Você acabou de chegar na floresta dos magos da programação, escolha o  caminho que deseja seguir")
caminhos = input("deseja ir pelo caminho da direita ou da esquerda?: ")
if caminhos == "direita":
    print("você chegou a uma montanha, deseja escalar?")
    montanha = input("sim ou não?: ")
    if montanha == "não":
        print("sua jornada termina por aqui,você MORREU! ")
    elif montanha == "sim":
        print("você subiu ao topo da montanha e ganhou o nobel de pessoa mais mita do planeta!")
elif caminhos == "esquerda":
    print("você chegou a um rio misterioso, deseja tentar atravessa-lo?")
    rio = input("sim ou não? ")
    if rio == "sim":
        print("você tentou nadar e MORREU para um jacaré")
    elif rio == ("não"):
        print("você desistiu e foi dormir!")
    else:
        print("insira uma resposta válida")