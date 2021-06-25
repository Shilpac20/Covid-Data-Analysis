import csv
import pandas as pd
from _datetime import datetime as dt
import numpy as np
import json
#print(dt.now())
#: districtid, timeid, neighbormean, neighborstdev
data_file_week = open('zscore-week.csv', 'w', newline="")
csv_writer_week = csv.writer(data_file_week)
header_week = ['districtid','weekid','neighborhoodzscore','statezscore']
csv_writer_week.writerow([header_week[0], header_week[1], header_week[2],header_week[3]])
start_date = dt.date(dt.strptime('15/03/2020', '%d/%m/%Y'))
start_date_weeknum = start_date.strftime("%U")
end_date=dt.date(dt.strptime('05/09/2020', '%d/%m/%Y'))
end_date_weeknum=end_date.strftime("%U")
start_date_monthnum = start_date.strftime("%m")
end_date_monthnum=end_date.strftime("%m")

data_file_month = open('zscore-month.csv', 'w', newline="")
csv_writer_month = csv.writer(data_file_month)

header_month = ['districtid','monthid','neighborhoodzscore','statezscore']
csv_writer_month.writerow([header_month[0], header_month[1], header_month[2],header_month[3]])

data_file_year = open('zscore-overall.csv', 'w', newline="")
csv_writer_year = csv.writer(data_file_year)
header_year = ['districtid','overallid','neighborhoodzscore','statezscore']
csv_writer_year.writerow([header_year[0], header_year[1], header_year[2],header_year[3]])


data_state_weekwise=pd.DataFrame(pd.read_csv("state-week.csv"))
data_state_monthwise=pd.DataFrame(pd.read_csv("state-month.csv"))
data_state_overall=pd.DataFrame(pd.read_csv("state-overall.csv"))

data_neighbor_weekwise=pd.DataFrame(pd.read_csv("neighbor-week.csv"))
data_neighbor_monthwise=pd.DataFrame(pd.read_csv("neighbor-month.csv"))
data_neighbor_overall=pd.DataFrame(pd.read_csv("neighbor-overall.csv"))

data_case_weekwise=pd.DataFrame(pd.read_csv("case-week.csv"))
data_case_monthwise=pd.DataFrame(pd.read_csv("case-month.csv"))
data_case_overall=pd.DataFrame(pd.read_csv("case-overall.csv"))

for i in range(len(data_state_weekwise)):
    districtid=data_state_weekwise.loc[i,'districtid']
    week_id=data_state_weekwise.loc[i,'weekid']
    statemean=data_state_weekwise.loc[i,'statemean']
    statestdev=data_state_weekwise.loc[i,'statestdev']
    neighmean=data_neighbor_weekwise.loc[i,'neighbormean']#,neighborstdev
    neighstdev=data_neighbor_weekwise.loc[i,'neighborstdev']
    casecount=data_case_weekwise.loc[i,'cases']
    if neighstdev==0:
        neighzscore=0
    else:
        neighzscore=float(((casecount-neighmean)/neighstdev).round(decimals=2))
    if statestdev==0:
        statezscore=0
    else:
        statezscore=float(((casecount-statemean)/statestdev).round(decimals=2))
    csv_writer_week.writerow([districtid,week_id,neighzscore,statezscore])
for i in range(len(data_state_monthwise)):
    districtid=data_state_monthwise.loc[i,'districtid']
    month_id=data_state_monthwise.loc[i,'monthid']
    statemean=data_state_monthwise.loc[i,'statemean']
    statestdev=data_state_monthwise.loc[i,'statestdev']
    neighmean=data_neighbor_monthwise.loc[i,'neighbormean']#,neighborstdev
    neighstdev=data_neighbor_monthwise.loc[i,'neighborstdev']
    casecount=data_case_monthwise.loc[i,'cases']
    if neighstdev==0:
        neighzscore=0
    else:
        neighzscore=float(((casecount-neighmean)/neighstdev).round(decimals=2))
    if statestdev==0:
        statezscore=0
    else:
        statezscore=float(((casecount-statemean)/statestdev).round(decimals=2))
    csv_writer_month.writerow([districtid,month_id,neighzscore,statezscore])
for i in range(len(data_state_overall)):
    districtid=data_state_overall.loc[i,'districtid']
    year_id=data_state_overall.loc[i,'overallid']
    statemean=data_state_overall.loc[i,'statemean']
    statestdev=data_state_overall.loc[i,'statestdev']
    neighmean=data_neighbor_overall.loc[i,'neighbormean']#,neighborstdev
    neighstdev=data_neighbor_overall.loc[i,'neighborstdev']
    casecount=data_case_overall.loc[i,'cases']
    if neighstdev==0:
        neighzscore=0
    else:
        neighzscore=float(((casecount-neighmean)/neighstdev).round(decimals=2))
    if statestdev==0:
        statezscore=0
    else:
        statezscore=float(((casecount-statemean)/statestdev).round(decimals=2))
    csv_writer_year.writerow([districtid,year_id,neighzscore,statezscore])
data_file_week.close()
data_file_month.close()
data_file_year.close()
#print(dt.now())

