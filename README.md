# 🚀 Sistema de Controle de Robôs Exploradores
Este projeto é um sistema para controle de robôs exploradores que realizam missões em planetas e enviam relatórios para a base de comando.

![Image](https://github.com/user-attachments/assets/cb1c1c39-c831-49c0-b9b7-299eb08bafbb)

## 📦 Sobre o Projeto
O sistema é dividido em três partes principais:

### 1. Classe RoboExplorador
Responsável por representar um robô explorador.

#### Atributos:

- nome (str): Nome do robô.
- planeta_destino (str): Nome do planeta onde o robô realizará a missão.
- energia (int): Energia atual do robô, de 0 a 100.

#### Método:

- str(): Retorna uma string no formato:

```json 
    Robô Xablau - Destino: Marte - Energia: 87%
```

### 2. Classe RelatorioDeMissao (herdada de RoboExplorador)
Representa o relatório gerado pelas missões dos robôs.

#### Atributos adicionais:

leituras 

- Tipo do dado (ex: "temperatura")
- Valor do dado (ex: -50)

Exemplo de leituras:

```json
(
    ("temperatura", -50),
    ("radiação", 2.5),
)
```
#### Métodos:

- resumo(): Retorna uma lista de frases

```json
["temperatura: -50", "radiação: 2.5"]
```
- contagem_leituras(): Retorna o número total de leituras feitas.

#### 3. Testes com pytest

- O sistema inclui testes automáticos que verificam:

- Funcionamento da classe RoboExplorador.

- Herança correta da classe RelatorioDeMissao.

- Funcionamento dos métodos resumo e contagem_leituras.

## 📜 Exemplo de Uso
```json
leituras = (
    (('temperatura', -50), ('radiacao', 2.5)),
    (('temperatura', -20), ('radiacao', 1.1)),
)

destinos = [
    ('Xablau', 'Marte', 87),
    ('Xablau', 'Saturno', 91),
]

for destino, leitura in zip(destinos, leituras):
    relatorio = RelatorioDeMissao(destino[0], destino[1], destino[2], leitura)
    print(relatorio)
    print(relatorio.resumo())
    print(relatorio.contagem_leituras())
```    

- Saída esperada:

```json
Robô Xablau - Destino: Marte - Energia: 87%
['temperatura: -50', 'radiacao: 2.5']
Robô Xablau - Destino: Saturno - Energia: 91%
['temperatura: -20', 'radiacao: 1.1']
```

## 🛠️ Tecnologias Utilizadas

- Python 3.x

#### Para rodar os testes:

```bash
pytest
```

## 📜 Como Usar
- Clone o repositório:
```bash
git clone https://github.com/wendellbaresizup/desafio2-python.git
```
- Acesse a pasta do projeto:

```bash
cd desafio2
```


### 👨‍💻 Autor
Projeto desenvolvido por Wendell Baresi
