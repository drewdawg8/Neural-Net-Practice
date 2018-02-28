from numpy import *
import numpy as np

X = array(([44,43],
            [3,5],
            [34,6],
            [8,6],
            [2,8]),dtype=float)
y = array(([87],
            [8],
            [40],
            [14],
            [10]),dtype = float)

X = X/100
y = y/100
random.seed(1)
class NeuralNetwork:

    def __init__(self):
        self.outputsize = 1
        self.inputsize = 2
        self.hiddensize = 3
        self.W1 = random.random((self.inputsize,self.hiddensize))
        self.W2 = random.random((self.hiddensize, self.outputsize))


    def train(self,X,y):

        o = self.forward(X)
        self.backward(X,y,o)


    def forward(self, X):
            self.z = dot(X,self.W1)
            self.z2 = self.sigmoid(self.z)
            self.z3 = dot(self.z2, self.W2)
            o = self.sigmoid(self.z3)
            return o

    def backward(self,X,y,o):
        self.o_error = y - o
        self.o_delta = self.o_error * self.sigmoidPrime(o)

        self.z2_error = self.o_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)

        self.W1 += X.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.o_delta)

    def sigmoid(self,X):
        return 1/(1+exp(-X))

    def sigmoidPrime(self,x):
        return x * (1-x)

NN = NeuralNetwork()

for i in range(100000):
    NN.train(X,y)

print("Input\n" + str(X))
print("ActualOutput\n" + str(y))
output = np.round(multiply((NN.forward(X)),100))
print("Predicted Output:\n" + str(output))
print("\n")
output2 = (multiply(NN.forward(array([40,3])/100),100))
print("New Output:\n" + str(output2))
