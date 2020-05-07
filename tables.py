import json
import os

dirname = os.path.abspath(os.path.dirname(__file__))

tables=[] # unique tables in whole dataset (test+train+dev)
unique_columns=[] # unique columns in whole dataset (test+train+dev)
type_of={} # data type of each unique column

def analyse_tables(path):
""" analyse the number of tables, number and type of unique colums contained in path where each table is stored as a json object"""
	try:	
		with open(path) as f:
			for line in f: # each line in file corresponds to ob=ne json object
				table = json.loads(line)
				if table["id"] not in tables: # store only unique tables
					tables.append(table["id"])
				columns=table["header"]
				for column in columns: # store only unique columns
					if column not in unique_columns:
						unique_columns.append(column)
				types=table["types"]
				for i in range(0,len(types)): # store type of columns
					type_of[columns[i]]=types[i]
	except err:
		print(err)

			
		


def main():
	# for analysing tables present int train, test and dev set
	path = os.path.join(dirname, "./data/train.tables.jsonl")
	analyse_tables(path)

	path = os.path.join(dirname, "./data/test.tables.jsonl")
	analyse_tables(path)

	path = os.path.join(dirname, "./data/dev.tables.jsonl")
	analyse_tables(path)

	# to get count of total text and real columns
	total_text_columns=0
	total_real_columns=0

	for key in type_of.keys():
		if type_of[key] == 'text':
			total_text_columns+=1
		else:
			total_real_columns+=1

	# print the results		

	print("Total number of tables: ")
	print(len(tables))
	print("Total number of unique columns: ")
	print(len(unique_columns))
	print("Total number of text columns: ")
	print(total_text_columns)
	print("Total number of real columns: ")
	print(total_real_columns)

if __name__ == '__main__':
	main()


