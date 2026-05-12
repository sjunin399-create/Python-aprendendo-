url = input('Digite um URL de um site: ')
pos_separador = url.find('://')
pos_barra = url.find('/', pos_separador + 3)

# 1. Primeiro tomamos a decisão baseada na barra
if pos_barra == -1:
    dominio = url[pos_separador + 3 :]
    caminho = 'Não possui caminho'
else:
    dominio = url[pos_separador + 3 : pos_barra]
    caminho = url[pos_barra:]

# 2. Agora exibimos as variáveis já prontas
print(f'O protocolo é: {url[:pos_separador]}')
print(f'O domínio é: {dominio}')
print(f'O caminho é: {caminho}')
