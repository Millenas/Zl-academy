from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass


    def dormir(self):
        print("Este animal está dormindo.")


class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro late.")

class Gato(Animal):
    def fazer_som(self):
        print("O gato mia.")



cachorro = Cachorro()
gato = Gato()


cachorro.fazer_som()
gato.fazer_som()


cachorro.dormir()
gato.dormir()