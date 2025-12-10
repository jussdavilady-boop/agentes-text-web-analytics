"""
NER Agent
---------
Detecta entidades simples usando heurísticas sin dependencias externas.
"""

import re


def simple_ner(text: str):
    """
    Detecta entidades que empiezan por mayúsculas.
    Ejemplo: "Gobierno de Colombia", "Banco Mundial".
    """
    if not text:
        return []

    pattern = r'([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)*)'
    entities = re.findall(pattern, text)

    # Eliminar duplicados conservando orden
    return list(dict.fromkeys(entities))
