import csv
import pandas as pd
from _datetime import datetime as dt
import numpy as np
import json
#print(dt.now())
#: districtid, timeid, neighbormean, neighborstdev
data_file_week = open('method-spot-week.csv', 'w', newline="")
csv_writer_week = csv.writer(data_file_week)
header_week = ['weekid','method','spot','districtid']
csv_writer_week.writerow([header_week[0], header_week[1], header_week[2],header_week[3]])
start_date = dt.date(dt.strptime('15/03/2020', '%d/%m/%Y'))
start_date_weeknum = start_date.strftime("%U")
end_date=dt.date(dt.strptime('05/09/2020', '%d/%m/%Y'))
end_date_weeknum=end_date.strftime("%U")
start_date_monthnum = start_date.strftime("%m")
end_date_monthnum=end_date.strftime("%m")

data_file_month = open('method-spot-month.csv', 'w', newline="")
csv_writer_month = csv.writer(data_file_month)

header_month = ['monthid','method','spot','districtid']
csv_writer_month.writerow([header_month[0], header_month[1], header_month[2],header_month[3]])

data_file_year = open('method-spot-overall.csv', 'w', newline="")
csv_writer_year = csv.writer(data_file_year)
header_year = ['yearid','method','spot','districtid']
csv_writer_year.writerow([header_year[0], header_year[1], header_year[2],header_year[3]])



data_neighbor_weekwise=pd.DataFrame(pd.read_csv("neighbor-week.csv"))
data_neighbor_monthwise=pd.DataFrame(pd.read_csv("neighbor-month.csv"))
data_neighbor_overall=pd.DataFrame(pd.read_csv("neighbor-overall.csv"))

data_state_weekwise=pd.DataFrame(pd.read_csv("state-week.csv"))
data_state_monthwise=pd.DataFrame(pd.read_csv("state-month.csv"))
data_state_overall=pd.DataFrame(pd.read_csv("state-overall.csv"))

data_case_weekwise=pd.DataFrame(pd.read_csv("case-week.csv"))
data_case_monthwise=pd.DataFrame(pd.read_csv("case-month.csv"))
data_case_overall=pd.DataFrame(pd.read_csv("case-overall.csv"))

for i in range(len(data_neighbor_weekwise)):
    districtid=data_neighbor_weekwise.loc[i,'districtid']
    week_id=data_neighbor_weekwise.loc[i,'weekid']
    neighmean=data_neighbor_weekwise.loc[i,'neighbormean']#,neighborstdev
    neighstdev=data_neighbor_weekwise.loc[i,'neighborstdev']
    casecount=data_case_weekwise.loc[i,'cases']
    statemean = data_state_weekwise.loc[i, 'statemean']
    statestdev = data_state_weekwise.loc[i, 'statestdev']
    spot='None'
    if casecount>neighmean+neighstdev:
        spot='hotspot'
    elif casecount< neighmean-neighstdev:
        spot='coldspot'
    if spot=='None':
        continue
    else:
        csv_writer_week.writerow([week_id,'neighbor',spot,districtid])
    spot='None'
    if casecount > statemean + statestdev:
        spot = 'hotspot'
    elif casecount < statemean - statestdev:
        spot = 'coldspot'
    if spot == 'None':
        continue
    else:
        csv_writer_week.writerow([week_id, 'state', spot, districtid])
for i in range(len(data_neighbor_monthwise)):
    districtid=data_neighbor_monthwise.loc[i,'districtid']
    month_id=data_neighbor_monthwise.loc[i,'monthid']
    neighmean=data_neighbor_monthwise.loc[i,'neighbormean']#,neighborstdev
    neighstdev=data_neighbor_monthwise.loc[i,'neighborstdev']
    casecount=data_case_monthwise.loc[i,'cases']
    statemean = data_state_monthwise.loc[i, 'statemean']
    statestdev = data_state_monthwise.loc[i, 'statestdev']
    spot='None'
    if casecount>neighmean+neighstdev:
        spot='hotspot'
    elif casecount< neighmean-neighstdev:
        spot='coldspot'
    if spot=='None':
        continue
    else:
        csv_writer_month.writerow([month_id,'neighbor',spot,districtid])
    spot = 'None'
    if casecount > statemean + statestdev:
        spot = 'hotspot'
    elif casecount < statemean - statestdev:
        spot = 'coldspot'
    if spot == 'None':
        continue
    else:
        csv_writer_month.writerow([month_id, 'state', spot, districtid])
for i in range(len(data_neighbor_overall)):
    districtid=data_neighbor_overall.loc[i,'districtid']
    year_id=data_neighbor_overall.loc[i,'overallid']
    neighmean=data_neighbor_overall.loc[i,'neighbormean']#,neighborstdev
    neighstdev=data_neighbor_overall.loc[i,'neighborstdev']
    statemean = data_state_overall.loc[i, 'statemean']
    statestdev = data_state_overall.loc[i, 'statestdev']
    casecount=data_case_overall.loc[i,'cases']
    spot='None'
    if casecount>neighmean+neighstdev:
        spot='hotspot'
    elif casecount<= neighmean-neighstdev:
        spot='coldspot'
    if spot=='None':
        continue
    else:
        csv_writer_year.writerow([year_id,'neighbor',spot,districtid])
    spot = 'None'
    if casecount > statemean + statestdev:
        spot = 'hotspot'
    elif casecount < statemean - statestdev:
        spot = 'coldspot'
    if spot == 'None':
        continue
    else:
        csv_writer_year.writerow([year_id, 'state', spot, districtid])
data_file_week.close()
data_file_month.close()
data_file_year.close()
#print(dt.now())

district_data_week=pd.DataFrame(pd.read_csv("method-spot-week.csv"))
group_data = district_data_week.sort_values(['weekid','method','spot'], ascending=[True,True,False])
group_data.to_csv("method-spot-week.csv",index=False)

district_data_month=pd.DataFrame(pd.read_csv("method-spot-month.csv"))
group_data = district_data_month.sort_values(['monthid','method','spot'], ascending=[True,True,False])
group_data.to_csv("method-spot-month.csv",index=False)

district_data_overall=pd.DataFrame(pd.read_csv("method-spot-overall.csv"))
group_data = district_data_overall.sort_values(['yearid','method','spot'], ascending=[True,True,False])
group_data.to_csv("method-spot-overall.csv",index=False)

