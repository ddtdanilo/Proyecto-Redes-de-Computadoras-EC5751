from pylab import figure, show
from numpy import arange, sin, pi
import string

def empaquetar(float_array):
	varstr = str(float_array).encode()
	return varstr

def desempaquetar(byte_array):
	varstr = byte_array.decode()
	newstr = varstr.replace("[", "")
	newstr = newstr.replace("]", "")
	var = [float(s) for s in newstr.split()]
	return var

def plotSignal(tEjeY,tPrincipal,Color,Data):
	
	fig = figure(1)
	ax1 = fig.add_subplot(211)
	var = Data
	ax1.plot(t,var)
	ax1.grid(True)
	ax1.set_ylim( (-2,2) )
	ax1.set_ylabel('1 Hz')
	ax1.set_title('A sine wave or two')
	for label in ax1.get_xticklabels():
	    label.set_color(Color)
	show()



t = arange(0.0, 1.0, 0.01)
var=sin(2*pi*t+pi/2)

varbyte=empaquetar(var)

var2 = desempaquetar(varbyte)
print(len(var2))

plotSignal("Eje Y","Título",'r',var2)







