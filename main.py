import requests

site = "https://www.google.com"
resposta = requests.get(site)

print(f"Testando conexão com: {site}")
print(f"Status da resposta: {resposta.status_code}") # 200 significa que está OK!
