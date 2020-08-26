from selenium import webdriver
from time import sleep
import os
#Gabriel Lopes - FEI
def pegar_conta():
    arquivo=open("Desktop\BOTS\conta_fei.txt","r")#Crie um arquivo com o seu login e senha e coloque o caminho dele aqui. (Coloque nesse formato-> login:senha)
    conta=arquivo.readlines()
    conta=conta[0].split(":")
    return conta[0],conta[1]
class Bot():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'Desktop\BOTS\geckodriver\geckodriver.exe')#Baixe o geckodriver e coloque o caminho dele aqui
    def avaliar(self,login,senha):
        from datetime import date
        hoje=int(date.today().weekday())
        dia=["segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira","sábado"]
        driver=self.driver
        driver.get("https://interage.fei.org.br/secureserver/portal")
        sleep(1)
        driver.find_element_by_id("Usuario").send_keys(login)
        driver.find_element_by_id("Senha").send_keys(senha)
        driver.find_element_by_id("btn-login").click()
        driver.get("https://interage.fei.org.br/secureserver/portal/graduacao/secretaria/temporarios-e-sazonais/avaliacoes-semanais")
        sleep(1)
        for x in range (0,hoje):
            try:
                driver.find_element_by_link_text(dia[x]+" 1").click()
            except:
                print(dia[x],"já avaliado.")
            lista=driver.find_elements_by_xpath("//label[@data-original-title='Muito bom']")
            for carinha in lista:
                try:
                    carinha.click()
                    sleep(1)
                except:
                    sleep(1)
            lista=driver.find_elements_by_name("cadastrar")
            for botao in lista:
                try:
                    botao.click()
                    sleep(1)
                except:
                    sleep(1)
bot=Bot()
login,senha=pegar_conta()
bot.avaliar(login,senha)
