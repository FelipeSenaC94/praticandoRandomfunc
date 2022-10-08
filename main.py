
import random

def confronto():
    if atkNeo > atkAS:
        print('O poder de ataque de Neo é maior que o do agente smith.')
    elif atkAS > atkNeo:
        print('O poder de ataque do Agente Smith é maior que o de Neo.')
    else:
        print('o poder de ataque é igual')


for i in range(3):
    atkNeo = (random.randint(1, 100))
    defNeo = (random.randint(1, 100))
    atkAS = (random.randint(1, 100))
    defAS = (random.randint(1, 100))
    print('O poder de ataque de Neo é: ', atkNeo)
    print('O poder de ataque do Agente Smith é: ', atkAS)
    print('O poder de defesa de Neo é: ', defNeo)
    print('O poder de defesa do Agente Smith é: ', defAS)

    confronto()