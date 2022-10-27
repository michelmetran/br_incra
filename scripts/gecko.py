"""
Equivalente ao Webdriver Project
Evita a necessidade de instalar drivers

https://github.com/mozilla/geckodriver/releases
out/22
"""

import tarfile
import requests
import platform
from paths import *
from zipfile import ZipFile


def _check_geckodriver_exists(path):
    # Paths
    path.mkdir(exist_ok=True)
    gecko_win_filepath = path / 'geckodriver.exe'
    gecko_linux_filepath = path / 'geckodriver'

    if platform.system() == 'Windows':
        if gecko_win_filepath.is_file():
            return True
        elif not gecko_win_filepath.is_file():
            return False

    elif platform.system() == 'Linux':
        if gecko_linux_filepath.is_file():
            return True

        elif not gecko_linux_filepath.is_file():
            return False

    else:
        return None


def _get_geckodriver(path):
    """
    Faz o download do geckodriver!
    TODO: Testar no windows!

    :param path:
    :return:
    """
    # Test
    has_geckodriver = _check_geckodriver_exists(path)

    # print(gecko_zip_filepath)
    if not has_geckodriver:
        if platform.system() == 'Windows':
            # Download do geckodriver
            url = 'https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-win64.zip'
            r = requests.get(url, verify=False)

            # Save
            gecko_zip_filepath = path / Path(url).name
            with open(gecko_zip_filepath, 'wb') as f:
                f.write(r.content)

            # Extract
            with ZipFile(gecko_zip_filepath, 'r') as zip_ref:
                zip_ref.extractall(path)

        elif platform.system() == 'Linux':
            # Download do geckodriver
            url = 'https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz'
            r = requests.get(url, verify=True)

            # Save
            gecko_zip_filepath = path / Path(url).name
            with open(gecko_zip_filepath, 'wb') as f:
                f.write(r.content)

            # Extract
            with tarfile.open(gecko_zip_filepath, 'r') as tar_ref:
                tar_ref.extractall(path)

    elif has_geckodriver:
        print(f'Geckodriver already in {path}')


def get_path_geckodriver(path):
    # Faz download se for necessário
    _get_geckodriver(path)

    # Path
    if platform.system() == 'Windows':
        gecko_path = path / 'geckodriver.exe'
        gecko_path = gecko_path.resolve().as_posix().replace('/', '\\')
        return gecko_path

    elif platform.system() == 'Linux':
        gecko_path = path / 'geckodriver'
        return gecko_path
    else:
        return None



if __name__ == '__main__':
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService

    # Services
    gecko_path = get_path_geckodriver(driver_path)
    service = FirefoxService(executable_path=gecko_path, log_path=logs_path / 'geckodriver.log')

    # Driver
    driver = webdriver.Firefox(service=service)
    driver.get('https://github.com/SergeyPirogov/webdriver_manager')

    # Close Connection
    time.sleep(4)
    driver.quit()

    # Message
    print('Driver close!!')
