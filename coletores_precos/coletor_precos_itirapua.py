from coletores_precos.coletor_precos import ColetorDePrecos
from logger import Logger
from posto import Posto
from telegram import Telegram
from time import time, sleep
from config import VAR, CONTROLS


class ColetorPrecosItirapua(ColetorDePrecos):

    def __init__(self):
        super().__init__()

    def coleta_precos(self, posto:Posto, maximizado=False):
        """
        Coleta preços de combustíveis do portal da Ipiranga (Itirapuã).
        """
        tentativa = 1
        max_tentativas = CONTROLS['max_tentativas']
        intervalo_se_erro = CONTROLS['intervalo_se_erro']
        logger = Logger()

        while tentativa <= max_tentativas:
            try:
                logger.log(f"Iniciando coleta de preços (tentativa {tentativa}/{max_tentativas})")
                self.navegador = self.inicializa_navegador(maximizado)
                self.inicio = time()

                # Login na página principal
                self.navegador.get(VAR['link'])
                self.preenche_input(VAR['xpath_input_login'], VAR['login'])
                self.preenche_input(VAR['xpath_input_senha'], VAR['senha'])
                self.clica_botao(VAR['xpath_button_entrar'])
                self.clica_botao(VAR['xpath_button_cookies'])
                logger.log(f"Login realizado com sucesso")
                sleep(3)

                # Seleciona a filial de Itirapuã
                self.clica_botao(VAR['xpath_button_razaosocial'])
                self.clica_botao(VAR['xpath_button_itirapua'])
                sleep(2)
                self.troca_iframe(VAR['xpath_iframe'])
                sleep(1)
                logger.log(f"Filial de Itirapuã selecionada")

                # Coleta de preços
                volumes = [10, 5, 15, 20, 25, 30, 35]
                combustiveis = ['etanol', 'gas', 'gas_ad', 's500', 's10']

                for vol in volumes:
                    if vol != 35 and vol != 10:
                        self.clica_botao(VAR[f'button_{vol}'])
                        sleep(2)

                        for combustivel in combustiveis:
                            posto.precos[f'{vol}'][combustivel] = self.coleta_valor(VAR[f'cif_{combustivel}'])
                        sleep(1)

                    elif vol == 10:
                        for combustivel in combustiveis:
                            posto.precos[f'{vol}'][combustivel] =   self.coleta_valor(VAR[f'cif_{combustivel}'])
                            posto.precos['fob'][combustivel] =  self.coleta_valor(VAR[f'fob_{combustivel}'])
                        sleep(1)

                    else:
                        self.navegador.get(VAR['link_pedidos'])
                        sleep(2)
                        self.troca_iframe(VAR['xpath_iframe_pedidos'])
                        sleep(2)
                        self.clica_botao(VAR['xpath_button_entrega'])
                        sleep(2)
                        self.preenche_input(VAR['input_etanol'], 35000)
                        sleep(1)
                        self.preenche_input(VAR['input_gas'], 35000)
                        sleep(2)

                        for combustivel in combustiveis:
                            posto.precos[f'{vol}'][combustivel] = self.coleta_valor(VAR[f'cif35_{combustivel}'])
                            sleep(1)

                    logger.log(f"Preços de {vol}m³ coletados")

                self.fechar_navegador()
                self.tempo_execucao = round(time() - self.inicio, 2)
                logger.log(f"Preços coletados com sucesso. Tempo de coleta: {self.tempo_execucao}s")

                posto.calcula_fretes()
                posto.salva_json()
                logger.log(f"Fretes calculados / Arquivos json salvos")
                break

            except Exception as e:
                tentativa += 1
                self.fechar_navegador()

                if tentativa <= max_tentativas:
                    logger.log_error(f"Erro na coleta de preços, nova tentativa em {intervalo_se_erro}s...")
                    sleep(intervalo_se_erro)
                    continue
                else:
                    telegram = Telegram()
                    telegram.enviar_mensagem(f"Erro na coleta de valores de frete!")
                    logger.log_error(f"Coleta de preços não realizada! Erro: {e}")
                    break
