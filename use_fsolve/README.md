# use_fsolve sample code
The sample demo how to return the roots of the (non-linear) equations defined by func(x) = 0 given a starting estimate.
`ex: solve x^2-25=0 ==> x=5`

#How to setup code environment
1. install `numpy` python module
<pre>
$ sudo apt-get install python-scipy
</pre>

#Code Description
1. import `fsolve` function
<pre>
...
from scipy.optimize import fsolve
...
</pre>

2. implement equation `x^2-25=0`
<pre>
...
def f(x):
       return x**2+1
...
</pre>

3. use `fsolve` to get roots `x`, starting estimate root is `1`:
<pre>
...
       x = fsolve(f,1)
       print x
...
</pre>

#How to test
1. run `use_fsolve.py` to test
