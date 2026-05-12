url = input('Digite um URL de um site: ')
pos_separador = url.find('://')
pos_barra = url.find('/', pos_separador + 3)
print(
    f' O protocolo e: {url[:pos_separador]}\n O dominio: {url[pos_separador + 3 : pos_barra]} \n Caminho: {url[pos_barra:]}'
)
# Verificamos se a barra foi encontrada
if pos_barra == -1:
    # Se não tem barra, o domínio começa após o :// e vai até o fim
    dominio = url[pos_separador + 3 :]
    caminho = 'Não possui caminho'
else:
    # Se tem barra, o domínio termina nela
    dominio = url[pos_separador + 3 : pos_barra]
    # E o caminho começa nela e vai até o fim
    caminho = url[pos_barra:]
