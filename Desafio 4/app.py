from flask import Flask, render_template, request
import mysql.connector

app = Flask (__name__)

mysql = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '1234',
database = 'DESAFIO4'
)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/contatos', methods=['GET','POST'])
def contatos():
		if request.method == 'POST':
			email = request.form['email']
			assunto = request.form['assunto']
			descricao = request.form['descricao']

			cur = mysql.connection.cursor(buffered=True)
			cur.execute('INSERT INTO CONTATOS (EMAIL,ASSUNTO,DESCRICAO) VALUES (%s,%s,%s)', (email, assunto, descricao))
				
			mysql.connection.commit()

			cur.close() 	 	

			return 'Sucesso'
		return render_template('contatos.html')

@app.route('/users')
def users():
	cur = mysql.connection.cursor(buffered=True)

	users = cur.execute("SELECT * FROM contatos")

	if users > 0:
		userDetails = cur.fetchall()

	return render_template("users.html", userDetails=userDetails)