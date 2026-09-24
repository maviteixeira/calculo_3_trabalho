"""Estruturas disponíveis no VoluLab.

Para adicionar uma estrutura: crie a classe em um novo arquivo deste pacote
(herdando de `Solido`) e registre-a em `ESTRUTURAS`. Ver docs/arquitetura.md.
"""

from volulab.models.base import Malha, Solido
from volulab.models.comodo_retangular import ComodoRetangular

#: Nome de exibição -> classe. O app monta o menu a partir deste dicionário.
ESTRUTURAS: dict[str, type[Solido]] = {
    ComodoRetangular.nome: ComodoRetangular,
}

__all__ = ["ESTRUTURAS", "ComodoRetangular", "Malha", "Solido"]
