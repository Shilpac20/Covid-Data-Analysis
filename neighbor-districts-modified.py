import json
with open('Required Data/neighbor-districts.json') as file:
    data=json.load(file)
    with open('neighbor-districts-modified.json', 'w') as f:
        json.dump(data, f,indent = 8)
    f.close()
    list_delhi=["shahdara/Q83486"]
    list_sikkim=[]
    list_goa=[]
    list_mumbai=["mumbai_city/Q2341660","mumbai_suburban/Q2085374"]
    list_telengana=["narayanpet/Q61746013",'mancherial_district/Q28169747','mulugu/Q61746006',"adilabad/Q15211","bhadradri_kothagudem/Q28169767","hyderabad/Q15340","jagtial/Q28169780","jangaon/Q28170170","jayashankar_bhupalapally/Q28169775","jogulamba_gadwal/Q27897618","kamareddy/Q27956125","karimnagar/Q15373","khammam/Q15371","komram_bheem/Q28170184","mahabubabad/Q28169761","mahabubnagar/Q15380","medak/Q15386","medchal\u2013malkajgiri/Q27614841","nagarkurnool/Q28169773","nalgonda/Q15384","nirmal/Q28169750","nizamabad/Q15391","peddapalli/Q27614797","rajanna_sircilla/Q28172781","rangareddy/Q15388","sangareddy/Q28169753","siddipet/Q28169756","suryapet/Q28169770","vikarabad/Q28170173","wanaparthy/Q28172504","warangal_rural/Q28169759","warangal_urban/Q213077","yadadri_bhuvanagiri/Q28169764"]
    list_manipur=["bishnupur/Q938190","chandel/Q2301769","churachandpur/Q2577281","imphal_east/Q1916666","imphal_west/Q1822188","senapati/Q2301706","tamenglong/Q2301717","thoubal/Q2086198","ukhrul/Q735101","kangpokpi/Q28419386","tengnoupal/Q28419388","pherzawl/Q28173809","noney/Q28419389","jiribam/Q28419387","kamjong/Q28419390","kakching/Q28173825"]
    list_assam=['bishwanath/Q28110722',"barpeta/Q41249","bongaigaon/Q42197","cachar/Q42209","charaideo/Q24039029","chirang/Q2574898","darrang/Q42461","baksa/Q2360266","dhemaji/Q42473","dhubri/Q42485","dibrugarh/Q42479","goalpara/Q42522","golaghat/Q42517","hailakandi/Q42505","hojai/Q24699407","jorhat/Q42611","kamrup/Q2247441","kamrup_metropolitan/Q2464674","west_karbi_anglong/Q24949218","east_karbi_anglong/Q42558","karimganj/Q42542","kokrajhar/Q42618","lakhimpur/Q42743","majuli/Q28110729","nagaon/Q42686","marigaon/Q42737","nalbari/Q42779","dima_hasao_district/Q42774","sivasagar/Q42768","sonitpur/Q42765","south_salmara-mankachar/Q24907599","tinsukia/Q42756","udalguri/Q321998"]

    for d in data.keys():
        try:
            if d.index('_delhi'):
                #print(d)
                list_delhi.append(d)
        except:
            try:
                if d.index('_sikkim_district'):
                    list_sikkim.append(d)
            except:
                try:
                    if d.index('_goa'):
                        list_goa.append(d)
                except:
                    continue
   # these list will be modified neighbors of the districts merged (delhi,sikkim,goa,assam,manipur,mumbai,telangana)
    districts_delhi=[]
    districts_goa=[]
    districts_assam=[]
    districts_sikkim=[]
    districts_manipur=[]
    districts_telengana=[]
    districts_mumbai=[]
    for i in list_delhi:
        neighbor=data[i]
        for j in set(neighbor).difference(set(districts_delhi)):
            districts_delhi.append(j)
            try:
                if j in list_delhi or j in list_assam or j in list_sikkim or j in list_manipur or j in list_goa or j in list_telengana or j in list_mumbai or j=='konkan_division/Q6268840' or j=='noklak/Q48731903':
                   districts_delhi.remove(j)
            except:
                continue
    for i in list_assam:
        neighbor=data[i]
        for j in set(neighbor).difference(set(districts_assam)):
            districts_assam.append(j)
            if j in list_delhi or j in list_assam or j in list_sikkim or j in list_manipur or j in list_goa or j in list_telengana or j in list_mumbai or j=='konkan_division/Q6268840' or j=='noklak/Q48731903':
                districts_assam.remove(j)
    for i in list_sikkim:
        neighbor=data[i]
        for j in set(neighbor).difference(set(districts_sikkim)):
            districts_sikkim.append(j)
            if j in list_delhi or j in list_assam or j in list_sikkim or j in list_manipur or j in list_goa or j in list_telengana or j in list_mumbai or j=='konkan_division/Q6268840' or j=='noklak/Q48731903':
                districts_sikkim.remove(j)
    for i in list_manipur:
        neighbor = data[i]
        for j in set(neighbor).difference(set(districts_manipur)):
            districts_manipur.append(j)
            if j in list_delhi or j in list_assam or j in list_sikkim or j in list_manipur or j in list_goa or j in list_telengana or j in list_mumbai or j=='konkan_division/Q6268840' or j=='noklak/Q48731903':
                districts_manipur.remove(j)
    for i in list_goa:
        neighbor = data[i]
        for j in set(neighbor).difference(set(districts_goa)):
            districts_goa.append(j)
            if j in list_delhi or j in list_assam or j in list_sikkim or j in list_manipur or j in list_goa or j in list_telengana or j in list_mumbai or j=='konkan_division/Q6268840' or j=='noklak/Q48731903':
                districts_goa.remove(j)
    for i in list_telengana:
        neighbor = data[i]
        for j in set(neighbor).difference(set(districts_telengana)):
            districts_telengana.append(j)
            if j in list_delhi or j in list_assam or j in list_sikkim or j in list_manipur or j in list_goa or j in list_telengana or j in list_mumbai or j=='konkan_division/Q6268840' or j=='noklak/Q48731903':
                districts_telengana.remove(j)
    for i in list_mumbai:
        neighbor = data[i]
        for j in set(neighbor).difference(set(districts_mumbai)):
            districts_mumbai.append(j)
            if j in list_delhi or j in list_assam or j in list_sikkim or j in list_manipur or j in list_goa or j in list_telengana or j in list_mumbai or j=='konkan_division/Q6268840' or j=='noklak/Q48731903':
                districts_mumbai.remove(j)
    #print("distritcs manipur",districts_manipur)
    with open('neighbor-districts-modified.json', 'r') as f:
        districts_data=json.load(f)
    with open('neighbor-districts-modified.json', 'r') as f:
        districts_data_temp=json.load(f)
    for element in districts_data:
        #print(districts_data[element])
        if element is not None:
            #print('Hi',element)
            if element in list_delhi or element in list_assam or element in list_sikkim or element in list_manipur or element in list_goa or element in list_telengana or element in list_mumbai or element=="noklak/Q48731903" or element=="konkan_division/Q6268840":
                del districts_data_temp[element]
    #print(json.dumps(districts_data))
    #print(districts_data_temp)

    for element in districts_data_temp:
        neighbour_list=districts_data_temp[element]
        #print(neighbour_list,element)
        neighbour_list_temp=[]
        flag_delhi=False
        flag_assam=False
        flag_sikkim=False
        flag_manipur=False
        flag_goa=False
        flag_telengana=False
        flag_mumbai=False
        flag_noklak=False
        flag_konkan=False
        for item in neighbour_list:
            try:
                if item in list_delhi:
                    #print('HI')
                    #print(item," ",neighbour_list)
                    #neighbour_list.remove(item)
                    #print(neighbour_list)
                    flag_delhi=True
                elif item in list_assam:
                    flag_assam=True
                elif item in list_sikkim:
                    flag_sikkim=True
                elif item in list_manipur:
                    flag_manipur=True
                elif item in list_goa:
                    flag_goa=True
                elif item in list_telengana:
                    flag_telengana=True
                elif item in list_mumbai:
                    flag_mumbai=True
                elif item=="noklak/Q48731903":
                    flag_noklak=True
                elif item=="konkan_division/Q6268840":
                    flag_konkan=True
                else:
                    neighbour_list_temp.append(item)

            except:
                continue
        #print(neighbour_list,element)
        if flag_delhi:
            neighbour_list_temp.append('delhi/Q145823')
            districts_data_temp[element]=neighbour_list_temp
        if flag_assam:
            neighbour_list_temp.append('assam/Q58731')
            districts_data_temp[element] = neighbour_list_temp
        if flag_sikkim:
            neighbour_list_temp.append('sikkim/Q4576')
            districts_data_temp[element] = neighbour_list_temp
        if flag_manipur:
            neighbour_list_temp.append('manipur/Q5873')
            districts_data_temp[element] = neighbour_list_temp
        if flag_goa:
            neighbour_list_temp.append('goa/Q8576')
            districts_data_temp[element] = neighbour_list_temp
        if flag_telengana:
            neighbour_list_temp.append('telangana/Q85761')
            districts_data_temp[element] = neighbour_list_temp
        if flag_mumbai:
            neighbour_list_temp.append('mumbai/Q857613')
            districts_data_temp[element] = neighbour_list_temp
        if flag_noklak:
            districts_data_temp[element] = neighbour_list_temp
        if flag_konkan:
            districts_data_temp[element]=neighbour_list_temp
    districts_data_temp['mumbai/Q857613'] = districts_mumbai
    districts_data_temp['telangana/Q85761'] = districts_telengana
    districts_data_temp['goa/Q8576'] = districts_goa
    districts_data_temp['manipur/Q5873'] = districts_manipur
    districts_data_temp['sikkim/Q4576'] = districts_sikkim
    districts_data_temp['assam/Q58731'] = districts_assam
    districts_data_temp['delhi/Q145823'] = districts_delhi
#this is used to handle speeling mistakes in json or replacing old name of a district with its new name
    spelling_replacements={'firozpur/Q172385':'ferozpur/Q172385',
                           'bid/Q814037':'beed/Q814037',
                           'gondiya/Q1917227':'gondia/Q1917227',
                           'hugli/Q548518':'hooghly/Q548518',
                           'jajapur/Q2087771':'jajpur/Q2087771',
                           'jalor/Q1460832':'jalore/Q1460832',
                           'mahesana_district/Q2019694':'mehsana_district/Q2019694',
                           'faizabad/Q1814132':'ayodhya/Q1814132',
                           'kochbihar/Q2728658':'coochbihar/Q2728658',
                           'shaheed_bhagat_singh_nagar/Q202710':'shahid_bhagat_singh_nagar/Q202710',
                           'jyotiba_phule_nagar/Q1891677':'amroha/Q1891677',
                           'sant_ravidas_nagar/Q127533':'bhadohi/Q127533',
                           'bijapur_district/Q1727570':'vijayapura/Q1727570',
                           'palghat/Q1535742':'palakkad/Q1535742',
                           'sonapur/Q1473957':'subarnapur/Q1473957',
                           'belgaum_district/Q815464':'belagavi/Q815464',
                           'baleshwar/Q2022279':'balasore/Q2022279',
                           'ysr/Q15342':'ysr_kadapa/Q15342'
                           }
    districts_data_1=json.dumps(districts_data_temp)
    for old, new in spelling_replacements.items():
        districts_data_1 = districts_data_1.replace(old, new)
    districts_data_temp=json.loads(districts_data_1)
    with open('neighbor-districts-modified.json', 'w+') as f:
        json.dump(districts_data_temp,f,indent =20 ,sort_keys=True)
    with open('neighbor-districts-modified.json') as file:
        data = json.load(file)
    dictionary = {}
    count = 101
    for d in sorted(data.keys()):
        # print("District is : ",d, " Neighbour is :",data[d])
        dictionary[d] = []
        dictionary[d].append({'id': count, "neighbor": data[d]})
        count += 1
    with open('neighbor-districts-modified.json', 'w') as f:
        json.dump(dictionary, f, indent=8)

