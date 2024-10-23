
# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    ##bot.browse("http://www.botcity.dev")

    # Implement here your logic...
    bot.execute(r'C:\Users\matutino\Documents\Zl-academy\6-OO\Exercicio_Apostila\exercicio6\dist\veiculo.exe')
    

    if not bot.find("nomeVeiculo", matching=0.97, waiting_time=10000):
        not_found("nomeVeiculo")
    bot.click_relative(66, 40)
    bot.paste("Fusca")

    if not bot.find("AnoVeiculo", matching=0.97, waiting_time=10000):
        not_found("AnoVeiculo")
    bot.click_relative(68, 47)
    bot.paste("1972")

    if not bot.find("valorDiaria", matching=0.97, waiting_time=10000):
        not_found("valorDiaria")
    bot.click_relative(49, 46)
    bot.paste("100")

    #Obs: tipocombustivel
    if not bot.find("tipoVeiculo", matching=0.97, waiting_time=10000):
        not_found("tipoVeiculo")
    bot.click_relative(127, 52)

    #para o tipo etanol
    if not bot.find("etanol", matching=0.97, waiting_time=10000):
        not_found("etanol")
    bot.click()

    if not bot.find("cilindrada", matching=0.97, waiting_time=10000):
        not_found("cilindrada")
    bot.click_relative(48, 51)
    bot.paste("250")

    if not bot.find("qtdDiarias", matching=0.97, waiting_time=10000):
        not_found("qtdDiarias")
    bot.click_relative(62, 41)
    bot.paste("8")

    if not bot.find("btn-calcular", matching=0.97, waiting_time=10000):
        not_found("btn-calcular")
    bot.click()

    if not bot.find("alertCalculoOk", matching=0.97, waiting_time=10000):
        not_found("alertCalculoOk")
    bot.click()

    if not bot.find("btn-add", matching=0.97, waiting_time=10000):
        not_found("btn-add")
    bot.click()

    if not bot.find("alertaddOk", matching=0.97, waiting_time=10000):
        not_found("alertaddOk")
    bot.click()
    

    if not bot.find("btn-sair", matching=0.97, waiting_time=10000):
        not_found("btn-sair")
    bot.click()
    
  

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )



def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
