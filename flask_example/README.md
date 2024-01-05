Projeto para validar aprendizagem 
no framework flask


** integrando com flask-pymongo

- iniciar uma instancia do mongo-db e colocar a url  no arquivo settings.toml
pra aplicacao ter comunicacao com o banco

- iniciar a aplicação WEB com o comando:
 flask run  (na pasta onde tá o arquivo app.py, que é a raiz do projeto) 


 # CLI
 o projeto tem uma cli com as principais funcionalidades facilitando assim a sua
 interação com projeto tambem via console. E possivel ver os principais comandos 
 na cli com: flask --help  dentro da pasta do projeto.

 - Principais usos:

LISTAGEM  -> flask posts lista-post-slug slug-do-post

ADD       -> flask posts novo-post --title "coruja azul" --content "hoje a coruja dormiu"

UPDATE    -> flask posts update slug-do-post --title "ja morant" --content "heartless"