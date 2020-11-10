import csv
import requests

csv_url = input("Give csv's url: ")
request = requests.get(csv_url)
url_content = request.content
csv_name = input("Give csv's name: ")
csv_file = open(csv_name+".csv", 'wb')
csv_file.write(url_content)
csv_file.close()
