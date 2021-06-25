#this program maps the json district to dirstrict names in raw_data files along with its states
import json
import csv
import pandas as pd
from fuzzywuzzy import process,fuzz


data_file = open('state-district.csv', 'w+',newline='',encoding='utf-8')
csv_writer = csv.writer(data_file)
header_list=['statename','districtname']
csv_writer.writerow([header_list[0],header_list[1]])

with open('Required Data/data-all.json') as file:
    datafile=json.load(file)
for dates in datafile.keys():
    for states in datafile[dates].keys():
        #print(datafile[dates][states].keys())
        try:
            for district in datafile[dates][states]['districts']:
                if district!='Unknown':
                    csv_writer.writerow([states,district])
        except:
            continue

data_file.close()

state_data=pd.read_csv("state-district.csv",usecols=['statename','districtname']).drop_duplicates(keep='first')
state_data.to_csv('state-district.csv',index=False)



district_id_data = pd.DataFrame(pd.read_csv('modified_neighbor_districts.csv'))
covid_district_data=pd.DataFrame(pd.read_csv('Required Data/district_wise.csv'))

def fuzz_score(str1,dataframe1):
    return process.extract(str1, dataframe1, scorer=fuzz.token_sort_ratio,limit=1)[0][0]

def fuzz_score1(str1,dataframe1):
    return process.extract(str1, dataframe1,limit=1)[0][0]

data_file_merge = open('case-district-data.csv', 'w',encoding='utf-8', newline="")
csv_writer_merge = csv.writer(data_file_merge)
header_week = ['districtid','districtname_json','districtname_covid19']
csv_writer_merge.writerow([header_week[0], header_week[1], header_week[2]])
dict_data={}
district_mismatch_list=['anand_district/Q485683','bishwanath/Q28110722','dahod_district/Q186518','east_khasi_hills/Q1945304','gadag_district/Q2353931','kanpur_dehat/Q610612','karur_district/Q15182','kheda_district/Q1755463','kolar_district/Q2509866','shahdara/Q83486','south_24_parganas/Q2308319','south_garo_hills/Q2329228','south_west_garo_hills/Q15961576',
'west_siang/Q15453','udham_singh_nagar/Q1805082','the_dangs/Q1135616','mahe_district/Q639279','upper_subansiri/Q15464','uttar_dinajpur/Q2019766','uttara_kannada/Q579205','west_garo_hills/Q2329181','west_godavari/Q15404','west_jaintia_hills/Q1920789','west_kameng_district/Q15459','west_khasi_hills/Q2064752','kra_daadi/Q21018627','kurung_kumey_district/Q2449506','kutch_district/Q1063417','leh_district/Q1921210','lower_dibang_valley/Q2373368',
'mahesana_district/Q2019694','mancherial_district/Q28169747','north_garo_hills/Q7055466','mulugu/Q61746006','narayanpet/Q61746013','paschim_bardhaman/Q29215602','paschim_medinipur/Q1855537','salem_district/Q15192','sawai_madhopur/Q1507166']

url=f"state-district.csv"
data=pd.DataFrame(pd.read_csv(url))

for i in range(len(district_id_data)):
    dist = district_id_data.loc[i, 'districtname']
    if dist=='pune_district/Q1797336':
        dist_name='Pune'
    elif dist=='tawang_district/Q15449':
        dist_name='Tawang'
    else:
        #print(data['districtname'])
        if dist in district_mismatch_list:
            dist_name = fuzz_score1(dist, covid_district_data['District'])
        else:
            dist_name= fuzz_score(dist, data['districtname'])
        #print(dist_name)
    district_1 = district_id_data.loc[i, 'districtid']

    #these districts i had to map manually as they were not mapping correctly(out of these 7 are merged districts namely delhi,mumbai,sikkim,goa,manipur,assam,telangana)
    if dist=='delhi/Q145823':
        dist_name='Delhi'
    elif dist=='adilabad/Q15211':
        dist_name='Adilabad'
    elif dist=='kamareddy/Q27956125':
        dist_name='Kamareddy'
    elif dist=='hyderabad/Q15340':
        dist_name='Hyderabad'
    elif dist=='medak/Q15386':
        dist_name='Medak'
    elif dist=='sikkim/Q4576':
        dist_name='Sikkim'
    elif dist=='assam/Q58731':
        dist_name='Assam'
    elif dist=='goa/Q8576':
        dist_name='Goa'
    elif dist=='manipur/Q5873':
        dist_name='Manipur'
    elif dist == "telangana/Q85761":
        dist_name = 'Telangana'
    elif dist=='theni_district/Q15196':
        dist_name='Theni'
    elif dist=='south_west_khasi_hills/Q15923741':
        dist_name='South West Khasi Hills'
    elif dist=='west_tripura/Q1947570':
        dist_name='West Tripura'
    elif dist=='south_west_garo_hills/Q15961576':
        dist_name='South West Garo Hills'
    elif dist=='upper_siang/Q15465':
        dist_name='Upper Siang'
    elif dist=='upper_dibang_valley/Q15446':
        dist_name='Upper Dibang Valley'
    elif dist=='gautam_buddha_nagar/Q1785950':
        dist_name='Gautam Buddha Nagar'
    elif dist=='ayodhya/Q1814132':
        dist_name='Ayodhya'
    elif dist=='coochbihar/Q2728658':
        dist_name='Cooch Behar'
    elif dist=='shahid_bhagat_singh_nagar/Q202710':
        dist_name='Shahid Bhagat Singh Nagar'
    elif dist=='tehri_garhwal/Q1357107':
        dist_name='Tehri Garhwal'
    elif dist=='west_siang/Q15453':
        dist_name='West Siang'
    elif dist=='amroha/Q1891677':
        dist_name='Amroha'
    elif dist=='bhadohi/Q127533':
        dist_name='Bhadohi'
    elif  dist=='vijayapura/Q1727570':
        dist_name="Vijayapura"
    elif dist=='palakkad/Q1535742':
        dist_name='Palakkad'
    elif dist=='subarnapur/Q1473957':
        dist_name='Subarnapur'
    elif dist=='belagavi/Q815464':
        dist_name='Belagavi'
    elif dist=='balasore/Q2022279':
        dist_name='Balasore'
    elif dist=='beed/Q814037':
        dist_name='Beed'
    elif dist=='hooghly/Q548518':
        dist_name='Hooghly'
    elif dist=='mehsana_district/Q2019694':
        dist_name='Mehsana'
    elif dist=='sri_potti_sriramulu_nellore/Q15383':
        dist_name='S.P.S. Nellore'
    elif dist=='seraikela_kharsawan/Q2362658':
        dist_name='Saraikela-Kharsawan'
    elif dist=='sahibzada_ajit_singh_nagar/Q2037672':
        dist_name='S.A.S. Nagar'
    elif dist=='pakke_kessang/None':
        dist_name='Pakke Kessang'
    elif dist=='rae_bareilly/Q1321157':
        dist_name='Rae Bareli'
    elif dist=='pashchim_champaran/Q100124':
        dist_name='West Champaran'

    csv_writer_merge.writerow([district_1,dist,dist_name])

data_file_merge.close()
district_data_json=pd.DataFrame(pd.read_csv("case-district-data.csv"))
district_data_json=district_data_json.sort_values(['districtid'], ascending=[True])
district_data_json.to_csv('case-district-data.csv',index=False)

data_district_json=pd.DataFrame(pd.read_csv('case-district-data.csv'))
data_state=pd.DataFrame(pd.read_csv('Required Data/district_wise.csv'))


data_state_district = open('district_state_data.csv', 'w', newline="")
csv_writer_state = csv.writer(data_state_district)
header_state = ['districtid','district_jsonname','district_covidname','state']
csv_writer_state.writerow([header_state[0], header_state[1], header_state[2],header_state[3]])
for i in range(len(data_district_json)):
    districtname=data_district_json.loc[i,'districtname_covid19']
    districtid=data_district_json.loc[i,'districtid']
    districtjsonname=data_district_json.loc[i,'districtname_json']
    #this is manual mapping of districts of same names to their respective states
    if districtjsonname=='aurangabad/Q592942':
        statename='Maharashtra'
    elif districtjsonname=='aurangabad/Q43086':
        statename='Bihar'
    elif districtjsonname=='hamirpur/Q2086180':
        statename='Himachal Pradesh'
    elif districtjsonname=='hamirpur/Q2019757':
        statename='Uttar Pradesh'
    elif districtjsonname=='pratapgarh/Q1473962':
        statename='Uttar Pradesh'
    elif districtjsonname=='pratapgarh/Q1585433':
        statename='Rajasthan'
    elif districtjsonname=='balrampur/Q16056268':
        statename='Uttar Pradesh'
    elif districtjsonname=='balrampur/Q1948380':
        statename='Chhattisgarh'
    elif districtjsonname=='bilaspur/Q100157':
        statename='Chhattisgarh'
    elif districtjsonname=='bilaspur/Q1478939':
        statename='Himachal Pradesh'
    else:
        try:
            #print("districtjsoname is ",districtjsonname," district name is ",districtname)
            statename=data_state.loc[data_state['District']==districtname,'State'].iloc[0]
            #print(districtid, districtjsonname, districtname, statename)
        except:
            continue
        #print(districtid,districtjsonname,districtname,statename)
    csv_writer_state.writerow([districtid,districtjsonname,districtname,statename])
merged_districts=['telangana/Q85761','goa/Q8576','manipur/Q5873','sikkim/Q4576','delhi/Q145823','assam/Q58731']
for i in merged_districts:
    districtid = data_district_json.loc[data_district_json['districtname_json'] == i, 'districtid'].iloc[0]
    districtjsonname=i
    districtname=data_district_json.loc[data_district_json['districtid'] == districtid, 'districtname_covid19'].iloc[0]
    csv_writer_state.writerow([districtid,districtjsonname,districtname,districtname])

data_state_district.close()
data_state_district.close()

district_data_state=pd.DataFrame(pd.read_csv("district_state_data.csv"))
#group_data=district_data_state.groupby(['districtid','weekid'],as_index=True)['cases'].sum().reset_index()
district_data_state = district_data_state.sort_values(['districtid'], ascending=[True])
district_data_state.to_csv("district_state_data.csv",index=False)

