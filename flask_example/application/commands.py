#apos finalizar as operacoes de controllers
#add elas para o cli
from application.posts import *
import click


def configure(app):
    app.cli.add_command(posts)


#criando um grupo para exibicao das funcionalidades na cli
@click.group()
def posts():
    '''Management of posts (CRUD)'''


@posts.command()
@click.option("--title")
@click.option("--content")
def novo_post(title, content):
    '''Add new post to database. Ex.
    flask posts novo-post --title "testecli" --content "casa banca com mel"
    '''
    if not title or not content:
        click.echo(message="Params obrigated...",err=True)
        return False
    newest_post = new_post(title=title, content=content)
    click.echo(f"New post Created!\n Slug: {newest_post}") 