import json

def generator(dados):
	with open('arquivo.json', 'w', encoding='utf8') as f:
		json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',',':'))

myJson = {
	'user': 'admin',
	'password': '12345'
}

generator(myJson)