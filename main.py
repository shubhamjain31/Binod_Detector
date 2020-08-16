import os

def isBinod(filename):
	with open(filename,'r') as f:
		fileContent = f.read()

	#detect all forms of binod like biNod
	if "binod" in fileContent.lower():
		return True
	else:
		return False

if __name__ == '__main__':

	#listing the contents of the folder
	dir_contents = os.listdir()
	
	nBinod = 0
	#for each text file, run isBinod for them
	for file in dir_contents:
		if file.endswith('txt'):
			print(f'Detecting Binod in {file}')
			flag = isBinod(file)
			if flag:
				print(f'Binod found in {file}')
				nBinod += 1
			else:
				print(f'Binod not found in {file}')

	print("\nBinod Detector Summary")
	print(f'{nBinod} files found with hidden into them')