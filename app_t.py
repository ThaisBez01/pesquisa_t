#Lista
cidades = ["Sobradinho", "Gurupi", "Jardim Botânico", "Sobradinho", "Plano Piloto", "Samambaia Sul", "Gurupi", 
           "São Paulo", "Recife", "Rio De Janeiro", "Gurupi", "Taguatinga", "Planaltina", "Sobradinho"]

#Usuário informa o nome que deseja procurar
cidade = input("Informe o nome da cidade que deseja procurar: ")

#Informa a quantidade de vezes que o termo foi achado
quantidade= cidades.count(cidade)

#Exibe o resultado na tela
if cidade in cidades: 
    print(f"{cidade} foi encontrado na lista {quantidade} vezes.")
else:
    print(f"{cidade} não foi encontrado.")