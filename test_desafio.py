import pytest
from RelatorioDeMissao import RelatorioDeMissao, leituras
from RoboExplorador import RoboExplorador

def test_roboExplorador():
    Robo = RoboExplorador('Xablau', 'Marte', 87)
    assert str(Robo)

def test_relatorioDeMissao():
    leituras = (('temperatura', -50), ('radiacao', 2.5),)
    relatorio = RelatorioDeMissao('Xablau', ' Marte', 87, leituras)
