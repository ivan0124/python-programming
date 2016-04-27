# use_fsolve sample code
The sample demo how to solve functon.
`ex: solve 3x+1=0 ==> x=1/3`

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

2. implement function `3x+1=0`
<pre>
...
def f(x):
       return 3*x+1
...
</pre>

3. use `fsolve` to get x solution:
<pre>
...
       x = fsolve(f,1)
       print x
...
</pre>

#How to test
1. run `use_fsolve.py` to test
