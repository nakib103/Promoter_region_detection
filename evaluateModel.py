import numpy as np
from keras.models import Sequential, model_from_json
import matplotlib.pyplot as plt
import numpy as np
from random import randint

model = model_from_json('promDet.json')# if json 
# model = model_from_yaml(open('my_model_architecture.yaml').read())# if yaml 
model.load_weights('promWeight.h5')

#print(model.summary())

# x = np.load('E:\\library of EEE\\4-2\\eee 426\\data\\MSCprojectDataBase\\floydDataset\\DRIVEtrainData.npy')
# y = np.load('E:\\library of EEE\\4-2\\eee 426\\data\\MSCprojectDataBase\\floydDataset\\DRIVEtrainDataLabel.npy')
# y = (y / 255).astype('int')
x = np.load('C:\\Users\\Snakib\\Dropbox\\thesisMSC\\Genomic\\promoter\\data\\humanNonTatatest.npy')
y = np.load('C:\\Users\\Snakib\\Dropbox\\thesisMSC\\Genomic\\promoter\\data\\humanNonTatatestLabel.npy')

model.evaluate(x, y, batch_size=16, verbose=2, sample_weight=None, steps=None)