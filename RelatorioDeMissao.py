from RoboExplorador import RoboExplorador


class RelatorioDeMissao(RoboExplorador):

    def __init__(self, nome, planeta_destino, energia, leituras):
        super().__init__(nome, planeta_destino, energia)
        self.leituras = leituras

    def resumo(self):
        return [f'{dado[0]}: {dado[1]}' for dado in self.leituras]

    def contagem_leituras(self):
        return f'Total de leituras foram: {len(self.leituras)}'

leituras = (
    (('temperatura', -50),('radiacao', 2.5)),
    (('temperatura', -20),('radiacao', 1.1)),
)

destinos = [
    ('Xablau', ' Marte', 87),
    ('Xablau', ' Saturno', 91),
]

for destino, leitura in zip(destinos, leituras):
    relatorio = RelatorioDeMissao(destino[0],destino[1],destino[2], leitura)
    print(relatorio)
    print(relatorio.resumo())
    print(relatorio.contagem_leituras())