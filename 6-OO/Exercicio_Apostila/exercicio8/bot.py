from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
from Biblioteca import Biblioteca
from Livro import Livro
from Autor import Autor
import datetime
import time



def main():

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()


    bot.browse(r"C:\Users\matutino\Documents\Zl-academy\6-OO\Exercicio_Apostila\exercicio8\emprestimo.html")

    autor1 = Autor("J.K. Rowling")
    livro1 = Livro("Harry Potter e a Pedra Filosofal", autor1, "001")
    
    autor2 = Autor("George Orwell")
    livro2 = Livro("1984", autor2, "002")
    
    biblioteca = Biblioteca("Biblioteca Central")
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    cliente_nome = "João Silva"
    livro_para_emprestimo = "001"  
    
    print("Preenchendo o formulário...") 
    bot.find_element("cod_livro", By.ID).send_keys(livro_para_emprestimo)
    time.sleep(1)
    bot.find_element("nome_cliente", By.ID).send_keys(cliente_nome)
    time.sleep(1)
    bot.find_element("livro_id", By.ID).send_keys(livro_para_emprestimo)
    time.sleep(1)
    bot.find_element("usuario_id", By.ID).send_keys("123") 
    time.sleep(1)

    data_emprestimo = datetime.date.today().strftime("%Y-%m-%d")
    data_devolucao = (datetime.date.today() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    
    bot.find_element("data_emprestimo", By.ID).send_keys(data_emprestimo)
    time.sleep(1)
    bot.find_element("data_devolucao", By.ID).send_keys(data_devolucao)
    time.sleep(1)

    print("Salvando os dados no arquivo...") 
    try:
        with open("emprestimo_dados.txt", "a", encoding="utf-8") as file:
            file.write(f"\nEmpréstimo registrado em {datetime.datetime.now()}\n")
            file.write(f"Código do Livro: {livro_para_emprestimo}\n")
            file.write(f"Nome do Cliente: {cliente_nome}\n")
            file.write(f"ID do Livro: {livro_para_emprestimo}\n")
            file.write(f"ID do Usuário: 123\n")
            file.write(f"Data de Empréstimo: {data_emprestimo}\n")
            file.write(f"Data de Devolução: {data_devolucao}\n")
            file.write(f"{'-'*40}\n") 
        print("Dados salvos com sucesso.") 
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}") 

    bot.wait(3000)
    bot.stop_browser()

if __name__ == '__main__':
    main()
