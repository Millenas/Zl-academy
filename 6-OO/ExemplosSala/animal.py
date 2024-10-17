class Animal:
    def fazer_soma(self):
        print("o animal faz um som")

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro late")

animal = Animal()
cachorro = Cachorro()

animal.fazer_soma()
cachorro.fazer_soma()