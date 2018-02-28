import numpy as np
from numpy import exp

class Layer:
    def __init__(self,numNeurons,numInput):
        self.weights = 2 * np.random.random((numInput,numNeurons)) - 1

class NeuralNet:

    def __init__(self,inputs,layer1,layer2):

        self.layer1 = layer1
        self.layer2 = layer2
        #self.syn1 = 2*np.random.random((4,1)) - 1
        self.inputs = inputs


    def train(self,outputs):
        for j in range(1000):
            layer1Output, layer2Output = self.predict(self.inputs)

            layer2Error = (outputs - layer2Output)
            layer2Delta = layer2Error * self.tanh(layer2Output,True)

            layer1Error = layer2Delta.dot(self.layer2.weights.T)
            layer1Delta = layer1Error * self.tanh(layer1Output,True)

            layer1Adjust = self.inputs.T.dot(layer1Delta)
            layer2Adjust = layer1Output.T.dot(layer2Delta)

            self.layer1.weights += layer1Adjust
            self.layer2.weights += layer2Adjust
            #print(self.layer1)

    def nonlin(self,x,deriv=False): #(0,1)
        #x -= max(x)
        if(deriv == True):
            return x*(1-x)
        return 1/(1+np.exp(-x))

    def tanh(self,x,deriv = False): #[-1,1]
        function = 2 * (self.nonlin(2*x)) - 1
        if(deriv):
            return 1 - (function**2)
        return function




    def predict(self,inputs):
        output1 = self.tanh(np.dot(inputs, self.layer1.weights))
        output2 = self.tanh(np.dot(output1,self.layer2.weights))
        return output1, output2


def main():
    np.random.seed(1)
    training_set_inputs = np.array([[0,0,1], # 1 = 1
                                    [1,1,0], #0 = 0
                                    [1,0,1], #-1 = 2
                                    [0,0,0],
                                    [1,0,0],
                                    [0,1,0]])

    training_set_outputs = np.array([[1,
                                    -1,
                                    -1,
                                    0,
                                    1,
                                    1]]).T

    #print(inputs.shape)
    layer1 = Layer(4, 3)
    layer2 = Layer(1, 4)
    neural = NeuralNet(training_set_inputs,layer1,layer2)
    neural.train(training_set_outputs)

    print("New situation:")
    hidden_state, output = neural.predict(np.array([0,0,0]))
    print(output)

main()
