class RoboExplorador:
    def __init__(self, nome, planeta_destino, energia):
        self.nome = nome
        self.planeta_destino = planeta_destino
        self.energia = energia

    def __str__(self):
        return f'Robo: {self.nome} - Destino: {self.planeta_destino} - Energia: {self.energia}%'

robo = RoboExplorador('Xablau', 'Marte', 87)
print(robo)
