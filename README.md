## Gerando e Exibindo dados com Python em Formato JSON

### Gerando nosso json

Esse nosso arquivo jsonGenerator.py tem como objetivo gerar o nosso documento json.

Rodando nossa função no terminal.

``` bash
	
	python jsonGenerator.py

```

Nosso script do arquivo jsonGenerator.py.

``` Python

	import json # Biblioteca para manipular nosso json

	# Função para gerar o nosso json
	def generator(dados):
		with open('arquivo.json', 'w', encoding='utf8') as f:
			json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',',':'))
	
	# Nosso json que ira como parametro
	myJson = {
		'user': 'admin',
		'password': '12345'
	}
	
	# Executando a funcão
	generator(myJson)

``` 