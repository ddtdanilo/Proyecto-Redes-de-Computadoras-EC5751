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



t = arange(0.0, 1.0, 0.01)

fig = figure(1)

ax1 = fig.add_subplot(211)
var=sin(2*pi*t)
varbyte=empaquetar(var)
print(varbyte)
var2 = desempaquetar(varbyte)
ax1.plot(t,var2)
ax1.grid(True)
ax1.set_ylim( (-2,2) )
ax1.set_ylabel('1 Hz')
ax1.set_title('A sine wave or two')

for label in ax1.get_xticklabels():
    label.set_color('r')




show()




