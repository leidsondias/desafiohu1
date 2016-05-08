### Instalação

Para instalar o projetoe suas dependências e popular o banco você deve rodar o comando abaixo:

```sh
$ make install
```
Além dos requirements é instalado um pacote do NodeJS, o *corsproxy* para rodar dois servidores com domínios diferentes na mesma máquina.

### Rodando projeto
Para rodar os dois servidores basta executar o comando:
```sh
$ make run
```

Os servidores irão rodar nas seguintes portas:
- 8000 - Site
- 5000 - API
- 1337 - Proxy

Algumas vezes ao parar o processo *make run* no terminal nem todos os processos são parados. Basta rodar a seguinte linha para que pare todos os processos parem:
```sh
$ kill -9 $(lsof -ti tcp:8000) & kill -9 $(lsof -ti tcp:5000) & kill -9 $(lsof -ti tcp:1337)
```

### Demais comandos

- Comando para realizar teste: ***make test***
- Comando para limpar banco: ***make drop***
- Comando para criar banco: ***make create***
- Comando para recriar banco: ***make recreate***
- Comando para popular banco: ***make load_data***
- Comando para limpar os arquivos temporários de python (pyc): ***make clean***

### Bibliotecas

* [corsproxy]
* [AngularJS]
* [Flask]
* [Flask-RESTful]
* [Flask-Script]
* [Flask-SQLAlchemy]
* [serpy]

### Versão
1.0.0

### Autor
[Leidson Dias] - @[linkedin], @[github]

[corsproxy]: <https://www.npmjs.com/package/corsproxy>
[AngularJS]: <https://angularjs.org/>
[Flask]: <http://flask.pocoo.org/>
[Flask-RESTful]: <http://flask-restful-cn.readthedocs.io/>
[Flask-Script]: <https://flask-script.readthedocs.io/en/latest/>
[Flask-SQLAlchemy]: <http://flask-sqlalchemy.pocoo.org/2.1/>
[serpy]: <https://github.com/clarkduvall/serpy>
[Leidson Dias]: <http://www.leidsondias.com.br>
[linkedin]: <https://br.linkedin.com/in/leidsondias>
[github]: <https://github.com/leidsondias>

# Desafio de auto-complete e busca disponibilidade

Neste problema você deve implementar o widget de busca de hoteis. Este desenvolvimento engloba o auto-complete de hoteis e a busca por disponibilidades quando o usuário informa um periodo de estadia. 

A interface em anexo precisa ser implementada assim como o backend para consumir a lista de hoteis e as disponibilidades. Tudo será avaliado. Faça o seu melhor na linguagem onde vc possui o maior domínio.

***Restrições***
* Eu preciso conseguir rodar seu código no mac os x OU no ubuntu;
* Eu vou executar seu código com os seguintes comandos:

>1. *git clone seu-fork*
2. *cd seu-fork*
3. *comando para instalar dependências*
4. *comando para executar a aplicação*

Esses comandos tem que ser o suficiente para configurar meu mac os x OU ubuntu e rodar seu programa. Pode considerar que eu tenho instalado no meu sistema Python, Java, PHP, Ruby, Android, iOS e/ou Node. Qualquer outra dependência que eu precisar vc tem que prover.

***Performance***
* Preciso que os seus serviços suportem um volume de 1000 requisições por segundo

***Artefatos***
* Imagens e database de hoteis e disponibilidades estão na pasta arquivos
