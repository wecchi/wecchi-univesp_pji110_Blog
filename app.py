import warnings

from flask import Flask, render_template, request, url_for, flash, redirect
import os, datetime
import sqlite3

# Com usar o jinja:		 https://jinja2docs.readthedocs.io/en/stable/templates.html#
# Mais detalhes do blog: https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

# A ferramenta SQLAlchemy é utilizada como mapeamento objeto-relacional da aplicação. 
# Repare que nos conectamos ao banco sem o uso dela, e após a criação das tabelas, inserimos a biblioteca e criamos a classe correspondente.
from flask_sqlalchemy import SQLAlchemy
# Exibir erros caso a postagem não exista
from werkzeug.exceptions import abort

# Ignorar mensagens de Warning
warnings.filterwarnings("ignore")

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))
thisyear = datetime.datetime.now().strftime("%Y")

app = Flask('__name__')
app.config['SECRET_KEY'] = 'm-$?8JqzA6eK_dja-SN3'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


class Posts(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	title = db.Column(db.String(80), nullable=False)
	content = db.Column(db.String(600), nullable=False)
		

# Quando a URL for root rodar a função index
@app.route('/')
def index():
	# conn = get_db_connection()
	# posts = conn.execute('SELECT * FROM posts').fetchall()
	posts = Posts.query.all()
	# conn.close()
	return render_template('index.html', posts=posts, thisyear=thisyear)


def get_post(post_id):
	post = Posts.query.filter_by(id=post_id).first()
	if post is None:
		abort(404)
	return post



# Renderiza detalhes de uma postagem
@app.route('/<int:post_id>')
def post(post_id):
	post = get_post(post_id)
	return render_template('post.html', post=post)



# Renderiza a página "Sobre"
@app.route('/about')
def about():
	return render_template('about.html', thisyear=thisyear)



# Renderiza a criação/salvamento de uma nova postagem
@app.route('/create', methods=('GET', 'POST'))
def create():
	if request.method == 'POST':
		title = request.form['title']
		content = request.form['content']

		if not title:
			flash('O título é obrigatório!')
		else:
			post = Posts(title=title, content=content)
			db.session.add(post)
			db.session.commit()
			return redirect(url_for('index'))

	return render_template('create.html')



# Edição de uma postagem
@app.route('/<int:post_id>/edit', methods=('GET', 'POST'))
def edit(post_id):
	# recupera a postagem pelo id
	post = get_post(post_id)

	# Caso esteja gravando a edição (post)
	if request.method == 'POST':
		title = request.form['title']
		content = request.form['content']

		if not title:
			flash('Título é obrigatório!!')
		else:
			post.title = title
			post.content = content
			db.session.commit()
			return redirect(url_for('index'))

	# Caso contrário, renderiza a chamada no template de edição
	else:
		return render_template('edit.html', post=post)


# Exclusão de uma postagem
@app.route('/<int:post_id>/delete', methods=('POST',))
def delete(post_id):
	# recupera a postagem pelo id
	post = get_post(post_id)
	db.session.delete(post)
	db.session.commit()
	flash('"{}" foi apagado com sucesso!'.format(post.title))

	return redirect(url_for('index'))