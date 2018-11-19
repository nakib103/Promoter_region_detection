from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv1D, MaxPool1D
from keras.losses import categorical_crossentropy
from keras import metrics
from keras.optimizers import Adam
import numpy as np

# *** some possible improvement - add dropout layer

# X_train = np.load('C:\\Users\\Snakib\\Dropbox\\thesisMSC\\Genomic\\promoter\\data\\humanNonTatatrain.npy')
# Y_train = np.load('C:\\Users\\Snakib\\Dropbox\\thesisMSC\\Genomic\\promoter\\data\\humanNonTatatrainLabel.npy')
X_train = np.load('/input/humanNonTatatrain.npy')
Y_train = np.load('/input/humanNonTatatrainLabel.npy')
X_test = np.load('/input/humanNonTatatest.npy')
Y_test = np.load('/input/humanNonTatatestLabel.npy')

input_shape = (251, 4)
model = Sequential()
model.add(Conv1D(filters = 300, kernel_size = 21, activation = 'relu', padding = 'valid', input_shape = input_shape))      
model.add(MaxPool1D(pool_size = 2))
model.add(Flatten())            	
model.add(Dense(units = 128, activation = 'relu')) 
model.add(Dense(units = 2, activation = 'sigmoid'))  

model.compile(loss = categorical_crossentropy, optimizer = Adam(lr = 0.0001, decay = 0.0), metrics = ['accuracy', metrics.categorical_accuracy])

batch_size = 16
epochs = 25

model.fit(X_train, Y_train, batch_size = batch_size, epochs = epochs, verbose = 2, validation_split = 0.125)

model.evaluate(X_test, Y_test, batch_size=16, verbose=2, sample_weight=None, steps=None)

json_string = model.save('/output/promoter.h5') 