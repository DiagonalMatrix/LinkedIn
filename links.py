import csv
from config import csv_filepath
#from url_helper import url_checker
import sys

linkedin_urls = []
linkedin_degrees_second = []
linkedin_degrees_third = []


with open(csv_filepath,'r') as f:
    try:
        reader = csv.reader(f,delimiter=str(sys.argv[1]))
    except Exception as e:
        reader = csv.reader(f)
    print(reader)
    header =next(reader)
    for row in reader:
        linkedin_url = row[0] # Adjust column if needed
        linkedin_degree_second = row[1]
        linkedin_degree_third = row[2]
        if len(linkedin_url):
            #linkedin_url = url_checker(linkedin_url)
            print(linkedin_url)
            linkedin_urls.append(linkedin_url)
            linkedin_degrees_second.append(linkedin_degree_second)
            linkedin_degrees_third.append(linkedin_degree_third)
        else:
            print('# ' + row[0] + ' ' + row[1] + "'s linkedin is blank")
