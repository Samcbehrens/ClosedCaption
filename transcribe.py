import json 
from pprint import pprint
import sys 

def readJson(jsonFile):
	with open(jsonFile) as data_file:    
		data = json.load(data_file)

	print(data["keys"]["Google"]["key"])



if __name__ == "__main__":
	readJson(sys.argv[1])