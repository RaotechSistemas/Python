
from types import MethodType, ModuleType


def media_notas():
    v1 = (float(input('Digite a 1ª nota: ')))
    v2 = (float(input('Digite a 2ª nota: ')))
    v3 = (float(input('Digite a 3ª nota: ')))
    v4 = (float(input('Digite a 4ª nota: ')))
    soma = v1 + v2 + v3 + v4
    media = soma / 4
    return media


resultado = media_notas()


print(resultado)


