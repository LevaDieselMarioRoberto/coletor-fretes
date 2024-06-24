from config import BASE_DIR
import json


class Posto():

    def __init__(self):
        volumes = ['fob', 5, 10, 15, 20, 25, 30, 35]
        combustiveis = ["etanol", "gas_ad", "gas", "s10", "s500"]

        self.precos = self.__cria_dicionario_precos(volumes, combustiveis)
        volumes.remove('fob')
        self.fretes = self.__cria_dicionario_precos(volumes, combustiveis)

    def __str__(self):
        msg = ''
        for vol in self.precos:
            msg += f'{vol}:\n'
            for comb in self.precos[vol]:
                if vol != 'fob': msg += f'    {comb}: {self.precos[vol][comb]} - Frete: {self.fretes[vol][comb]}\n'
                else: msg += f'    {comb}: {self.precos[vol][comb]}\n'
        return msg

    def __cria_dicionario_precos(self, volumes:list, combustiveis:list):
        precos = {}
        for volume in volumes:
            precos[str(volume)] = {}
            for combustivel in combustiveis:
                precos[f'{volume}'][f'{combustivel}'] = None
        return precos

    def calcula_fretes(self):
        for volume in self.fretes:
            for combustivel in self.fretes[volume]:
                self.fretes[volume][combustivel] = round(self.precos[volume][combustivel] - self.precos['fob'][combustivel], 4)

    def salva_json(self):
        arquivo_json = BASE_DIR + f"precos/precos.json"
        with open(arquivo_json, 'w') as f:
            json.dump(self.precos, f, indent=2)

        arquivo_json = BASE_DIR + f"precos/fretes.json"
        with open(arquivo_json, 'w') as f:
            json.dump(self.fretes, f, indent=2)
