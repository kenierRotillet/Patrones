class IFormas(object):
	"""docstring for FormasTrigonometricas"""
	def conectar(self):
		print("Conectando una forma:..")
	def desconectar(self):
		print("Desconectando una forma:..")

class cCirculo(IFormas):
	"""docstring for Circulo"""	
	def conectar(self):
		print("Conectando a Circulo")
	def desconectar(self):
		print("Desconectando a Circulo")

class cCuadrado(IFormas):
	"""docstring for Circulo"""	
	def conectar(self):
		print("Conectando a Cuadrado")
	def desconectar(self):
		print("Desconectando a Cuadrado")

class cTriangulo(IFormas):
	"""docstring for Circulo"""	
	def conectar(self):
		print("Conectando a Triangulo")
	def desconectar(self):
		print("Desconectando a Triangulo")

class cVacia(IFormas):
	"""docstring for Vacio"""
	def conectar(self):
		print("Conectando a NAda")
	def desconectar(self):
		print("Desconectando a NAda")
		
