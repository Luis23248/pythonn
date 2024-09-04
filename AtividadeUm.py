import os

os.system("cls || clean")


class pet:
    def __init__(self, nome: str, idade: int, raca: str, porte: str, alimentacao: str) -> None:
        self.nome = nome
        self.idade = idade 
        self.raca = raca 
        self.porte = porte
        self.alimentacao = alimentacao 

    
    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nRaça: {self.raca} \nPorte: {self.porte} \nAlimentação: {self.alimentacao}"
    
pet = pet (nome = "Cachorro", idade = 3, raca = "Pit Bull", porte = "Pequeno", alimentacao = "Ração" )

print(pet.exibir_dados())    