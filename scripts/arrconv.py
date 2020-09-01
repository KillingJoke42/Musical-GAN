import pypianoroll as pipy
import numpy as np

def import_npz(fileptr):
	pianoroll = pipy.load(fileptr).get_stacked_pianoroll()[:128,:,4]
	pianoroll = pianoroll.reshape((128,128,1))
	return pianoroll

# def piano_conv(fileptr):
# 	pianoroll = np.load(fileptr)
# 	inst1 = list()
# 	track = 4

# 	inst1.append(pianoroll["pianoroll_%d_csc_data.npy"%track])
# 	inst1.append(pianoroll["pianoroll_%d_csc_indices.npy"%track])
# 	inst1.append(pianoroll["pianoroll_%d_csc_indptr.npy"%track])
# 	inst1.append(pianoroll["pianoroll_%d_csc_shape.npy"%track])

# 	#print(len(set(inst1[2])))
# 	"""
# 	inst1.append(range(1,12))
# 	inst1.append([5, 1, 6, 3, 3, 4, 5, 0, 5, 3, 5])
# 	inst1.append([0, 1, 1, 3, 4, 4, 4, 7, 8, 9, 9])
# 	#inst1.append([])
# 	"""
# 	piano_conv = list()
# 	new_row = np.full((1,11136), 128, dtype=np.uint8)

# 	tempstart = 0
# 	for i in range(inst1[2].shape[0]):
# 		if tempstart != inst1[2][i]:
# 			piano_conv.append(new_row)
# 			new_row = np.full((1,11136), 128, dtype=np.uint8)
# 			new_row[0][inst1[1][i]] = inst1[0][i]
# 			tempstart = inst1[2][i]
# 		else:
# 			new_row[0][inst1[1][i]] = inst1[0][i]

# 	#print(len(piano_conv))
# 	piano_conv = np.array(piano_conv)
# 	#print(piano_conv.shape)
	
# 	#assert(piano_conv.shape == inst1[3][::-1])

# 	return piano_conv

def main():
	pianoroll = import_npz("b97c529ab9ef783a849b896816001748.npz")
	print(pianoroll.shape)

if __name__ == "__main__":
	main()