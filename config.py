import os
from getpass import getuser
from dotenv import load_dotenv

user = getuser()
onedrive = f"C:/Users/{user}/OneDrive - MARIO ROBERTO TRANSP REVENDEDORA D OLEO DIESEL/Leva Diesel/"

BASE_DIR = f"{onedrive}/Informatica/projetos/coletor_frete/"
JSON_VIBRA_JJ = f"{onedrive}/Informatica/projetos/coletor_precos/precos/Vibra Janjão.json"
PLANILHA_DIR = f"{onedrive}/Logística/Frete.xlsx"
PLANILHA_BKP_DIR = f"{BASE_DIR}Frete.xlsx"
ARQUIVO_LOG = BASE_DIR + "dist/coletor.log"
ARQUIVO_ENV = BASE_DIR + ".env" # Necessário ser explícito para execução de tarefa automática do Windows

load_dotenv(ARQUIVO_ENV)

CONTROLS = {
    'coleta_habilitada':    os.getenv('COLETA_HABILITADA', 'true').lower() == 'true',
    'maximizado':           os.getenv('MAXIMIZADO', 'false').lower() == 'true',
    'max_tentativas':       int(os.getenv('MAX_TENTATIVAS')),
    'intervalo_se_erro':    int(os.getenv('INTERVALO_SE_ERRO')),

    'imprime_precos_terminal':  os.getenv('IMPRIME_PRECOS_TERMINAL', 'false').lower() == 'true',
    'salva_precos_planilha':    os.getenv('SALVA_PRECOS_PLANILHA', 'false').lower() == 'true',
}

TELEGRAM_CONFIG = {
    'token':    os.getenv('TOKEN'),
    'idchat':   os.getenv('IDCHAT'),
}

VAR = {
    'link':         os.getenv('LINK_IPR'),
    'link_pedidos': os.getenv('LINK_PEDIDOS_IPR'),

    'login': os.getenv('LOGIN_IPR_POSTOS'),
    'senha': os.getenv('SENHA_IPR_POSTOS'),

    'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN'),
    'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA'),

    'xpath_button_entrar':  os.getenv('XPATH_BUTTON_ENTRAR'),
    'xpath_button_cookies': os.getenv('XPATH_BUTTON_COOKIES'),
    'xpath_button_entrega': os.getenv('XPATH_BUTTON_ENTREGA'),

    'xpath_button_razaosocial': os.getenv('XPATH_BUTTON_RAZAOSOCIAL'),
    'xpath_button_itirapua':    os.getenv('XPATH_BUTTON_ITIRAPUA'),
    'xpath_iframe':             os.getenv('XPATH_IFRAME'),
    'xpath_iframe_pedidos':     os.getenv('XPATH_IFRAME_PEDIDOS'),

    'cif_etanol':   os.getenv('XPATH_ETANOL_CIF'),
    'fob_etanol':   os.getenv('XPATH_ETANOL_FOB'),
    'cif_gas':      os.getenv('XPATH_GASOLINA_CIF'),
    'fob_gas':      os.getenv('XPATH_GASOLINA_FOB'),
    'cif_gas_ad':   os.getenv('XPATH_GASOLINAAD_CIF'),
    'fob_gas_ad':   os.getenv('XPATH_GASOLINAAD_FOB'),
    'cif_s500':     os.getenv('XPATH_S500_CIF'),
    'fob_s500':     os.getenv('XPATH_S500_FOB'),
    'cif_s10':      os.getenv('XPATH_S10_CIF'),
    'fob_s10':      os.getenv('XPATH_S10_FOB'),

    'button_5':     os.getenv('XPATH_BUTTON_5'),
    'button_15':    os.getenv('XPATH_BUTTON_15'),
    'button_20':    os.getenv('XPATH_BUTTON_20'),
    'button_25':    os.getenv('XPATH_BUTTON_25'),
    'button_30':    os.getenv('XPATH_BUTTON_30'),

    'input_etanol': os.getenv('XPATH_INPUT_ETANOL'),
    'input_gas':    os.getenv('XPATH_INPUT_GASOLINA'),

    'cif35_etanol':    os.getenv('XPATH_ETANOL_CIF35'),
    'cif35_gas':       os.getenv('XPATH_GASOLINA_CIF35'),
    'cif35_gas_ad':    os.getenv('XPATH_GASOLINAAD_CIF35'),
    'cif35_s500':      os.getenv('XPATH_S500_CIF35'),
    'cif35_s10':       os.getenv('XPATH_S10_CIF35'),
}
