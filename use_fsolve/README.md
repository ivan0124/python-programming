# use_fsolve sample code
The sample demo how to return the roots of the (non-linear) equations defined by func(x) = 0 given a starting estimate.
`ex: solve x^2-25=0 ==> root x=5`

#How to setup code environment
1. install `numpy` python module
<pre>
$ sudo apt-get install python-scipy
</pre>

#Code Description
1. import `fsolve` function: [use_fsolve.py](https://github.com/ivan0124/python-programming/blob/master/use_fsolve/use_fsolve.py)
<pre>
...
from scipy.optimize import fsolve
...
</pre>

2. implement equation `x^2-25=0`: [use_fsolve.py](https://github.com/ivan0124/python-programming/blob/master/use_fsolve/use_fsolve.py)
<pre>
...
def f(x):
       return x**2+1
...
</pre>

3. use `fsolve` to get roots `x`, starting estimate root is `3`: [use_fsolve.py](https://github.com/ivan0124/python-programming/blob/master/use_fsolve/use_fsolve.py)
<pre>
...
       x = fsolve(f,3)
       print x
...
</pre>

#How to test
1. run `use_fsolve.py` to test
