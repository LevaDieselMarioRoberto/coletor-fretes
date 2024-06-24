from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


class ColetorDePrecos(ABC):

    def __init__(self):
        self.inicio = None
        self.tempo_execucao = None
        self.navegador = None

    def inicializa_navegador(self, maximizado):
        """
        Inicializa uma instância do navegador Edge com opções específicas.
        """

        options = webdriver.EdgeOptions()

        if maximizado:
            options.add_argument("--start-maximized")
            options.add_argument("--force-device-scale-factor=0.8")
        else:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")

        options.add_argument("--log-level=1")
        options.add_argument("--enable-chrome-browser-cloud-management")
        svc = EdgeService(EdgeChromiumDriverManager().install())
        navegador = webdriver.Edge(service=svc, options=options)

        return navegador

    def clica_botao(self, xpath, tempo_espera=20, sleep_time=2):
        """
        Clica em um botão na página da web.
        """
        sleep(sleep_time)
        WebDriverWait(self.navegador, tempo_espera).until(EC.presence_of_element_located((By.XPATH, xpath))).click()

    def preenche_input(self, campo, valor, xpath_ou_id='xpath', tempo_espera=20):
        """
        Preenche um campo de input na página da web.
        """
        if xpath_ou_id == 'xpath':
            WebDriverWait(self.navegador, tempo_espera).until(EC.presence_of_element_located((By.XPATH, campo))).send_keys(valor)
        elif xpath_ou_id == 'id':
            WebDriverWait(self.navegador, tempo_espera).until(EC.presence_of_element_located((By.ID, campo))).send_keys(valor)

    def coleta_valor(self, campo, xpath_ou_id='xpath', tempo_espera=20):
        """
        Coleta o valor de um elemento na página da web.
        """
        if xpath_ou_id == 'xpath':
            return round(
                float(
                    WebDriverWait(self.navegador, tempo_espera)
                    .until(EC.presence_of_element_located((By.XPATH, campo)))
                    .get_attribute("innerHTML").replace("<small>R$</small> ", "").strip().replace(",", ".")
                ), 4
            )
        elif xpath_ou_id == 'id':
            return round(
                float(
                    WebDriverWait(self.navegador, tempo_espera)
                    .until(EC.presence_of_element_located((By.ID, campo)))
                    .get_attribute("innerHTML").replace("<small>R$</small> ", "").strip().replace(",", ".")
                ), 4
            )

    def troca_iframe(self, xpath_iframe, tempo_espera=5):
        """
        Troca para um iframe específico.
        """
        iframe = WebDriverWait(self.navegador, tempo_espera).until(EC.presence_of_element_located((By.XPATH, xpath_iframe)))
        self.navegador.switch_to.frame(iframe)

    def fechar_navegador(self):
        """ 
        Fecha o navegador. 
        """
        self.navegador.quit()

    @abstractmethod
    def coleta_precos(self, maximizado=False):
        pass
