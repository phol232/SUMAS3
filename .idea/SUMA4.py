def suma(primerSumando, segundoSumando):
    return primerSumando + segundoSumando
if __name__ == '__main__':
    primerSumando = int(input("Ingrese el primer sumando: "))
segundoSumando = int(input("Ingrese segundo sumando: "))
print(f"{primerSumando} + {segundoSumando} = {suma(primerSumando,segundoSumando)}")

def suma(primerSumando, segundoSumando):
    return primerSumando + segundoSumando

from Suma import suma
if __name__ == '__main__':
    primerSumando = int(input("Ingrese el primer sumando: "))
segundoSumando = int(input("Ingrese segundo sumando: "))
print(f"{primerSumando} + {segundoSumando} = {suma(primerSumando,segundoSumando)}")