'''
leia uma nota de um aluno, de 0 à 10 e mostre na tela o seu conceito. Considere:
nota >= 9,0 -> Excelente
>= 7,0 e < 9,0 -> Bom
>= 5,0 e < 7,0 -> Razoável
< 5,0 -> Fraco

'''
import numpy as np


class ConceitoAluno:
    def __init__(self):
        """
        Avalia o aluno conforme a nota inserida
        """
        self.nota = -1

    def set_nota(self):
        """
        Funcao para inserir a nota do aluno
        """
        while self.nota not in np.arange(0, 10, 0.1):
            print('Insira uma nota entre 0 a 10')
            self.nota = float(input('Qual a nota do aluno?\n'))
            if self.nota in np.arange(0, 10, 0.1):
                break

    def get_nota(self):
        """

        :return: Nota do aluno
        """
        return self.nota

    def conceituar(self):
        """
        Conceitua o aluno:
        nota >= 9,0 -> Excelente
        >= 7,0 e < 9,0 -> Bom
        >= 5,0 e < 7,0 -> Razoável
        < 5,0 -> Fraco

        :return: Retorna o conceito em formato str conforme nota
        """
        if self.nota >= 9:
            return 'Exelente'
        elif 7 <= self.nota < 9:
            return 'Bom'
        elif 5 <= self.nota < 7:
            return 'Razoável'
        else:
            return 'Fraco'


a = ConceitoAluno()
a.set_nota()
print(a.conceituar())

