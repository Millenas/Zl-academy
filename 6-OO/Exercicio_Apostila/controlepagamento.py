from abc import ABC, abstractmethod

class Pagamento(ABC):
    
    @abstractmethod
    def processar_pagamento(self):
        pass
    
    def detalhes_pagamento(self):
        print(f"Processando pagamento via {self.__class__.__name__}")


class PagamentoCartao(Pagamento):
    
    def processar_pagamento(self):
        print("Pagamento processado com cartão.")


class PagamentoBoleto(Pagamento):
    
    def processar_pagamento(self):
        print("Pagamento processado com boleto.")


def testar_pagamentos():

    cartao = PagamentoCartao()
    boleto = PagamentoBoleto()
    

    cartao.detalhes_pagamento()
    cartao.processar_pagamento()
    

    boleto.detalhes_pagamento()
    boleto.processar_pagamento()


if __name__ == "__main__":
    testar_pagamentos()
