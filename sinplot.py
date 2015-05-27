#from pylab import figure, show
from numpy import arange, sin, pi
import string

t = arange(0.0, 1.0, 0.01)

fig = figure(1)

ax1 = fig.add_subplot(211)
var=sin(2*pi*t)
varstr=str(var)
newstr = varstr.replace("[", "")
newstr = newstr.replace("]", "")
var = [float(s) for s in newstr.split()] 



def empaquetar(float_array):
	varstr = str(float_array).encode()
	return varstr

def desempaquetar(byte_array):
	varstr = byte_array.decode()
	newstr = varstr.replace("[", "")
	newstr = newstr.replace("]", "")
	var = [float(s) for s in newstr.split()]
	return var


