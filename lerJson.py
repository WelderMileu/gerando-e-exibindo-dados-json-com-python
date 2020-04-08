import json

def ler():
	with open('arquivo.json', 'r', encoding='utf8') as f:
		return json.load(f)


dados = ler()

print(dados['user'])