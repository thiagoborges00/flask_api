from application.database import mongo
from datetime import datetime
import pymongo


def get_all_posts(published: bool = True):
    
    return list(mongo.db.blog.posts.find({"published":published}))


def get_post_by_slug(slug: str) -> dict:
    '''retorna uma postou uma None'''
    post = mongo.db.blog.posts.find_one({"slug": slug})
    return post


def update_post_by_slug(slug: str,data: dict) -> dict:
    #TODO se o titulo mudar alterar o slug tbm
    
    return mongo.db.posts.find_one_and_update({"slug":slug}, {"$set": data})


def new_post(title: str, content: str, published: bool = True) -> str:
    slug = title.replace(" ", "-").replace("_", "-").lower()
    #mongo.db.blog.posts.find({})

    #TODO remover acentos
    #TODO garantir que o registro não existe

    try:
        mongo.db.posts.insert_one({
            "title": title,
            "content": content,
            "published": published,
            "slug": slug,
            "date_created": datetime.now(),

        })
    except pymongo.errors.ServerSelectionTimeoutError:
        return 'connection error, maybe you might connect mongodb .'
    except Exception as e:
        print(type(e))

    return slug


def exclude_post(slug: str):
    mongo.db.blog.posts.delete_one({"slug": {"$op": slug}})
