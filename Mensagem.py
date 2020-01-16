from datetime import date, datetime
import sqlite3

class Mensagem(object):
	def __init__(self, id_Mensagem, titulo, conteudo, destinatario, usuario, date=datetime.now()):
		self.id_Mensagem = id_Mensagem
		self.titulo = titulo
		self.destinatario = destinatario
		self.usuario = usuario
		self.conteudo = conteudo
		if isinstance(date,datetime):
			self.date = date.strftime('%d/%m/%y %H:%M' )
		else:
			self.date = date


	@staticmethod
	def create_Mensagem(titulo, conteudo, date, destinatario, usuario):
		query = "insert into Mensagem (titulo, conteudo, date, destinatario, usuario)values('"+titulo + "','" + conteudo + "','" + date + "','" + destinatario + "','" + usuario + "')"
		conn = sqlite3.connect('banco.db')
		c = conn.cursor()
		c.execute(query)
		conn.commit()

	@staticmethod
	def readAll_Mensagem():
		lst = []
		conn = sqlite3.connect('banco.db')
		c = conn.cursor()
		query = "select * from Mensagem"
		c.execute(query)
		dados = c.fetchall()
		for dado in dados:
			print(dado)
			query = "select * from usuario where id_usuario = " + str(dado[4])
			b = conn.cursor()
			b.execute(query)
			aux = b.fetchall()
			if not aux:
				continue
			destinatario = aux[0][3]
			query = "select * from usuario where id_usuario = " + str(dado[5])
			a = conn.cursor()
			a.execute(query)
			aux = a.fetchall()
			if not aux:
				continue
			usuario = aux[0][3]
			MSG = Mensagem(dado[0], dado[1], dado[2], destinatario, usuario, date = dado[3])
			lst.append(MSG)
		return lst

	@staticmethod
	def Read_Some(usuario):
		lst = []
		conn = sqlite3.connect('banco.db')
		c = conn.cursor()
		query = f'select * from Mensagem,usuario where Mensagem.usuario = usuario.id_usuario and usuario.username = "{usuario}"'
		c.execute(query)
		conn.commit()
		dados = c.fetchall()
		for dado in dados:
			query = "select * from usuario where id_usuario = " + str(dado[4])
			b = conn.cursor()
			b.execute(query)
			aux = b.fetchall()
			if not aux:
				continue
			destinatario = aux[0][3]
			MSG = Mensagem(dado[0], dado[1], dado[2], destinatario, usuario, date = dado[3])
			lst.append(MSG)

		return lst

	@staticmethod
	def update_Mensagem(id_Mensagem,titulo, conteudo):
		conn = sqlite3.connect('banco.db')
		c = conn.cursor()
		query = f'update Mensagem set titulo = "{titulo}", conteudo = "{conteudo}" where id_Mensagem = "{id_Mensagem}"'
		c.execute(query)
		conn.commit()

	@staticmethod
	def delete_Mensagem(id_Mensagem):
		query = f"delete from Mensagem where id_Mensagem = '{id_Mensagem}'"
		conn = sqlite3.connect('banco.db')
		c = conn.cursor()
		c.execute(query)
		conn.commit()