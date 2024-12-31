from ex112.utilidadescev.moeda import moeda
from ex112.utilidadescev.dados import dados

p = dados.leiaDinheiro('Digite o valor: R$')
moeda.resumo(p, 80, 35)
