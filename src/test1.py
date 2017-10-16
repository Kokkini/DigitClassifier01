import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

import network_blackAndWhite as network
import pickle

net = network.Network((784,30,10))
fileName = 'netBW.pickle'
file = open(fileName, 'wb')
pickle.dump(net, file)
file.close()
net.SGD_single(training_data, 0.1)
print net.evaluate(test_data)
file = open(fileName, 'wb')
pickle.dump(net, file)
file.close()