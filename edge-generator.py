import json
import csv
import pandas as pd
#from collections import OrderedDict

with open('neighbor-districts-modified.json') as f:
  data = json.load(f)
data_file = open('edge-graph.csv', 'w',newline="")
csv_writer = csv.writer(data_file)
#ordered_data=OrderedDict(sorted(data.items()))
district_data=pd.DataFrame(pd.read_csv("modified_neighbor_districts.csv"))


header_index=['districtid','neighbor_districtid']
csv_writer.writerow([header_index[0],header_index[1]])

for node in data:
    district_1=district_data.loc[district_data['districtname'] == node, 'districtid'].iloc[0]

    for edge in data[node][0]['neighbor']:
        district_2 = district_data.loc[district_data['districtname'] == edge, 'districtid'].iloc[0]
        if int(district_1)<int(district_2): #if district_1 has greater id than district_2 that means that edge has already been added so I do not write that edge again in csv
            csv_writer.writerow([district_1,district_2])

data_file.close()
district_data_edge=pd.DataFrame(pd.read_csv("edge-graph.csv"))
district_data_edge=district_data_edge.sort_values(['districtid','neighbor_districtid'], ascending=[True,True])
district_data_edge.to_csv('edge-graph.csv',index=False)