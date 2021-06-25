import csv
import pandas as pd
from _datetime import datetime as dt

data_file_week = open('top-week.csv', 'w', newline="")
csv_writer_week = csv.writer(data_file_week)
header_week = ['weekid','method','spot','districtid1','districtid2','districtid3','districtid4','districtid5']
csv_writer_week.writerow([header_week[0], header_week[1], header_week[2],header_week[3],header_week[4],header_week[5],header_week[6],header_week[7]])
start_date = dt.date(dt.strptime('15/03/2020', '%d/%m/%Y'))
start_date_weeknum = start_date.strftime("%U")
end_date=dt.date(dt.strptime('05/09/2020', '%d/%m/%Y'))
end_date_weeknum=end_date.strftime("%U")
start_date_monthnum = start_date.strftime("%m")
end_date_monthnum=end_date.strftime("%m")

data_file_month = open('top-month.csv', 'w', newline="")
csv_writer_month = csv.writer(data_file_month)

header_month = ['monthid','method','spot','districtid1','districtid2','districtid3','districtid4','districtid5']
csv_writer_month.writerow([header_month[0], header_month[1], header_month[2],header_month[3],header_month[4],header_month[5],header_month[6],header_month[7]])

data_file_year = open('top-overall.csv', 'w', newline="")
csv_writer_year = csv.writer(data_file_year)
header_year = ['yearid','method','spot','districtid1','districtid2','districtid3','districtid4','districtid5']
csv_writer_year.writerow([header_year[0], header_year[1], header_year[2],header_year[3],header_year[4],header_year[5],header_year[6],header_year[7]])

data_weekwise=pd.DataFrame(pd.read_csv("zscore-week.csv"))
data_monthwise=pd.DataFrame(pd.read_csv("zscore-month.csv"))
data_overall=pd.DataFrame(pd.read_csv("zscore-overall.csv"))

for weekid in range(1, int(end_date_weeknum) - int(start_date_weeknum) + 2):
    data_week=pd.DataFrame(data_weekwise.loc[data_weekwise['weekid']==weekid])
    data_hotspot_distid_list=list(data_week.nlargest(5,['neighborhoodzscore'])['districtid'])
    data_coldspot_distid_list=list(data_week.nsmallest(5,['neighborhoodzscore'])['districtid'])
    csv_writer_week.writerow([weekid,'neighbor','hotspot',data_hotspot_distid_list[0],data_hotspot_distid_list[1],data_hotspot_distid_list[2],data_hotspot_distid_list[3],data_hotspot_distid_list[4]])
    csv_writer_week.writerow([weekid,'neighbor','coldspot',data_coldspot_distid_list[0],data_coldspot_distid_list[1],data_coldspot_distid_list[2],data_coldspot_distid_list[3],data_coldspot_distid_list[4]])
    data_hotspot_distid_list_state = list(data_week.nlargest(5, ['statezscore'])['districtid'])
    data_coldspot_distid_list_state = list(data_week.nsmallest(5, ['statezscore'])['districtid'])
    csv_writer_week.writerow([weekid, 'state', 'hotspot', data_hotspot_distid_list_state[0], data_hotspot_distid_list_state[1],
                              data_hotspot_distid_list_state[2], data_hotspot_distid_list_state[3], data_hotspot_distid_list_state[4]])
    csv_writer_week.writerow([weekid, 'state', 'coldspot', data_coldspot_distid_list_state[0], data_coldspot_distid_list_state[1],
         data_coldspot_distid_list_state[2], data_coldspot_distid_list_state[3], data_coldspot_distid_list_state[4]])


for month_id in range(1, int(end_date_monthnum) - int(start_date_monthnum) + 2):
    data_month=pd.DataFrame(data_monthwise.loc[data_monthwise['monthid']==month_id])
    data_hotspot_distid_list=list(data_month.nlargest(5,['neighborhoodzscore'])['districtid'])
    data_coldspot_distid_list = list(data_month.nsmallest(5, ['neighborhoodzscore'])['districtid'])
    csv_writer_month.writerow([month_id, 'neighbor', 'hotspot', data_hotspot_distid_list[0], data_hotspot_distid_list[1],
                              data_hotspot_distid_list[2], data_hotspot_distid_list[3], data_hotspot_distid_list[4]])
    csv_writer_month.writerow(
        [month_id, 'neighbor', 'coldspot', data_coldspot_distid_list[0], data_coldspot_distid_list[1],
         data_coldspot_distid_list[2], data_coldspot_distid_list[3], data_coldspot_distid_list[4]])
    data_hotspot_distid_list_state = list(data_month.nlargest(5, ['statezscore'])['districtid'])
    data_coldspot_distid_list_state = list(data_month.nsmallest(5, ['statezscore'])['districtid'])
    csv_writer_month.writerow(
        [month_id, 'state', 'hotspot', data_hotspot_distid_list_state[0], data_hotspot_distid_list_state[1],
         data_hotspot_distid_list_state[2], data_hotspot_distid_list_state[3], data_hotspot_distid_list_state[4]])
    csv_writer_month.writerow(
        [month_id, 'state', 'coldspot', data_coldspot_distid_list_state[0], data_coldspot_distid_list_state[1],
         data_coldspot_distid_list_state[2], data_coldspot_distid_list_state[3], data_coldspot_distid_list_state[4]])

data_hotspot_distid_list=list(data_overall.nlargest(5,['neighborhoodzscore'])['districtid'])
data_coldspot_distid_list=list(data_overall.nsmallest(5,['neighborhoodzscore'])['districtid'])
csv_writer_year.writerow([1, 'neighbor', 'hotspot', data_hotspot_distid_list[0], data_hotspot_distid_list[1],
                              data_hotspot_distid_list[2], data_hotspot_distid_list[3], data_hotspot_distid_list[4]])
csv_writer_year.writerow(
        [1, 'neighbor', 'coldspot', data_coldspot_distid_list[0], data_coldspot_distid_list[1],
         data_coldspot_distid_list[2], data_coldspot_distid_list[3], data_coldspot_distid_list[4]])

data_hotspot_distid_list_state=list(data_overall.nlargest(5,['statezscore'])['districtid'])
data_coldspot_distid_list_state=list(data_overall.nsmallest(5,['statezscore'])['districtid'])
csv_writer_year.writerow(
        [1, 'state', 'hotspot', data_hotspot_distid_list_state[0], data_hotspot_distid_list_state[1],
         data_hotspot_distid_list_state[2], data_hotspot_distid_list_state[3], data_hotspot_distid_list_state[4]])
csv_writer_year.writerow(
        [1, 'state', 'coldspot', data_coldspot_distid_list_state[0], data_coldspot_distid_list_state[1],
         data_coldspot_distid_list_state[2], data_coldspot_distid_list_state[3], data_coldspot_distid_list_state[4]])

data_file_week.close()
data_file_month.close()
data_file_year.close()