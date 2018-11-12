# programming (first edition)
This is a reminder for me to recall what revision and what function added into the programming.
# Read-Process-AIS-Data
The automatic identification system(AIS) is an automatic tracking system used on ships and by vessel traffic services(VTS). Information provided by AIS equipment, such as unique identification, position, course, and speed, can be displayed on a screen or an ECDIS. AIS is intented widely to assist a vessel's tracking, watchkeeping and allow maritime autorities to track and monitor vessel movement. This is just a briefing about AIS and the data of AIS produced can be used to do a lot of analysis works such as vessel tracking behavior analysis in different navigation areas or providing a lot of sample data for the maritime autonomous surface ships(MASS) system training. This is the pre-work for the convolutional neural network for the MASSs. Here is some briefing about this pre-processing AIS data.
# AIS data collection
The AIS data is derived from the shore-based station and satellite-AIS. These data formats is commonly used the NMEA coding format. There are many open sources for decoding the AIS data. And this project uses one of decoding programming to decode the data to .csv format. After that, we transfer these data into MySQL to do the preliminary process. 
## Preliminary process in MySQL
In the MySQL, the tables and filed can be built to help choose the data. The choose standard is based on your work and your requirements.
## Get the .csv format data
When the data are selected in the MySQL platform, it can be easily converted into .csv format. The .csv format is compatible to process in the Pandas or Numpy packages under the Python development environment. 
## The detail or technologies 
the details can be shown in the .py files and there are three files: read and process data.py, trajectory generation test.py and trajectory generation.py. The three files have different functions:
### read and procee data.py
this file is the process starting point. It uses to combine the .csv file into one file and get the whole dataframe. And also, erase the unnecessary fields. The details can be explained in the file.
### trajectory generation test.py
This file is used to test some of algorithms processing the data. Due to the large size of the original data, it runs wasting a lot of time and we choose some parts of data from the original data.
### trajectory generation.py
This is the processing file to process the original data.

# programming revision (second edition)
This is a second major revision. In this revision, I add some functions like delete_csv_file.py, ais_trajectory.sh and address_datetime.py into the directory.
Let's just talk about the functions.
## trajectory gengeration.py 
After processing the AIS data, the trajectory of the same MMSI can be obtained. The only drawback is that it cannot seperate it into different files. So, I introduce the delete_csv_file function into the directory.
## delete_csv_file.py 
This means that it can realise the function of divide the file into a list by MMSI character. And after that, deleting a small file, for example, there is just only 1 kb file, which is just only contain a small or only one trajectory. It cannot useful for later CNN. 
## asi_trajectory.sh
This is a shell script to submit the file into the HPC for ULC Legion platform. 
## address_datetime.py
This file can extract the filed of time for the same MMSI vessel. It can show the different day's trajectory and finally it can get the trajectory results.

# Acknowledgement
The authors acknowledge the use of the UCL Legion High Performance Computing Facility (Legion@UCL), and associated support services, in the completion of this work.
