horastrab = float(input("Digite a quantidade de horas trabalhadas: "))
preco_excedente = 20.00

if (horastrab > 50):
    salario = 500.00
    excedente = (horastrab - 50) * preco_excedente
    print(f'O valor salario é R$:{salario}')
    print(f' e Excedente: R$:{excedente} ')
    print(f' O Total a receber: R$: ',salario+excedente)

else:

    salario = horastrab * 10.00
    excedente = 0.0
    print(f'O valor salario é R$:{salario}')
    print(f' e Excedente: R$:{excedente} ')
