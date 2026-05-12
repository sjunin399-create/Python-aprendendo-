url = input('Digite um URL de um site: ')
pos_separador = url.find('://')
pos_barra = url.find('/', pos_separador + 3)
print(
    f' O protocolo e: {url[:pos_separador]}\n O dominio: {url[pos_separador + 3 : pos_barra]} \n Caminho: {url[pos_barra:]}'
)
