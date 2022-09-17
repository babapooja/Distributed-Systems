import os
import time 

file_name = "int.txt"

# method to read content from file - Opening text file in read mode
def check_file_content():
	file1 = open(file_name, 'r')
	time.sleep(.1)
	file_value = int(file1.read())
	file1.flush()
	file1.close()
	return file_value

# method to increment counter and write back to file - Opening text file in write mode
def read_write_file():
	file_content = check_file_content()
	file_content+=1
	print('{0} printing {1} to file.'.format(os.getpid(), file_content))
	file1 = open(file_name, 'w')
	file1.write(file_content.__str__())
	file1.flush()
	file1.close()

# main method to be executed
def parent_child():
	# loop to create 3 processes P1, P2, P3
	for process in range(1,4):
		# fork call to create a child process
		pid = os.fork()
		if pid==0:
			# execute the file read and increment count till the number in the file is < 500
			while check_file_content()<500:
				print("created process #{0}: {1} ".format(process, os.getpid()))
				read_write_file()	
	os._exit(0)

# method call	
parent_child()

