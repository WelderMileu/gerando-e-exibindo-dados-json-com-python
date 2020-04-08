# Gerando e Exibindo dados com Python em Formato JSON


### Gerando nosso json

Usamos o arquivo jsonGenarator.py para poder gerar o nosso arquivo json, esse arquivo tem uma função generator que passamos como parametro o nosso json que sera gerado nosso json na raiz da
pasta do projeto.

``` python

import json

def generator(dados):
	with open('arquivo.json', 'w', encoding='utf8') as f:
		json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',',':'))

myJson = {
	'user': 'admin',
	'password': '12345'
}

generator(myJson)

```