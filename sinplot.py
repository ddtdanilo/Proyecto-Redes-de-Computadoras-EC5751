from pylab import figure, show
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
ax1.plot(t,var)
ax1.grid(True)
ax1.set_ylim( (-2,2) )
ax1.set_ylabel('1 Hz')
ax1.set_title('A sine wave or two')

for label in ax1.get_xticklabels():
    label.set_color('r')


ax2 = fig.add_subplot(212)
ax2.plot(t, sin(2*2*pi*t))
ax2.grid(True)
ax2.set_ylim( (-2,2) )
l = ax2.set_xlabel('Hi mom')
l.set_color('g')
l.set_fontsize('large')

show()
