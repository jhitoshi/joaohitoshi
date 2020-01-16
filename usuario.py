
import sqlite3
class usuario(object):
	def __init__(self, username, senha, nome):
		self.username = username
		self.senha = senha
		self.nome = nome



	def __str__(self):
		return self.username + "," + self.nome + "," + self.senha
		
	@staticmethod
	def create_usuario(username, senha, nome):
		query = "insert into usuario (username, senha, nome)values('"+username + "','" + senha + "','" + nome + "')"
		conn = sqlite3.connect('banco.db')
		c = conn.cursor()
		c.execute(query)
		conn.commit()

	@staticmethod
	def readAll_usuario():
		lst = []
		conn = sqlite3.connect('banco.db')
		c = conn.cursor()
		query = "select * from usuario"
		c.execute(query)
		dados = c.fetchall()
		for dado in dados:
			user = usuario(dado[3], dado[2], dado[1]) 
			lst.append(user)

		return lst

	@staticmethod
	def update_usuario(username, nome, senha):
		conn = sqlite3.connect('banco.db')
		c = conn.cursor()
		query = f'update usuario set nome = "{nome}", senha = "{senha}" where username = "{username}"'
		c.execute(query)
		conn.commit()

	@staticmethod
	def delete_usuario(username):
		query = f"delete from usuario where username = '{username}'"
		conn = sqlite3.connect('banco.db')
		c = conn.cursor()
		c.execute(query)
		conn.commit()
