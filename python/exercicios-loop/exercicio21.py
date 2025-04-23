class Cliente:
    def __init__(self, num_cli:int, nome:str, morada:str, telemovel:str, nif:str, compra:int):
        desconto = 0.0
        
        self.num_cli = num_cli
        self.nome = nome
        self.morada = morada,
        self.telemovel = telemovel
        self.nif = nif
        self.compra = compra

        if self.compra >= 100 and self.compra <= 200:
            desconto = 0.05
        elif self.compra >= 200 and self.compra < 500:
            desconto = 0.10
        else:
            desconto = 0.15

        self.divida_final = self.compra - self.compra * desconto
    def __repr__(self):
        return f"Cliente(número cliente = {self.num_cli}, nome = \"{self.nome}\", morada = \"{self.morada}\", telemovel = \"{self.telemovel}\", nif = \"{self.nif}\", compra = {self.compra:.2f}, divida final = {self.divida_final:.2f})"
def encontrar_cliente(id):
    for cliente in clientes:
        if cliente.num_cli == id:
            return cliente
    return None
clientes = [
    Cliente(0, "Diogo Costa", "Rua Primeiro de Maio", "111111111", "111111111", 45.60),
    Cliente(1, "Afonso Batista", "Rua Segundo de Maio", "222222222", "222222222", 106.99)
]

for cliente in clientes:
    id = 0
    encontrado = None

    print(cliente)
    if input("Deseja procurar um cliente por id? S ou N: ") == 'N':
        continue
    id = int(input("Introduze a id: "))
    encontrado = encontrar_cliente(id)
    if encontrado != None:
        print(f"Cliente encontrado {encontrado}")
    else:
        print("Cliente encontrado não encontrado")
