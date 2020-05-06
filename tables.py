import json
import os

dirname = os.path.abspath(os.path.dirname(__file__))


def analyse_tables():
	
	total_tables=0
	total_text_columns=0
	total_real_columns=0
	unique_column_names=0
	avg_table_columns=0
	avg_table_rows=0


	with open("/home/chrome/Desktop/wiki_sql_analsis/data/dev.tables.jsonl") as f:
		for line in f:
			j = json.loads(line)
			print(j)
analyse_tables()