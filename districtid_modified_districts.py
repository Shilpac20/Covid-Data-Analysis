#this program is used to give district id to each district in neighbor-districts-modified.json
import json
import csv
with open('neighbor-districts-modified.json',encoding='utf-8') as f:
  data = json.load(f)

data_file = open('modified_neighbor_districts.csv', 'w+',newline='',encoding='utf-8')
csv_writer = csv.writer(data_file)

count = 100

header_index=['districtid','districtname']
for d in sorted(data.keys()):
    if count == 100:
        csv_writer.writerow([header_index[0],header_index[1]])

    count += 1
    csv_writer.writerow([count,d])

data_file.close()
