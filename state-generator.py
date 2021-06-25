import csv
import pandas as pd
from _datetime import datetime as dt
import numpy as np
import json
#print(dt.now())
#: districtid, timeid, neighbormean, neighborstdev
data_file_week = open('state-week.csv', 'w', newline="")
csv_writer_week = csv.writer(data_file_week)
header_week = ['districtid','weekid','statemean','statestdev']
csv_writer_week.writerow([header_week[0], header_week[1], header_week[2],header_week[3]])
start_date = dt.date(dt.strptime('15/03/2020', '%d/%m/%Y'))
start_date_weeknum = start_date.strftime("%U")
end_date=dt.date(dt.strptime('05/09/2020', '%d/%m/%Y'))
end_date_weeknum=end_date.strftime("%U")
start_date_monthnum = start_date.strftime("%m")
end_date_monthnum=end_date.strftime("%m")

data_weekwise=pd.DataFrame(pd.read_csv("case-week.csv"))
data_monthwise=pd.DataFrame(pd.read_csv("case-month.csv"))
dictionary={}
dictionary_month={}
for i in range(len(data_weekwise)):
    districtid=data_weekwise.loc[i,'districtid']
    weekid=data_weekwise.loc[i,'weekid']
    cases=data_weekwise.loc[i,'cases']
    if districtid in dictionary:
        dictionary[districtid][weekid]=cases
    else:
        dictionary[districtid]={weekid:cases}

for i in range(len(data_monthwise)):
    districtid=data_monthwise.loc[i,'districtid']
    monthid=data_monthwise.loc[i,'monthid']
    cases=data_monthwise.loc[i,'cases']
    if districtid in dictionary_month:
        dictionary_month[districtid][monthid]=cases
    else:
        dictionary_month[districtid]={monthid:cases}

#print(dictionary_month)
data_file_month = open('state-month.csv', 'w', newline="")
csv_writer_month = csv.writer(data_file_month)

header_month = ['districtid','monthid','statemean','statestdev']
csv_writer_month.writerow([header_month[0], header_month[1], header_month[2],header_month[3]])

data_file_year = open('state-overall.csv', 'w', newline="")
csv_writer_year = csv.writer(data_file_year)
header_year = ['districtid','overallid','statemean','statestdev']
csv_writer_year.writerow([header_year[0], header_year[1], header_year[2],header_year[3]])



data_overall=pd.DataFrame(pd.read_csv("case-overall.csv"))
state_data=pd.DataFrame(pd.read_csv("district_state_data.csv"))
list_state=[628,132,244,299,465,665,210]#[299,132,667,296,630,244,466,210]#[668,131,297,631,241,467,208,466]#465,132,299,244,665,210,
for distid in state_data['districtid']:
    #print(distid)
    statename = state_data.loc[state_data['districtid'] == distid, 'state'].iloc[0]
    #print(statename)
    group_bystate=state_data.groupby('state')
    state_neighbor=list(group_bystate.get_group(statename)['districtid'])
    #state_neighbor = list(state_data.loc[state_data['state'] == statename, 'districtid'])
    for week_id in range(1, int(end_date_weeknum) - int(start_date_weeknum) + 2):
        list_week_cases=[]
        for stateid in state_neighbor:
            if distid==stateid and stateid not in list_state:
                continue
            else:
                cases=int(dictionary[stateid][week_id])
                list_week_cases.append(cases)

        week_std = float(np.std(list_week_cases).round(decimals=2))
        week_mean = float(np.mean(list_week_cases).round(decimals=2))
        csv_writer_week.writerow([distid, week_id, week_mean, week_std])

    for month_id in range(1, int(end_date_monthnum) - int(start_date_monthnum) + 2):
        list_month_cases=[]
        for statedistid in state_neighbor:
            if distid == statedistid and statedistid not in list_state:
                continue
            else:
                cases = int(dictionary_month[statedistid][month_id])
                list_month_cases.append(cases)
        if len(list_month_cases)==0:
            print(distid)
        month_std=float(np.std(list_month_cases).round(decimals=2))
        month_mean=float(np.mean(list_month_cases).round(decimals=2))
        csv_writer_month.writerow([distid,month_id,month_mean,month_std])
    list_overall_cases=[]
    for statedistid in state_neighbor:
    #for neighborid in edge_data.loc[edge_data['districtid'] == distid, 'neighbor_districtid']:
        #print(type(statedistid),type(distid))
        if distid==statedistid and statedistid not in list_state:
            continue
        else:
            list_overall_cases.append(int(data_overall[((data_overall['overallid'] == 1) & (data_overall['districtid'] == statedistid))]['cases']))
    overall_std = float(np.std(list_overall_cases).round(decimals=2))
    overall_mean = float(np.mean(list_overall_cases).round(decimals=2))
    csv_writer_year.writerow([distid, 1, overall_mean, overall_std])

data_file_week.close()
data_file_month.close()
data_file_year.close()
#print(dt.now())

