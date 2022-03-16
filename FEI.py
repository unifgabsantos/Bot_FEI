from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
def getAccounts()->list:
    accounts = []
    try:
        file = open("./Resources/accounts.txt","r")
    except:
        print("\nCrie um arquivo chamado accounts dentro de Resources e coloque as contas nesse formato:\nlogin:senha\nlogin2:senha2\n")
        exit(0)
    for line in file.readlines():
        try:
            line = line.strip().split(":")
            username,password = line[0],line[1]
        except:
            print("\nColoque as contas nesse formato:\nlogin:senha\nlogin2:senha2\n")
            exit(0)
        accounts.append({"Username":username,"Password":password})
    return accounts
class Bot():
    def __init__(self,account:dict) -> None:
        self.account = account
        try:
            self.driver = webdriver.Chrome("./Resources/chromedriver.exe")
        except:
            print("\nBaixe o chrome driver que tenha a mesma versão do chrome da sua maquina e coloque em dentro da pasta Resources\n\nSite:https://chromedriver.chromium.org/downloads\n")
            exit(0)
    def start(self):
        driver = self.driver
        account = self.account
        driver.get("https://interage.fei.org.br/secureserver/portal")
        sleep(5)
        try:
            driver.find_element_by_id("Usuario").send_keys(account['Username'])
            driver.find_element_by_id("Senha").send_keys(account['Password'])
            driver.find_element_by_id("btn-login").click()
        except:
            print("Esse erro não deveria acontecer, mas se aconteceu me envie um e-mail: gabriel.lopessb@gmail.com ")
        sleep(1)
        driver.get("https://interage.fei.org.br/secureserver/portal/graduacao/sala-dos-professores/aulas/presenca")
        sleep(3)