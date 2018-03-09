import keras
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from sklearn.preprocessing import MinMaxScaler
from random import randint
from numpy import array
from keras import backend as K
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Scaler is used to get all of our input between 0 and 1
scaler = MinMaxScaler(feature_range=(0,1))

training_samples = []
training_labels = []

'''
Generate 2000 training samples. Young is <= 45 and outputs a 0.
Old is > 45 and outputs a 1.
'''
for i in range(1000):
    young = randint(1,45) * 1.0
    training_samples.append(young)
    training_labels.append(0.0)

    old = randint(46,100) * 1.0
    training_samples.append(old)
    training_labels.append(1)

'''
Convert training samples and lables into numpy array
'''
training_samples = array(training_samples)
training_labels = array(training_labels)

'''
Scale the input between 0 and 1 using the scaler
'''
scaled_samples = scaler.fit_transform(training_samples.reshape(-1,1))
'''
Create the ML model.
The first layer is our input model so it requires an input shape.
    Because our input is 1 dimensional (a single integer)
    the input shape will be (1,)
    16 is the number of outputs? (Need to read docs)
The second layer is our hidden layer
    has 32 outputs and uses relu activation
The 3rd layer is our output layer
    has 2 outputs. 0 or 1.
    Uses softmax activation
'''
model = Sequential([
        Dense(16,input_shape=(1,),activation='relu'),
        Dense(32,activation='relu'),
        Dense(2,activation='softmax')
])

'''
Compile the model.
Adam is the optimizer and uses a learning rate of .001
    Another example of an optimizer is stochastic gradient descent (SGD)
Sparse Categorical Crossentropy is the type of loss. (Need to read the docs)
Metrics specifies how the model 'grades itself'.
    In this case I'm grading by accuracy
'''

model.compile(Adam(lr=.0001),loss='sparse_categorical_crossentropy',metrics=['accuracy'])

'''
Train the model with fit.
Scaled samples are our sample inputs
Training labels are our label for each input
Batch Size is how many it will select for each training episode
    Not quite sure how this works. A bath size of 32 was slower and less accurate than 10.
Epochs is how many training episodes we want
Shuffle means the input is randomly shuffled
verbose means that it will print out loss/acc for each epoch
'''
model.fit(scaled_samples, training_labels, batch_size = 10,epochs = 20, shuffle = True,verbose = 2)
K.clear_session()
