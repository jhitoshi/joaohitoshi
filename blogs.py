from bottle import *
from datetime import date, datetime
from Mensagem import Mensagem
from usuario import usuario 
import csv
import sqlite3

conn = sqlite3.connect('banco.db')
c = conn.cursor()

c.execute('''
	create table if not exists usuario(
		id_usuario integer primary key autoincrement,
		nome text,
		senha text,
		username text);
	''')
conn.commit()
c.execute('''

	create table if not exists Mensagem(
		id_Mensagem integer primary key autoincrement,
		titulo text,
		conteudo text,
		date text,
		destinatario integer,
		usuario integer,
		foreign key (destinatario) references usuario(id_usuario),
		foreign key (usuario) references usuario(id_usuario));
	''')
conn.commit()

# try:			
# 	file = open('', 'r')
# 	file.close()
# except FileNotFoundError:
# 	file = open('msgs.csv', 'w')
# 	fields = ['titulo', 'conteudo',  'destinatario', 'usuario', 'date']
# 	writer = csv.DictWriter(file, fieldnames=fields)
# 	writer.writeheader()
# 	file.close()

# try:
# 	usuarios = open('lista_usuarios.csv', 'r')
# 	usuarios.close()
# except FileNotFoundError:
# 	usuarios = open('lista_usuarios.csv', 'w')
# 	fields = ['username', 'senha']
# 	writer = csv.DictWriter(usuarios, fieldnames = fields)
# 	writer.writeheader()
# 	usuarios.close()


mensagens = []
mensagens_Sel = []
mensagens_enviadas = []

def Novo_User():
	global usuarios, senha


def save_mensagens():
	global mensagens_enviadas
	with open("msgs.csv", "a", encoding='utf-8') as f:
		fields = ['titulo', 'conteudo',  'destinatario', 'usuario', 'date']
		writer = csv.DictWriter(f, fieldnames=fields)
		writer.writerow({'titulo': msg.titulo, 'conteudo': msg.conteudo, 'destinatario': msg.destinatario, 'usuario': msg.usuario, 'date': msg.date})

username = ''
password = ''

@route('/')
def login():
	username = ''
	return template('login_msg')


@post('/')
def verificar():
	global username, password
	username = request.forms.get('user')
	password = request.forms.get('pass')

	for user in usuario.readAll_usuario():
		if user.username == username and user.senha == password:
			return redirect('/inbox/')		
	text = 'Senha Errada' + '<a href = "/"> Voltar! </a>' + 'ou' + '<a href = "/cadastro/"> Cadastre-se </a>'
	return text

	
@route('/inbox/')
def inbox():
	global mensagens
	mensagens.clear()
	MSG = Mensagem.readAll_Mensagem()
	for msg in MSG:
		if msg.destinatario == username:
			mensagens.append(msg)
	return template('caixa', mensagens=mensagens, username = username)

@route('/Minhas_Mensagens/')
def Minhas():
	global mensagens, usuario
	mensagens.clear()
	mensagens = Mensagem.Read_Some(username)
	return template('Minhas', mensagens = mensagens, username = username)



@route('/cadastro/')
def cadastro():
	return template('Novo_User')

@post('/cadastro/')
def usuario_cadastrar():
	global novo_usuario, nova_senha
	novo_nome = request.forms.get('novo_nome')
	novo_usuario = request.forms.get('novo_user')
	nova_senha = request.forms.get('novo_pass')
	usuario.create_usuario(novo_usuario, nova_senha, novo_nome)
	return redirect('/')



@route('/nova_mensagem/')
def nova_msg():
	return template('nova_mensagem', mensagens = mensagens)

@post('/nova_mensagem/')
def nova_msg_post():
	global msg, username
	titulo = request.forms.titulo
	destinatario = request.forms.destinatario
	conteudo = request.forms.conteudo
	conn = sqlite3.connect('banco.db')
	c = conn.cursor()
	query = f"select * from usuario where username = '{destinatario}'"
	c.execute(query)
	dados = c.fetchall()
	if not dados:
		return redirect('/inbox/')
	destinatario = dados[0][0]

	query = f"select * from usuario where username = '{username}'"
	c.execute(query)
	dados = c.fetchall()
	userid = dados[0][0]

	Mensagem.create_Mensagem(titulo, conteudo, str(datetime.now()), str(destinatario), str(userid))
	return redirect('/inbox/')

@route('/mensagem/<id1:int>')
def mensagem(id1):
	mensagem = mensagens[id1]
	return template('mensagem_tpl', mensagem=mensagem, mensagens=mensagens)

@route('/upMensagem/<id1:int>/')
def mensagen(id1):
	global mensagens_Sel
	mensagens_Sel = mensagens[id1]
	print('test')
	return template('update', mensagem=mensagens_Sel, mensagens = mensagens)

@post('/Update/')
def UpdateMSG():
	titulo = request.forms.titulo
	conteudo = request.forms.conteudo
	Mensagem.update_Mensagem(mensagens_Sel.id_Mensagem, titulo, conteudo)
	redirect('/Minhas_Mensagens/')

@route('/static/<file_path:path>')
def static_path(file_path):
	main_dir = os.path.dirname(__file__)
	rel_path = "static/"
	abs_path = os.path.join(main_dir, rel_path)
	return static_file(file_path, root=abs_path)

@route('/delete_msg/')
def delete_msg():
	Mensagem.delete_Mensagem(mensagens_Sel.id_Mensagem)
	redirect('/Minhas_Mensagens/')


run(reloader=True, interval = 1)
