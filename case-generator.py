from _datetime import datetime as dt
import csv
import pandas as pd

data_file_week = open('case-week.csv', 'w', newline="")
csv_writer_week = csv.writer(data_file_week)
header_week = ['districtid','weekid','cases']
csv_writer_week.writerow([header_week[0], header_week[1], header_week[2]])
start_date = dt.date(dt.strptime('15/03/2020', '%d/%m/%Y'))
start_date_weeknum = start_date.strftime("%U")
end_date=dt.date(dt.strptime('05/09/2020', '%d/%m/%Y'))
end_date_weeknum=end_date.strftime("%U")

data_file_month = open('case-month.csv', 'w', newline="")
csv_writer_month = csv.writer(data_file_month)
start_date_monthnum = start_date.strftime("%m")
end_date_monthnum=end_date.strftime("%m")
header_month = ['districtid','monthid','cases']
csv_writer_month.writerow([header_month[0], header_month[1], header_month[2]])

data_file_year = open('case-overall.csv', 'w', newline="")
csv_writer_year = csv.writer(data_file_year)
header_year = ['districtid','overallid','cases']
csv_writer_year.writerow([header_year[0], header_year[1], header_year[2]])

district_id_data = pd.DataFrame(pd.read_csv('district_state_data.csv'))
#this is done to handle the week and the months which have no data
for distid in district_id_data['districtid']:
    for k in range(1,int(end_date_weeknum)-int(start_date_weeknum)+2):
        csv_writer_week.writerow([distid,k,0])
    for k in range(1,int(end_date_monthnum)-int(start_date_monthnum)+2):
        csv_writer_month.writerow([distid,k,0])
    csv_writer_year.writerow([distid,1,0])
#print("Time start : ",dt.now())
for i in range(1,15):
    url=f"Required Data/raw_data{i}.csv"
    data=pd.DataFrame(pd.read_csv(url))
    data_df=data['Date Announced']

    for i in range(len(data)):
       # print(i)
       status_of_patient=data.loc[i,'Current Status']
       #print(status_of_patient)
       if(type(status_of_patient)==str and status_of_patient.lower()=='hospitalized'):
           flag=True
           dist=data.loc[i, 'Detected District']
           #print(dist," ",data_df[i])
           if type(data.loc[i, 'Detected State'])==str and data.loc[i, 'Detected State'].lower()=='delhi':
               dist='Delhi'
           elif type(data.loc[i, 'Detected State'])==str and data.loc[i, 'Detected State'].lower()=='sikkim':
               dist='Sikkim'
           elif type(data.loc[i, 'Detected State'])==str and data.loc[i, 'Detected State'].lower()=='goa':
               dist='Goa'
           elif type(data.loc[i, 'Detected State'])==str and data.loc[i, 'Detected State'].lower()=='manipur':
               dist='Manipur'
           elif type(data.loc[i, 'Detected State'])==str and data.loc[i, 'Detected State'].lower()=='assam':
               dist='Assam'
           elif type(data.loc[i, 'Detected State']) == str and data.loc[i, 'Detected State'].lower() == 'telangana':
               dist = 'Telangana'
               #pratapgarh/Q1473962--Uttar Pradesh
           if type(dist)!=float: # to neglect nan items
               try:
                   state=''
                   if data.loc[i, 'Detected District']=='Aurangabad':
                       state=data.loc[i, 'Detected State']
                       if(state=='Maharashtra'):
                           dist='aurangabad/Q592942'
                       else:
                           dist='aurangabad/Q43086'
                       dist_id=district_id_data.loc[district_id_data['district_jsonname']==dist,'districtid'].iloc[0]
                       flag=False
                   elif data.loc[i, 'Detected District']=='Hamirpur':
                       state=data.loc[i, 'Detected State']
                       if(state=='Himachal Pradesh'):
                           dist="hamirpur/Q2086180"
                       else:
                           dist='hamirpur/Q2019757'
                       dist_id=district_id_data.loc[district_id_data['district_jsonname']==dist,'districtid'].iloc[0]
                       flag=False
                   elif data.loc[i, 'Detected District']=='Pratapgarh':
                       state=data.loc[i, 'Detected State']
                       if(state=='Uttar Pradesh'):
                           dist="pratapgarh/Q1473962"
                       else:
                           dist='pratapgarh/Q1585433'
                       dist_id=district_id_data.loc[district_id_data['district_jsonname']==dist,'districtid'].iloc[0]
                       flag=False
                   elif data.loc[i, 'Detected District'] == 'Balrampur':
                       state = data.loc[i, 'Detected State']
                       if (state == 'Uttar Pradesh'):
                           dist = "balrampur/Q16056268"
                           #print(int(data.loc[i,'Num Cases']))
                       else:
                           dist = 'balrampur/Q1948380'
                       dist_id = district_id_data.loc[district_id_data['district_jsonname'] == dist, 'districtid'].iloc[0]
                       flag=False
                   elif data.loc[i, 'Detected District'] == 'Bilaspur':
                       state = data.loc[i, 'Detected State']
                       if (state == 'Chhattisgarh'):
                           dist = "bilaspur/Q100157"
                       else:
                           dist = 'bilaspur/Q1478939'
                       dist_id = district_id_data.loc[district_id_data['district_jsonname'] == dist, 'districtid'].iloc[0]
                       flag=False
                   if(flag):
                        try:
                            if(dist.lower()=='adilabad'):
                                dist_id=district_id_data.loc[district_id_data['district_jsonname']=='adilabad/Q15211','districtid'].iloc[0]
                            else:
                                dist_id=district_id_data.loc[district_id_data['district_covidname']==dist,'districtid'].iloc[0]
                        except:
                            dist_id=-1

               except:
                    #print(data.loc[i, 'Detected District'])
                    #district_1=count
                    #count+=1
                    dist_id=-1
               if(dist_id!=-1):
                   #print(district_1)
                    temp=dt.date(dt.strptime(data_df[i],'%d/%m/%Y'))
                    #print(temp," ",start_date)
                    if temp >=start_date and temp<=end_date:
                        csv_writer_week.writerow([dist_id,int(temp.strftime("%U"))-int(start_date_weeknum)+1,int(data.loc[i,'Num Cases'])])
                        csv_writer_month.writerow([dist_id, int(temp.strftime("%m")) - int(start_date_monthnum) + 1,int(data.loc[i, 'Num Cases'])])
                        csv_writer_year.writerow([dist_id, 1,int(data.loc[i, 'Num Cases'])])

data_file_week.close()
data_file_month.close()
data_file_year.close()

district_data_week=pd.DataFrame(pd.read_csv("case-week.csv"))
group_data=district_data_week.groupby(['districtid','weekid'],as_index=True)['cases'].sum().reset_index()
group_data = group_data.sort_values(['districtid','weekid'], ascending=[True, True])
group_data.to_csv('case-week.csv',index=False)

#print('case-week.csv is created')

district_data_month=pd.DataFrame(pd.read_csv("case-month.csv"))
group_data=district_data_month.groupby(['districtid','monthid'],as_index=True)['cases'].sum().reset_index()
group_data = group_data.sort_values(['districtid','monthid'], ascending=[True, True])
group_data.to_csv('case-month.csv',index=False)


#print('case-month.csv is created')

district_data_year=pd.DataFrame(pd.read_csv("case-overall.csv"))
group_data=district_data_year.groupby(['districtid','overallid'],as_index=True)['cases'].sum().reset_index()
group_data = group_data.sort_values(['districtid','overallid'], ascending=[True, True])
group_data.to_csv('case-overall.csv',index=False)
#print('case-overall.csv is created')

#print("Time end : ",dt.now())
