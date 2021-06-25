I have used Python 3.6.1 interpretor and the following packeges:-
pandas,fuzzywuzzy,python-Levenshtein,numpy,datetime
To install these packages run the following command:
sudo apt-get install -y python3-fuzzywuzzy
sudo apt-get -y install python3-pip
sudo pip3 install pandas
sudo apt-get install -y python3-levenshtein
pip3 install DateTime

Please do not delete any of the csv files created in any of the questions as I have used those csv files to solve some of the subsequent questions.
The data that I have obtained from https://api.covid19india.org/documentation/csv/ ,I have kept it in the Required Data Folder and has used it for solving the assignment problems.

For making the scripts executable please run the command chmod u+x scriptname.sh.

To run the scripts write ./scriptname.sh in the terminal.

1. For creating the neighbor-districts-modified.json please run the neighbor-districts-modified.sh script. This script will also create modified_neighbor_districts.csv which maps each district(sorted alphabetically) to a unique districtid (starting from 101).Please run the command chmod u+x neighbor-districts-modified.sh before running the script to make it executable and to run type ./neighbor-districts-modified.sh in the terminal.

Also it is going to create a district_state_data.csv which matches the json districts to closest matching names of covi19 districts(this is done using json_covid_datamatch.py file)of data_all.json.While matching i used fuzzywuzzy token sort ratio and got 94% accuracy.(35 mismatches out of 627 districts)[Note: out of the 35 mismatches 15 were slight mismatch like east garo hills being mapped to west garo hills].In order to further increase the accuracy for the mismatched 35 districts I have tried to map them to the districts in district_wise.csv which I obtained from the Covid19 website. On matching them my accuracy now went from 94% to 97% as now only 18 districts out of 627 districts are mismatched.I mapped these 18 districts to their correct names in Covid19 data manually.The json districtname to covid19 district name mapping with their respective state name is 
present in district_state_data.csv.

Districts of delhi,sikkim,goa,manipur,assam and telegana have been merged in neighbor-districts-modified.json as their district wise data was unavailable in 'https://api.covid19india.org/v4/data-all.json'.Also noklak,konkan has been removed as it was unavailable in data-all.json.Also i have merged mumbai_cityand mumbai_suburn to mumbai due to unavailability of data.

2. For question 2, I have used the json district to covid19 data district mapping(i.e. district_state_data.csv formed in the previous question) and have calculated the count of cases weekwise, monthwise and overall(yearwise). To generate the case-week.csv,case-month.csv,case-overall.csv please run the case-generator.sh. This script(case-generator.sh) might require approx 5-7 mins as it scans 15 rawdata input files(obtained from https://api.covid19india.org/documentation/csv/) to generate the output.Before running case-generator.sh please run the command chmod u+x case-generator.sh to make it executable and to run the script type ./case-generator.sh in the terminal.

I have considered the week 15th March,2020-21st,March,2020 as weekid 1 and for month I have considered month of March to have a monthid of 1.Also the output is sorted based on districtid and timeid.

3.For creating the edge-graph.csv please run  edge-generator.sh file. It creates an undirected graph with edges from district 'i' to 'j' if 'j' and 'i' are neighbors and does not create an edge form district 'j' to district 'i'(i.e. does not create duplicate edges). For creating the edge-graph.csv file I have used modified_neighbor_districts.csv(formed in question 1 and contains districts with its district id) and the
neighbor-districts-modified.json(formed in question 1 containing each district with its neighboring districts as adjacency list).Also the output is sorted based on districtid.Before running edge-generator.sh please run the command chmod u+x edge-generator.sh to make it executable and to run the script type ./edge-generator.sh in the terminal.

4.For the 4th question i.e. calculating neighbor district cases mean and standard deviation based on week,month and overall please run the neighbor-generator.sh. The script will create three csvs namely
neighbor-week.csv,neighbor-month.csv,neighbor-overall.csv. For the generation of neighbor-time(where time is week,month,overall).csv I have used the data computed in previous question in the case-week.csv,case-month.csv and case-overall.csv . I have rounded up the standard deviation and mean upto 2 decimal places as mentioned in the question. Also the output is sorted based on districtid.Before running neighbor-generator.sh please run the command chmod u+x neighbor-generator.sh to make it executable and to run the script type ./neighbor-generator.sh in the terminal. Please wait the script might take 3-4mins to run.

5.For th 5th question i.e. calculating mean and standard deviation of districts within a state based on week,month and overall, please run state-generator.sh. The script will create three csvs namely 
state-week.csv,state-month.csv,state-overall.csv. For generating the state-time.csv(where time is week,month,overall) i have used the data computed in previous question in the case-week.csv,case-month.csv and case-overall.csv.Also i have used district_state_data.csv(which i computed in question 1) for district to state mapping. I have rounded up the standard deviation and mean upto 2 decimal places as mentioned in the question. Also the output is sorted based on districtid. Before running state-generator.sh please run the command chmod u+x state-generator.sh to make it executable and to run type ./state-generator.sh in the terminal.

6.For the 6th question which is calculating zscore neighbourwise and statewise please run 
zscore-generator.sh script. The script will create three csvs namely zscore-week.csv,
zscore-month.csv,zscore-overall.csv. For generating the zscore i have used case-week.csv,case-month.csv and case-overall.csv,state-week.csv,state-month.csv,state-overall.csv,neighbor-week.csv,neighbor-month.csv,neighbor-overall.csv(all these were computed in the previous questions).I have rounded up the standard deviation and mean upto 2 decimal places as mentioned in the question. Also the output is sorted based on districtid. Before running zscore-generator.sh please run the command chmod u+x zscore-generator.sh to make it executable and to run type ./zscore-generator.sh in the terminal.

7.For the 7th question i.e. identifying hotspot and coldspot both neighbor wise and state wise please run method-spot-generator.sh. The script is going to create three csv files namely method-spot-week.csv,
method-spot-month.csv,method-spot-overall.csv. For generating hotspot and coldspot i have used case-week.csv,case-month.csv and case-overall.csv,state-week.csv,state-month.csv,state-overall.csv,neighbor-week.csv,neighbor-month.csv,neighbor-overall.csv(all these were computed in the previous questions).
Before running method-spot-generator.sh please run the command chmod u+x method-spot-generator.sh to make it executable and to run type ./method-spot-generator.sh in the terminal.

8.For the 8th question, i.e. identifying top 5 hotspots and coldspots weekwise,monthwise and overall based on zscore please run the script top-generator.sh.The script is going to create three csv files namely top-week.csv,top-month.csv,top-overall.csv. For this i have used the zscore-week.csv,zscore-month.csv and zscore-overall.csv which has been formed in the previous questions. 
Before running top-generator.sh please run the command chmod u+x top-generator.sh to make it executable and to run please type ./top-generator.sh in the terminal.

9.For the 9th question i.e. the top level script assign1.sh which runs all the scripts please execute the command chmod u+x assign1.sh to make it executable and then to tun please type ./assign1.sh in the terminal.

10. The report.tex is present in the folder named as Report and all the required files for its succesfull compilation is present there .