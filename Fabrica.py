import Formas

class cFabrica(object):	
	def getFormas(self,formas):
		if (formas == None):			
			print("No selecciono formas")
			return Formas.cVacia
		elif (formas == "Cuadrado"):
			print("Selecciono un cuadro")
			return Formas.cCuadrado
		elif (formas == "circulo"):
			print("Selecciono un circulo")
			return Formas.cCirculo
		elif (formas == "triangulo"):
			print("Selecciono un triangulo")
			return Formas.cTriangulo
		else:
			print("No hay formas")
			return Formas.cVacia
