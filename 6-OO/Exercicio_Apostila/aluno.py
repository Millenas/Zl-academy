class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def mostrar_info(self):
        print(f"Nome: {self.nome}, Matrícula: {self.matricula}")


class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def mostrar_alunos(self):
        print(f"Alunos matriculados no curso {self.nome}:")
        for aluno in self.alunos:
            aluno.mostrar_info()


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        print(f"Cursos oferecidos pela escola {self.nome}:")
        for curso in self.cursos:
            print(f"Código: {curso.codigo}, Nome: {curso.nome}")
            curso.mostrar_alunos()


if __name__ == "__main__":

    aluno1 = Aluno("Alice", 101)
    aluno2 = Aluno("Bob", 102)
    aluno3 = Aluno("Charlie", 103)


    curso1 = Curso("Matemática", "MAT101")
    curso2 = Curso("Física", "FIS101")


    curso1.adicionar_aluno(aluno1)
    curso1.adicionar_aluno(aluno2)
    curso2.adicionar_aluno(aluno3)


    escola = Escola("Escola Primária")
    escola.adicionar_curso(curso1)
    escola.adicionar_curso(curso2)

    escola.mostrar_cursos()


"""
Respostas para as Perguntas de Reflexão
Como a composição facilita a criação de relações complexas entre objetos?

A composição permite que objetos sejam construídos a partir de outros objetos, formando relações mais complexas. Por exemplo, uma Escola contém vários Cursos, e cada Curso pode conter vários Alunos. Isso permite que cada classe tenha sua própria responsabilidade e facilite a manutenção do código.
Qual é a vantagem de usar composição em vez de herança neste exercício?

A composição é mais flexível do que a herança, pois permite que objetos de diferentes classes sejam combinados de várias maneiras, sem as limitações da hierarquia de classes. Isso significa que se precisarmos modificar ou adicionar novas funcionalidades, podemos fazê-lo sem afetar toda a estrutura do código.
Como o encapsulamento é utilizado nas classes Aluno, Curso e Escola?
O encapsulamento é utilizado ao definir atributos como privados e ao expor métodos para manipular esses atributos. No nosso exemplo, as classes têm atributos que são acessados e modificados apenas por meio de métodos específicos, como mostrar_info, adicionar_aluno e mostrar_cursos. Isso ajuda a proteger a integridade dos dados.

Como você pode estender este sistema para incluir novas funcionalidades, como notas dos alunos e professores para cada curso?
Para incluir notas dos alunos, poderíamos adicionar um atributo notas na classe Aluno e um método para calcular a média. Para incluir professores, poderíamos criar uma nova classe Professor e relacioná-la à classe Curso. Assim, cada curso poderia ter um professor responsável e cada aluno poderia ter suas notas registradas.
"""