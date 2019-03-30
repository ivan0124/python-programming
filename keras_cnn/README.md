## A Simple Neural Network in Keras + TensorFlow to classify the image Dataset

Following python packages are required to run this file:
<pre>
    sudo pip install scikit-learn
    sudo pip install keras
    sudo pip install imutils
    sudo pip install opencv-python
</pre>

# How to train model
<pre>
$ python train_network.py --dataset images --model santa_not_santa.model
</pre>

# How to test model
<pre>
$ python test_network.py --model santa_not_santa.model --image examples/santa_01.png
</pre>
