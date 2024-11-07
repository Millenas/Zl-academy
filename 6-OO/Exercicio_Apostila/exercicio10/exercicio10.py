from botcity.web import WebBot, By, Browser
from webdriver_manager.chrome import ChromeDriverManager

# Define a classe base para os bots
class BotBase:
    def preencher_formulario(self, bot: WebBot):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

    def salvar_dados(self, dados: dict, arquivo: str):
        with open(arquivo, "a", encoding="utf-8") as file:
            for campo, valor in dados.items():
                file.write(f"{campo}: {valor}\n")
            file.write("\n")  

class BotCadastro(BotBase):
    def preencher_formulario(self, bot: WebBot):
        dados = {
            "nome": "João da Silva",
            "email": "joao@example.com",
            "senha": "senha123",
            "confirmar_senha": "senha123"
        }
        bot.find_element("nome", By.ID).send_keys(dados["nome"])
        bot.wait(500)
        bot.find_element("email", By.ID).send_keys(dados["email"])
        bot.wait(500)
        bot.find_element("senha", By.ID).send_keys(dados["senha"])
        bot.wait(500)
        bot.find_element("confirmar_senha", By.ID).send_keys(dados["confirmar_senha"])
        bot.wait(500)
        bot.find_element("submit", By.ID).click()
        bot.wait(500)
        self.salvar_dados(dados, "dados_formulario.txt")

class BotAtualizacao(BotBase):
    def preencher_formulario(self, bot: WebBot):
        dados = {
            "novo_nome": "João da Silva Atualizado",
            "novo_email": "joaoatualizado@example.com"
        }
        bot.find_element("novo_nome", By.ID).send_keys(dados["novo_nome"])
        bot.wait(500)
        bot.find_element("novo_email", By.ID).send_keys(dados["novo_email"])
        bot.wait(500)
        bot.find_element("submit_atualizacao", By.ID).click()
        bot.wait(500)
        self.salvar_dados(dados, "dados_formulario.txt")

def processar_bot(bot: BotBase, web_bot: WebBot):
    bot.preencher_formulario(web_bot)

def main():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    bot.browse(r"C:\Users\matutino\Documents\Zl-academy\6-OO\Exercicio_Apostila\exercicio10\formulariocadastro.html")  
    bot_cadastro = BotCadastro()
    processar_bot(bot_cadastro, bot)  
    bot.wait(3000)  

    bot.browse(r"C:\Users\matutino\Documents\Zl-academy\6-OO\Exercicio_Apostila\exercicio10\formularioatualizacao.html")
    bot_atualizacao = BotAtualizacao()
    processar_bot(bot_atualizacao, bot)  
    bot.wait(3000)  
    bot.stop_browser()

if __name__ == '__main__':
    main()
