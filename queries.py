import json
import os


agg_ops = ['', 'MAX', 'MIN', 'COUNT', 'SUM', 'AVG'] # aggregation operators in sql queries

dirname = os.path.abspath(os.path.dirname(__file__))

def analyse_queries(path,set_name):
	""" get the total number of queries and the number of queries having different aggregators specified in agg_opps"""
	
	json_queries=[] 
	aggregator_counts=[0 for i in range(6)] # aggregator_counts[i] represents count of queries in the file path having aggregrator agg_ops[i] 
	
	try:
		with open(path) as f:
			for line in f:
				if line!=None:
					json_query = json.loads(line)
					json_queries.append(json_query)
	except err:
		print(err)

	# to get the number of queries having each type of aggregator
	for query in json_queries:
		aggregator_counts[query["sql"]["agg"]]+=1
	
	total_queries=len(json_queries)


	# print results for each set
	print(set_name)
	
	print("Total number of queries",end="")
	print(len(json_queries))
	
	print("Number of queries with no aggregator")
	print(aggregator_counts[0])
	
	print("Number of queries with max aggregator")
	print(aggregator_counts[1])
	
	print("Number of queries with min aggregator")
	print(aggregator_counts[2])
	
	print("Number of queries with count aggregator")
	print(aggregator_counts[3])
	
	print("Number of queries with sum aggregator")
	print(aggregator_counts[4])
	
	print("Number of queries with avg aggregator")
	print(aggregator_counts[5])

	

def main():
	# for analysing queries present int train, test and dev set
	path = os.path.join(dirname, "./data/train.jsonl")
	analyse_queries(path,"Train set")

	path = os.path.join(dirname, "./data/test.jsonl")
	analyse_queries(path,"Test set")

	path = os.path.join(dirname, "./data/dev.jsonl")
	analyse_queries(path,"Dev set")


if __name__ == '__main__':
	main()


	