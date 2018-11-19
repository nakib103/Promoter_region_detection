from Bio import SeqIO
import numpy as np
import os
from sys import exit

dataDir = "C:\\Users\\Snakib\\Dropbox\\thesisMSC\\Genomic\\promoter\\data"
humanNonTataPosDir = os.path.join(dataDir, "human_non_tata.fa")
dataDir = "C:\\Users\\Snakib\\Dropbox\\thesisMSC\\Genomic\\promoter\\data"
humanNonTataNegDir = os.path.join(dataDir, "human_nonprom_big.fa")

trainPosDataLen = int(19811*0.8)
trainNegDataLen = int(27731*0.8)
trainDataLen = trainPosDataLen + trainNegDataLen
testPosDataLen = 19811 - trainPosDataLen
testNegDataLen = 27731 - trainNegDataLen
testDataLen = testPosDataLen + testNegDataLen

trainData = np.zeros((trainDataLen, 251, 4))
testData = np.zeros((testDataLen, 251, 4))
trainDataLabel = np.zeros((trainDataLen, 2)) 
testDataLabel = np.zeros((testDataLen, 2)) 

for i in range(trainDataLen):
	if (i < trainPosDataLen):
		trainDataLabel[i][0] = 1
	else:
		trainDataLabel[i][1] = 1
for i in range(testDataLen):
	if (i < testPosDataLen):
		testDataLabel[i][0] = 1
	else:
		testDataLabel[i][1] = 1

for seqNo, entry in enumerate(SeqIO.parse(humanNonTataPosDir, "fasta")):
		name, sequence = entry.id, str(entry.seq)

		for base, i in enumerate(sequence):
			if (seqNo < trainPosDataLen):
				if( i == 'A'):
					trainData[seqNo][base][0] = 1
					continue
				elif( i == 'T'):
					trainData[seqNo][base][1] = 1
					continue
				elif( i == 'G'):
					trainData[seqNo][base][2] = 1
					continue
				else:
					trainData[seqNo][base][3] = 1
			else:
				if( i == 'A'):
					testData[seqNo - trainPosDataLen][base][0] = 1
					continue
				elif( i == 'T'):
					testData[seqNo - trainPosDataLen][base][1] = 1
					continue
				elif( i == 'G'):
					testData[seqNo - trainPosDataLen][base][2] = 1
					continue
				else:
					testData[seqNo - trainPosDataLen][base][3] = 1

for seqNo, entry in enumerate(SeqIO.parse(humanNonTataNegDir, "fasta")):
		name, sequence = entry.id, str(entry.seq)

		for base, i in enumerate(sequence):
			if (seqNo < trainNegDataLen):
				if( i == 'A'):
					trainData[seqNo + trainPosDataLen][base][0] = 1
					continue
				elif( i == 'T'):
					trainData[seqNo + trainPosDataLen][base][1] = 1
					continue
				elif( i == 'G'):
					trainData[seqNo + trainPosDataLen][base][2] = 1
					continue
				else:
					trainData[seqNo + trainPosDataLen][base][3] = 1
			else:
				if( i == 'A'):
					testData[testPosDataLen + seqNo - trainNegDataLen][base][0] = 1
					continue
				elif( i == 'T'):
					testData[testPosDataLen + seqNo - trainNegDataLen][base][1] = 1
					continue
				elif( i == 'G'):
					testData[testPosDataLen + seqNo - trainNegDataLen][base][2] = 1
					continue
				else:
					testData[testPosDataLen + seqNo - trainNegDataLen][base][3] = 1

rng_state = np.random.get_state()
np.random.shuffle(trainData)
np.random.set_state(rng_state)
np.random.shuffle(trainDataLabel)

rng_state = np.random.get_state()
np.random.shuffle(testData)
np.random.set_state(rng_state)
np.random.shuffle(testDataLabel)

np.save('C:\\Users\\Snakib\\Dropbox\\thesisMSC\\Genomic\\promoter\\data\\humanNonTatatrain', trainData)
np.save('C:\\Users\\Snakib\\Dropbox\\thesisMSC\\Genomic\\promoter\\data\\humanNonTatatrainLabel', trainDataLabel)
np.save('C:\\Users\\Snakib\\Dropbox\\thesisMSC\\Genomic\\promoter\\data\\humanNonTatatest', testData)
np.save('C:\\Users\\Snakib\\Dropbox\\thesisMSC\\Genomic\\promoter\\data\\humanNonTatatestLabel', testDataLabel)