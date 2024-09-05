# CALCULO DO VALOR DA VARIAVEL SOMA
INDICE = 27
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)



# VERIFICAR SE UM NUMERO PERTENCE A SEQUENCIA DE FIBONACCI
def fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    if b == num or num == 0:
        return f"O numero {num} pertence a sequencia de fibonacci"
    else:
        return f"O numero {num} não pertence a sequencia de fibonacci"

num = int(input("Digite um numero: "))
print(fibonacci(num))



# CALCULO DE FATURAMENTO DIARIO
import json

faturamento_json = '''
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612}
]
'''

faturamento = json.loads(faturamento_json)

faturamento_valores = [f['valor'] for f in faturamento if f['valor'] > 0]

menor_faturamento = min(faturamento_valores)
maior_faturamento = max(faturamento_valores)

media_mensal = sum(faturamento_valores) / len(faturamento_valores)

dias_acima_da_media = sum(1 for f in faturamento_valores if f > media_mensal)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento superior à média: {dias_acima_da_media}")



# CALCULO DE PERCENTUAIS DE FATURAMENTO POR ESTADO
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}% do faturamento total")




# INVERSÃO DE STRING SEM FUNÇÕES PRONTAS
def inverter_string(s):
    invertida = ''
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    return invertida

string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")