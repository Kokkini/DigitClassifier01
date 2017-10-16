import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

print(validation_data[0][0]*256)