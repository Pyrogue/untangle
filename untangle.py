#!/usr/bin/python3.4
#This untangles images.

#will have several algorithms
#some will allow the mapping to not be a function, colors going to multiple spots, or nowhere

def brute(uscr, scr, puzzle):
	"""
	Searches entire image for colors, does not stop at first find.
	accepts:
		training files: unscrambled, scrambled
		file to unscramble
	returns unscrambled file
	"""
	return 

def arrize(png):
	"""
	reads png into numpy array
	https://pythonhosted.org/pypng/ex.html#png-to-numpy-array-reading
	"""
	return numpy.vstack(itertools.imap(numpy.uint16, pngdata))

def main():
	#request and open files
	filename=["Unscrambled file:","Scrambled file:","File to unscramble:"]
	print("Unscrambled file:")
	filename[0] = input()
	print("Scrambled file:")
	filename[1] = input()
	print("File to unscramble:")
	filename[2] = input()

	#choose algorythm
	print("Brute: B")
	algorithm = input()

	#open files, convert to arrrays

	#run algorithm

main()