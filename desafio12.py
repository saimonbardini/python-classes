"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""

preco_produto = float(input('Informe o preço do produto: R$'))
desconto = float(input('Informe o percentual de desconto: '))

print(f'Valor informado: {preco_produto}\n Valor desconto: {desconto}\nValor final: ', preco_produto - (preco_produto * desconto / 100))