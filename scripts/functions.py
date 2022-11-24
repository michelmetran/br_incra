"""
Funções

"""


import pprint
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from traquitanas.scrapping import gecko


class Driver:
    """
    Create Driver

    :param webdriver: _description_
    :type webdriver: _type_
    """

    def __init__(self, driver_path, logs_path, download_path):
        """
        _summary_

        :param driver_path: _description_
        :type driver_path: _type_
        :param logs_path: _description_
        :type logs_path: _type_
        :param download_path: _description_
        :type download_path: _type_
        """
        # Services
        gecko_path = gecko.get_path_geckodriver(driver_path, verify_ssl=True)

        # Logs
        logs_filepath = logs_path / 'geckodriver.log'

        # Services
        service = FirefoxService(
            executable_path=gecko_path, log_path=logs_filepath
        )

        # Options
        options = FirefoxOptions()
        options.headless = False
        options.set_preference('intl.accept_languages', 'pt-BR, pt')
        options.set_preference('browser.download.folderList', 2)
        options.set_preference('browser.aboutConfig.showWarning', False)
        options.set_preference(
            'browser.download.manager.showWhenStarting', False
        )
        options.set_preference('browser.download.dir', str(download_path))
        options.set_preference(
            'browser.helperApps.neverAsk.saveToDisk',
            'application/octet-stream, application/pdf, application/vnd.ms-excel',
        )
        options.set_preference(
            'browser.helperApps.showOpenOptionForPdfJS', False
        )
        options.set_preference('browser.download.forbid_open_with', True)
        options.set_preference(
            'general.useragent.override',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        )
        options.set_preference('pdfjs.disabled', True)
        options.set_preference('plugin.scan.Acrobat', '99.0')
        options.set_preference('plugin.scan.plid.all', False)

        # Driver
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.maximize_window()

    def go_page(self):
        """
        _summary_
        """
        url = 'https://certificacao.incra.gov.br/csv_shp/export_shp.py'
        self.driver.get(url)

    def get_estados(self):
        """
        Lista os Estados Disponíveis
        """
        # Pega todas as opções de Estados
        ufs_xpath = self.driver.find_elements(
            By.XPATH, "//*[@id='selectuf']/option"
        )

        # Monta uma lista com as opções de Estado
        ufs = []
        for i in ufs_xpath[1:]:
            # print(i.get_attribute('innerHTML'))
            ufs.append(i.get_attribute('innerHTML'))

        return ufs

    def get_infos(self):
        """
        ddd
        """
        # Get text of file
        text = self.driver.find_element(
            By.XPATH, '//*[@class="form-horizontal form_2"]'
        ).text
        text = text.split('\n')
        text = [i.split(':') for i in text]

        # Get dictionary
        return {
            'camada': text[0][1].strip(),
            'srid': text[1][1].strip(),
            'processamento': text[2][1].strip(),
            'nome_arquivo': text[3][1].strip(),
        }

    def get_sigef(self, estado, t=60):
        """
        Sigef
        """
        # Start
        print(f'Sigef de "{estado}": início donwload...')

        # Seleciona "Nome da Camada"
        sat = Select(self.driver.find_element(By.XPATH, "//*[@id='selectshp']"))
        sat.select_by_visible_text('Imóvel certificado SIGEF Total')

        # Seleciona o Estado
        uf = Select(self.driver.find_element(By.XPATH, "//*[@id='selectuf']"))
        uf.select_by_visible_text(estado)
        time.sleep(2)

        # Clica em "Enviar" para gerar o arquivo
        self.driver.find_element(By.XPATH, "//*[@id='enviar']").click()
        # time.sleep(2)

        # Enquanto está processando, aguarda
        dict_infos = self.get_infos()
        while dict_infos['camada'] == '...':
            time.sleep(2)
            dict_infos = self.get_infos()
            print('... waiting...')
        pprint.pprint(dict_infos)

        # Clica para fazer download
        self.driver.find_element(
            By.XPATH, '//*[@class="form-horizontal form_2"]//a'
        ).click()
        time.sleep(t)

    def get_snci(self, estado, t=60):
        """
        SNCI
        """
        # Start
        print(f'SNCI de "{estado}": início donwload...')

        # Seleciona "Nome da Camada"
        sat = Select(self.driver.find_element(By.XPATH, "//*[@id='selectshp']"))
        sat.select_by_visible_text('Imóvel certificado SNCI Total')

        # Seleciona o Estado
        uf = Select(self.driver.find_element(By.XPATH, "//*[@id='selectuf']"))
        uf.select_by_visible_text(estado)
        time.sleep(2)

        # Clica em "Enviar" para gerar o arquivo
        self.driver.find_element(By.XPATH, "//*[@id='enviar']").click()
        # time.sleep(2)

        # Enquanto está processando, aguarda
        dict_infos = self.get_infos()
        while dict_infos['camada'] == '...':
            time.sleep(2)
            dict_infos = self.get_infos()
            print('... waiting...')
        pprint.pprint(dict_infos)

        # Clica para fazer download
        self.driver.find_element(
            By.XPATH, '//*[@class="form-horizontal form_2"]//a'
        ).click()
        time.sleep(t)

    def get_assentamento(self, estado, t=60):
        """
        Projeto de Assentamento
        """
        # Start
        print(f'Assentamento de "{estado}": início donwload...')

        # Seleciona "Nome da Camada"
        sat = Select(self.driver.find_element(By.XPATH, "//*[@id='selectshp']"))
        sat.select_by_visible_text('Projetos de Assentamento Total')

        # Seleciona o Estado
        uf = Select(self.driver.find_element(By.XPATH, "//*[@id='selectuf']"))
        uf.select_by_visible_text(estado)
        time.sleep(2)

        # Clica em "Enviar" para gerar o arquivo
        self.driver.find_element(By.XPATH, "//*[@id='enviar']").click()
        # time.sleep(2)

        # Enquanto está processando, aguarda
        dict_infos = self.get_infos()
        while dict_infos['camada'] == '...':
            time.sleep(2)
            dict_infos = self.get_infos()
            print('... waiting...')
        pprint.pprint(dict_infos)

        # Clica para fazer download
        self.driver.find_element(
            By.XPATH, '//*[@class="form-horizontal form_2"]//a'
        ).click()
        time.sleep(t)

    def get_quilombolas(self, estado, t=60):
        """
        Quilombolas
        """
        # Start
        print(f'Quilombolas de "{estado}": início donwload...')

        # Seleciona "Nome da Camada"
        sat = Select(self.driver.find_element(By.XPATH, "//*[@id='selectshp']"))
        sat.select_by_visible_text('Áreas de Quilombolas')

        # Seleciona o Estado
        uf = Select(self.driver.find_element(By.XPATH, "//*[@id='selectuf']"))
        uf.select_by_visible_text(estado)
        time.sleep(2)

        # Clica em "Enviar" para gerar o arquivo
        self.driver.find_element(By.XPATH, "//*[@id='enviar']").click()
        # time.sleep(2)

        # Enquanto está processando, aguarda
        dict_infos = self.get_infos()
        while dict_infos['camada'] == '...':
            time.sleep(2)
            dict_infos = self.get_infos()
            print('... waiting...')
        print(dict_infos)

        # Clica para fazer download
        self.driver.find_element(
            By.XPATH, '//*[@class="form-horizontal form_2"]//a'
        ).click()
        time.sleep(t)

    def quit(self):
        """
        _summary_
        """
        self.driver.quit()


if __name__ == '__main__':
    from paths import driver_path, input_path, logs_path

    # Driver
    driver = Driver(driver_path, logs_path, input_path)
    driver.go_page()

    # Quit Driver
    time.sleep(4)
    driver.quit()
