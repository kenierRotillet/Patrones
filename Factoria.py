class Formas(object):
	"""docstring for FormasTrigonometricas"""
	def conectar(self):
		print("Conectando una forma:..")
	def desconectar(self):
		print("Desconectando una forma:..")

class Circulo(Formas):
	"""docstring for Circulo"""	
	def conectar(self):
		print("Conectando a Circulo")
	def desconectar(self):
		print("Desconectando a Circulo")

class Cuadrado(Formas):
	"""docstring for Circulo"""	
	def conectar(self):
		print("Conectando a Cuadrado")
	def desconectar(self):
		print("Desconectando a Cuadrado")

class Triangulo(Formas):
	"""docstring for Circulo"""	
	def conectar(self):
		print("Conectando a Triangulo")
	def desconectar(self):
		print("Desconectando a Triangulo")

