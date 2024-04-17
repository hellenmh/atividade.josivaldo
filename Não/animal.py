class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie
    def emitir(self):
        print("o animal", self.nome, "da especie", self.especie,"esta emetindo som")
    def informacao(self):
        print(f"o animal{self.nome}da especie {self.especie}tem {self.idade} anos de idade")
if __name__=="__main__":
    animal= Animal("fido", "5", "cachorro")
    animal.emitir()
    animal.informacao()

    