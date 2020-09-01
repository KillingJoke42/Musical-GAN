import numpy as np
from arrconv import import_npz
import os

def import_dataset(filepath):
	filecount = 0
	dataset = list()
	for subdir, dirs, files in os.walk(filepath):
		if filecount != 6000:
			for file in files:
				try:
					pianoroll = import_npz(os.path.join(subdir, file))
					dataset.append(pianoroll)
					filecount += 1
					del(pianoroll)
				except Exception as e:
					print(e)
	dataset = np.array(dataset)
	print(dataset.shape)
	return dataset

def main():
	import_dataset("D:/musnn_dataset/lpd_5/lpd_5_cleansed")

if __name__ =="__main__":
	main()