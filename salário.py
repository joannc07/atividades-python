salario_incial = float(input('Digite o valor do salário: '))
salario_final = salario_incial+(salario_incial*0.15)
print('O salário incial era de R${:.2f} e após o aumento recebido passou a ser R${:.2f}'. format(salario_incial,salario_final))