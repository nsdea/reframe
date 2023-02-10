import flask
import wikipedia
import wikipediaapi

from .. import system

frame_bp = flask.Blueprint('frame_bp', __name__, template_folder='../')

@frame_bp.route('/')
def home():
    return flask.render_template('reframe/templates/home.html')

@frame_bp.route('/wiki/<title>')
def article_page(title):
    article = wikipediaapi.Wikipedia('en', extract_format=wikipediaapi.ExtractFormat.HTML).page(title)
    content = article.text

    return flask.render_template('reframe/templates/article.html', title=title, content=content)

@frame_bp.route('/wiki/Special:Search')
def search():
    query = flask.request.args.get('search')
    results = wikipedia.search(query)
    return flask.render_template('reframe/templates/results.html', query=query, results=results)
