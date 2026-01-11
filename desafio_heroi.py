# ============= Boas vindas ==============
print(" Bem vindo ao RPG ".center(50, "="))

print('''
Vamos criar o seu personagem para que ele 
possa enfrentar os desafios desta jornada
''')

print("-" * 50)
# ----------------------------------------

# input nome, idade, tipo
nome = input("Entre com o nome do seu herói: ")
idade = int(input("Agora entre com a idade do seu herói: "))
print("Por último, informe qual será o tipo do seu herói")

while True:
    try:
        tipo = int(input('''1 - guerreiro
    2 - mago
    3 - monge
    4 - ninja
    >>> '''))
        if tipo >= 1 and tipo <=4:
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 4.")
    except ValueError:
        print("Erro: Digite apenas NÚMEROS (1, 2, 3 ou 4).")

# classe heroi
class heroi:
    def __init__(self, nome, idade, tipo_num):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        
        opcoes = {
            1: "guerreiro", 
            2: "mago", 
            3: "monge", 
            4: "ninja"}
        self.tipo = opcoes.get(tipo_num, " ")

    def ataque(self):
        ataques = {
            "guerreiro": "espada",
            "mago": "magia",
            "monge": "artes marciais",
            "ninja": "shuriken"
        }
        
        ataque = ataques.get(self.tipo, " ")

        print(f"O {self.tipo} atacou usando {ataque}")
        return ataque

novo_heroi = heroi(nome, idade, tipo)

print(" FICHA DO HERÓI ".center(50, "="))
print(f'''Nome: {novo_heroi.nome}
Idade: {novo_heroi.idade}
Tipo: {novo_heroi.tipo}
Tipo de ataque: {novo_heroi.ataque()}''')
print("-" * 50)

novo_heroi.ataque()