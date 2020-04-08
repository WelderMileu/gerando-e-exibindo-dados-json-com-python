# Gerando e Exibindo dados com Python em Formato JSON


### Gerando nosso json

- Usamos o arquivo jsonGenarator.py para poder gerar o nosso arquivo json, esse arquivo tem uma função generator que passamos como parametro o nosso json que sera gerado na raiz do nosso projeto.


- Primeiro passo e importar o nosso json que por padrão ja vem no python.

``` python

import json

```

- Depois Criaremos nosso funcão reponsavel por criar nosso json

``` python

def generator(dados):
	with open('arquivo.json', 'w', encoding='utf8') as f:
		json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',',':'))


```

- Passamos como parametro dados que representa o json que iremos passar
- with open para apontar o nome do arquivo, 'w' para dizer que quermos que seja no modo de escrever, e por ultimo passando qual a codificação no nosso arquivo, o f e para espicificar o nosso with open.
- Passando a funcao json.dump, vamos colocar as nossos dados vindo do nosso parametro o f que espicificar o nosso with open.


``` python




myJson = {
	'user': 'admin',
	'password': '12345'
}

generator(myJson)

```