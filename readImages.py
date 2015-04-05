import struct
import numpy as np
lab_file = "train-labels-idx1-ubyte"
img_file = "train-images-idx3-ubyte"

def main():
	readBinaryImgFile(img_file)

def readBinaryLabelFile(fn):
	f = open(fn, "rb")
	magic = struct.unpack('>I', f.read(4))[0]
	num_items = struct.unpack('>I', f.read(4))[0]
	bin_lab = f.read()
	labels = [struct.unpack('B', lab)[0] for lab in bin_lab]
	assert(len(labels) == num_items)
	assert(magic == 2049)
	f.close()

def readBinaryImgFile(fn):
	f = open(fn, "rb")
	magic = struct.unpack('>I', f.read(4))[0]
	num_items = struct.unpack('>I', f.read(4))[0]
	rows = struct.unpack('>I', f.read(4))[0]
	cols = struct.unpack('>I', f.read(4))[0]
	imgs = [struct.unpack('B', byte)[0] for byte in f.read()]


	np.reshape(imgs,(num_items,cols,rows))

if __name__ == "__main__":
	main()
