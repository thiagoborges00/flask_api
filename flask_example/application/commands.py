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

@posts.command()
@click.argument("slug")
def lista_post_slug(slug):
    '''List one post by slug'''

    if not slug:
        click.echo(message="Type slug ...\n")
        return False
    post = get_post_by_slug(slug=slug)
    if post is None:
        click.echo("Post inexistent .. ")
        return False
    click.echo(post)

@posts.command()
@click.argument("slug")
@click.option("--content", default=None, type=str)
@click.option("--published", default='true', type=str)
def update(slug, content, published):
    '''Update post by slug. Ex.
    flask posts update slug-do-post --title "ja morant" --content "heartless"'''
    data = {}
    if not content or not published:
        click.echo("Type something ...")
        return False
    
    data["content"]= content,
    data["published"]= published.lower()
    
    post = update_post_by_slug(slug=slug, data=data)
    click.echo(f"Post updated, {post}, {data},{slug}\n")
