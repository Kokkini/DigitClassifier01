import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

import network
import pickle
step = 0.05
numEpoches = 10
net = network.Network((784,30,10))
fileName = 'netCrossEntropy.pickle'
file = open(fileName, 'wb')
pickle.dump(net, file)
file.close()
print("net created")
print("training started")
net.SGD_single(training_data, test_data, numEpoches, step)
file = open(fileName, 'wb')
pickle.dump(net, file)
file.close()