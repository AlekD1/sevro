import re
import datetime as dt


def make_dir_for_squad_main_image(instance, filename):
    return f'squads/{instance.name}/main_image/{filename}'

def make_dir_for_project_banner(instance, filename):
    return f'secondary/projects/{instance.title}/banner/{filename}'

def make_dir_for_project_images(instance, filename):
    path = instance.project.title if instance.project is not None else "image_wo_album"
    return f'secondary/projects/{path}/images/{filename}'

def make_dir_for_news_images(instance, filename):
    today = str(dt.date.today())
    return f'news/{today}-{instance.title}/images/{filename}'

def make_dir_for_links(instance, filename):
    link = re.split('https://|http://', instance.url)[1].replace('/', '-')
    return f'links/{link}/images/{filename}'

def make_dir_for_album(instance, filename):
    return f'albums/{instance.name}/banner/{filename}'

def make_dir_for_album_images(instance, filename):
    path = instance.album.name if instance.album is not None else "image_wo_album"
    return f'albums/{path}/images/{filename}'

def make_dir_for_partner_image(instance, filename):
    return f'partners/{instance.name}/{filename}'
