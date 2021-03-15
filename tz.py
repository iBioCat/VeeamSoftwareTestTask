import sys
import hashlib
import os

def check_hash(file_path,method,given_hashsum):														#проверка, совпадают ли заданная контрольная и фактическая
	if method == "md5":
				current_file = open(file_path,'rb').read()
				hashsum = hashlib.md5(current_file)
				if given_hashsum == hashsum.hexdigest():
					result = "OK"
				else:
					result = "FAIL"
	elif method == "sha1":
				current_file = open(file_path,'rb').read()
				hashsum = hashlib.sha1(current_file)
				if given_hashsum == hashsum.hexdigest():
					result = "OK"
				else:
					result = "FAIL"
	elif method == "sha256":
				current_file = open(file_path,'rb').read()
				hashsum = hashlib.sha256(current_file)
				if given_hashsum == hashsum.hexdigest():
					result = "OK"
				else:
					result = "FAIL"
	return result

def check_files(filename,dir_path):																	#открытие файла, форматирование информации
	f = open(filename, encoding="utf-8")
	for line in f:
		current_info = line.split()
		if os.path.exists(dir_path + current_info[0]):
			result = check_hash(dir_path + current_info[0],current_info[1],current_info[2])
			print(current_info[0],result)
		else:
			print(current_info[0],"NOT FOUND")


def main():																							#вызов функции с исходными данными
	check_files(sys.argv[1],sys.argv[2])															

if __name__ =="__main__":
	main()