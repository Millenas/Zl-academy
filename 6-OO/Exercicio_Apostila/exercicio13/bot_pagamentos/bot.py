# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
import subprocess
import time

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

    # Execute operations with the DesktopBot as desired
    # desktop_bot.control_a()
    # desktop_bot.control_c()
    # value = desktop_bot.get_clipboard()

    #webbot = WebBot()

    # Configure whether or not to run on headless mode
    #webbot.headless = False

    # Uncomment to change the default Browser to Firefox
    # webbot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    # webbot.driver_path = "<path to your WebDriver binary>"

    # Opens the BotCity website.
    #webbot.browse("https://www.botcity.dev")

    # Implement here your logic...
    bot.execute(r'C:\Users\matutino\Documents\Zl-academy\6-OO\Exercicio_Apostila\exercicio13\dist\sistemapagamentos.exe')

    if not bot.find("nomefuncionario", matching=0.97, waiting_time=10000):
        not_found("nomefuncionario")
    bot.click_relative(132, 16)
    bot.paste("Millena Sangela")
    
    if not bot.find("matriculafun", matching=0.97, waiting_time=10000):
        not_found("matriculafun")
    bot.click_relative(143, 11)
    bot.paste("25752")

    if not bot.find("tipohorista", matching=0.97, waiting_time=10000):
        not_found("tipohorista")
    bot.click()

    if not bot.find("hrstrabalho", matching=0.97, waiting_time=10000):
        not_found("hrstrabalho")
    bot.click_relative(168, 10)
    bot.paste("160")

    if not bot.find("valorhora", matching=0.97, waiting_time=10000):
        not_found("valorhora")
    bot.click_relative(153, 15)
    bot.paste("26")

    if not bot.find("btn-cadastrar", matching=0.97, waiting_time=10000):
        not_found("btn-cadastrar")
    bot.click()
    
    if not bot.find("alert-ok", matching=0.97, waiting_time=10000):
        not_found("alert-ok")
    bot.click()
    

    if not bot.find("btn_sair", matching=0.97, waiting_time=10000):
        not_found("btn_sair")
    bot.click()

        
    
    # Wait 3 seconds before closing
    
    #webbot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    #webbot.stop_browser()

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
