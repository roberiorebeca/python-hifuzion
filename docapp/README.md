# Aplicação de Controle de Documentos

Essa aplicação tem por objetivo controlar documentos na web por cliente e endereço parecido com um sistema de almoxarifado

## Divisão da Aplicação

* api: Controle da aplicação backend, será feito com python e django
* web: Controle da aplicação web, será feito com javascript com VueJS
* doc: Documentação da aplicação

## Requisitos:

| Tecnologia | Versão |
|---|---|
| Python | 3.7.3 |
| NodeJS | 10.15.3|
| Yarn | 1.15.2|
| Django |2.1|
| VueCLI |3.5.3|

OBS.: Para controlar os pacotes do python vamos utilizar o pipenv

Pacotes de Produção

```bash
pipenv install django python-decouple dj-database-url django-cors-headers django-extensions django-filter django-rest-auth djangorestframework
```
Pacotes de Desenvolvimento
``` bash
pipenv install -d sqlformatter notebook
```