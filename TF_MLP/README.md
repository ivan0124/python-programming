#How to setup TensorFlow environment ( for Ubuntu 14.04 64bit/single CPU)
Tutorial

https://www.tensorflow.org/versions/r0.10/get_started/os_setup.html

2. install pip
<pre>
# Ubuntu/Linux 64-bit
$ sudo apt-get install python-pip python-dev
</pre>

3. export path
<pre>
# Ubuntu/Linux 64-bit, CPU only, Python 2.7
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.3.0-cp27-none-linux_x86_64.whl
</pre>

4. install TensorFlow
<pre>
# Python 2
$ sudo pip install --upgrade $TF_BINARY_URL
</pre>

5. install other dependencies
<pre>
# For Python 2.7:
$ sudo apt-get install python-pandas python-numpy swig python-dev python-wheel
$ sudo pip install pandas
$ sudo apt-get install libfreetype6-dev libpng-dev
$ sudo pip install matplotlib
</pre>


# How to use Test
1. run `tf_mlp.py`, then you will see the test result

# How to run TensorBoard
1.tensorboard --logdir ./logs/

2.Launch browser and go to http://127.0.0.1:6006
