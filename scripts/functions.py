"""


"""


import os
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options




class Pom:
    def __init__(self, driver) -> None:
        driver = pass




def get_infos():
    """



    """
    # Get text of file
    text = driver.find_element(
        By.XPATH, '//*[@class="form-horizontal form_2"]').text
    text = text.split('\n')
    text = [i.split(':') for i in text]

    # Get dictionary
    return {
        'camada': text[0][1].strip(),
        'srid': text[1][1].strip(),
        'processamento': text[2][1].strip(),
        'nome_arquivo': text[3][1].strip(),
    }


def get_sigef_estado(estado, t=60):
    """
    Sigef

    """

    # Start
    print(f'"{estado}" início donwload...')

    # Seleciona "Nome da Camada"
    sat = Select(driver.find_element(By.XPATH, "//*[@id='selectshp']"))
    sat.select_by_visible_text('Imóvel certificado SIGEF Total')

    # Seleciona o Estado
    uf = Select(driver.find_element(By.XPATH, "//*[@id='selectuf']"))
    uf.select_by_visible_text(estado)
    time.sleep(2)

    # Clica em "Enviar" para gerar o arquivo
    driver.find_element(By.XPATH, "//*[@id='enviar']").click()
    # time.sleep(2)

    # Enquanto está processando, aguarda
    dict_infos = get_infos()
    while dict_infos['camada'] == '...':
        time.sleep(2)
        dict_infos = get_infos()
        print('Waiting...')
    print(dict_infos)

    # Clica para fazer download
    driver.find_element(
        By.XPATH, '//*[@class="form-horizontal form_2"]//a').click()
    time.sleep(t)

    # End
    print(f'"{estado}" donwload ok!')


def get_snci_estado(estado, t=60):
    """
    SNCI

    """
    # Start
    print(f'"{estado}" início donwload...')

    # Seleciona "Nome da Camada"
    sat = Select(driver.find_element(By.XPATH, "//*[@id='selectshp']"))
    sat.select_by_visible_text('Imóvel certificado SNCI Total')

    # Seleciona o Estado
    uf = Select(driver.find_element(By.XPATH, "//*[@id='selectuf']"))
    uf.select_by_visible_text(estado)
    time.sleep(2)

    # Clica em "Enviar" para gerar o arquivo
    driver.find_element(By.XPATH, "//*[@id='enviar']").click()
    # time.sleep(2)

    # Enquanto está processando, aguarda
    dict_infos = get_infos()
    while dict_infos['camada'] == '...':
        time.sleep(2)
        dict_infos = get_infos()
        print('Waiting...')
    print(dict_infos)

    # Clica para fazer download
    driver.find_element(
        By.XPATH, '//*[@class="form-horizontal form_2"]//a').click()
    time.sleep(t)

    # End
    print(f'"{estado}" donwload ok!')


def get_assentamento_estado(estado, t=60):
    """
    Projeto de Assentamento

    """

    # Start
    print(f'"{estado}" início donwload...')

    # Seleciona "Nome da Camada"
    sat = Select(driver.find_element(By.XPATH, "//*[@id='selectshp']"))
    sat.select_by_visible_text('Projetos de Assentamento Total')

    # Seleciona o Estado
    uf = Select(driver.find_element(By.XPATH, "//*[@id='selectuf']"))
    uf.select_by_visible_text(estado)
    time.sleep(2)

    # Clica em "Enviar" para gerar o arquivo
    driver.find_element(By.XPATH, "//*[@id='enviar']").click()
    # time.sleep(2)

    # Enquanto está processando, aguarda
    dict_infos = get_infos()
    while dict_infos['camada'] == '...':
        time.sleep(2)
        dict_infos = get_infos()
        print('Waiting...')
    print(dict_infos)

    # Clica para fazer download
    driver.find_element(
        By.XPATH, '//*[@class="form-horizontal form_2"]//a').click()
    time.sleep(t)

    # End
    print(f'"{estado}" donwload ok!')




def get_quilombolas_estado(estado, t=60):
    """
    Quilombolas
    """

    # Start
    print(f'"{estado}" início donwload...')

    # Seleciona "Nome da Camada"
    sat = Select(driver.find_element(By.XPATH, "//*[@id='selectshp']"))
    sat.select_by_visible_text('Áreas de Quilombolas')

    # Seleciona o Estado
    uf = Select(driver.find_element(By.XPATH, "//*[@id='selectuf']"))
    uf.select_by_visible_text(estado)
    time.sleep(2)

    # Clica em "Enviar" para gerar o arquivo
    driver.find_element(By.XPATH, "//*[@id='enviar']").click()
    # time.sleep(2)

    # Enquanto está processando, aguarda
    dict_infos = get_infos()
    while dict_infos['camada'] == '...':
        time.sleep(2)
        dict_infos = get_infos()
        print('Waiting...')
    print(dict_infos)

    # Clica para fazer download
    driver.find_element(
        By.XPATH, '//*[@class="form-horizontal form_2"]//a').click()
    time.sleep(t)

    # End
    print(f'"{estado}" donwload ok!')




if __name__ == '__main__':
    import time

    a = Pom()