class IFormas(object):
	"""docstring for FormasTrigonometricas"""
	def conectar():
		print("Conectando una forma:..")
	def desconectar():
		print("Desconectando una forma:..")

class cCirculo(IFormas):
	"""docstring for Circulo"""	
	def conectar():
		print("Conectando a Circulo")
	def desconectar():
		print("Desconectando a Circulo")

class cCuadrado(IFormas):
	"""docstring for Circulo"""	
	def conectar():
		print("Conectando a Cuadrado")
	def desconectar():
		print("Desconectando a Cuadrado")

class cTriangulo(IFormas):
	"""docstring for Circulo"""	
	def conectar():
		print("Conectando a Triangulo")
	def desconectar():
		print("Desconectando a Triangulo")

class cVacia(IFormas):
	"""docstring for Vacio"""
	def conectar():
		print("Conectando a NAda")
	def desconectar():
		print("Desconectando a NAda")
		
