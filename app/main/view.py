from flask import render_template
from . import main
from ..request import get_sources, get_articles
from ..models import Sources


@main.route('/')
def index():
    title = "Welcome to the News page."

    general = get_sources('general')
    technology = get_sources('technology')
    business = get_sources('business')
    health = get_sources('health')
    entertainment = get_sources('entertainment')
    sports = get_sources('sports')

    return render_template('index.html', title=title, general=general, technology=technology, business=business, health=health, entertainment=entertainment, sports=sports
                           )


@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    Function that returns articles based on their sources
    '''
    news_source = get_articles(source_id)
    title = 'Articles | News Articles'
    return render_template('articles.html', title=title, name=source_id, news=news_source)
