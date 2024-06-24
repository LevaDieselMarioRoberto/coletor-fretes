from posto import Posto
from coletores_precos.coletor_precos_itirapua import ColetorPrecosItirapua
from planilha import Planilha
from logger import Logger
from time import time
from config import CONTROLS

logger = Logger()

if CONTROLS['coleta_habilitada']:

    posto = Posto()
    coletor = ColetorPrecosItirapua()

    inicio = time()
    logger.log(f"   --- Iniciando coleta de preços... ---")

    coletor.coleta_precos(posto, CONTROLS['maximizado'])

    if CONTROLS['imprime_precos_terminal']: print(posto)

    if CONTROLS['salva_precos_planilha']:
        planilha = Planilha()
        planilha.preenche_planilha(posto)

    tempo_total = round(time() - inicio, 2)
    logger.log(f"Tempo de execução total: {tempo_total}s")

else:
    logger.log("Coleta desabilitada ou fora do horário permitido.")
