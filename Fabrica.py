import Formas

class cFabrica(object):	
	def getFormas(self,formas):
		if (formas == None):			
			print("No selecciono formas")
			return Formas.cVacia
		elif (formas == "Cuadrado"):
			print("Cuadro")
			return Formas.cCuadrado
		elif (formas == "circulo"):
			print("Circulo")
			return Formas.cCirculo
		elif (formas == "triangulo"):
			print("Triangulo")			
			return Formas.cTriangulo
		else:
			print("No hay formas")
			return Formas.cVacia
