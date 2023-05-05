from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask (__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234' 
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/contatos', methods=['GET','POST'])
def contatos():
		if request.method == 'POST':
				email = request.form['email']
				assunto = request.form['assunto']
				descricao = request.form['descricao']

				cur = mysql.connection.cursor()
				cur.execute(f'INSERT INTO CONTATO (EMAIL,ASSUNTO,DESCRICAO) VALUES ({email},{assunto},{descricao})')
				
				mysql.commit()

				cur.close()

				return 'Sucesso'
				