###########################################################################
### COP 4045 - Python Programming - Jordan Burgher - FAU - Summer 2021 ###
###            A4: Fuel Consumption (in Python!)          ###
###             June 17, 2021                                         ###

# Instructions:
# 1. Print a brief (2-5 lines) message explaining the purpose of this “app”
# 2. Prompt for:
#    § Main option:(1) Mileage info or (2) Trend plot
# 3. If option == 1:
    #Prompt user to input the MPG interval they are interested in.
    #Find the vehicles that are within that range and store their information in appropriate data structures.The data file for thispart is called epaData2015.csv
    #Display information(make, model)about vehicles that fall withing that range(similar to the output of code listing 7.15 in the textbook). 
# 4. If option == 2:
    #Prompt user to input the measure that they are interested in.
        #• At a minimum, offer 3 options: (H)ighway MPG, (C)ity MPG and (O)verall MPG
     #Prompt user to input the preferred way to produce the plot:
        #• (D)isplay on screen or save to (F)ile.
    #Gather the necessary data from the CSV file and store it in appropriate data structures. The
    #data file for this part is called epaData2020.csv
    # Prepare and display/save the plot using pylab (see code listing 7.17 in the textbook)



# [1] https://colab.research.google.com/notebooks/intro.ipynb 
# [2] https://github.com/alan-turing-institute/the-turing-way/blob/master/workshops/boost-research-reproducibility-binder/workshop-presentations/zero-to-binder-python.md

###########################################################################

#INTRODUCTION
#This program use matplotlib.py module and csv for data from the US Environment Protection agency (EPA)
#to generate an EPA vehicle fuel consumption information and the relevant trends over time.'''

print("Welcome to Vehicle Fuel Consumption Information!\n\n")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<MAIN MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>")

option = input(" 1: Mileage Information\n 2: Trend over time\n Please enter your selection: ")
import csv   #importing required module
import matplotlib.pyplot as plt# importing required module

Optional = []
year = []

#FUNCTION DEFINITION
#highest mileage data
#from http://www.fueleconomy.gov/FEG/download.shtml
def create_mileage_list(epa_file): 
    #create a list of cars and mileage from epa_file
    #create a mileage list and initialize it to empty
    mileage_list = []
    epa_file.readline()
    x, y = [], []
    
    for line in epa_file(x,y): # get each line from the file
        line_list = line.split(',')# csv split on comma
        if 'Car' in line_list[70]: # append highway mileage
            mileage_list.append(int(line_list[10]))
    return mileage_list
    
'''def create_mileage_list2(epa_file):
    mileage_list = []
    epa_file.readline()   #skip header line
    for line in epa_file:
        line_list = line.split(',')
        if 'Car' in line_list[70]:
            mileage_list.append((int(line_list[10]), line_list[2], line_list[3]))
    return mileage_list'''

def find_max_min_mileage(mileage_list, max_mileage, min_mileage):
    
    max_mileage_list = []
    min_mileage_list = []


    for car_tuple in mileage_list:
        if car_tuple[0] == max_mileage:
            max_mileage_list.append(car_tuple)
        if car_tuple[0] == min_mileage:
            min_mileage_list.append(car_tuple)
            
    return max_mileage_list, min_mileage_list


def create_mileage_list(epa_file):
    
    mileage_list = []
    reader = csv.reader(epa_file) #create csv reader
    for line_list in reader:      #no split needed
        mileage_list.append(line_list[10])
    return mileage_list
        
        
#PLOTTING EPA DATA         
#import matplotlib.py
epa_file = open("epadata2015.csv")
Dict = {}
x,y = [], []
file = epa_file
for line in epa_file:
    line_lst = line.strip().split()
    x.append(str([1]))
    y.append(str([2]))

epa_file.close()
("Please select which MPG average you want to measure")
("(C) City MPG")
("(H) Highway MPG")
("(O) Overall or Combined MPG")
Selection: str = input(">> ")[0]
print("Please select(D)to display on screen\n(F) Save to file?\n")
input("Enter your choice: ")
#plot
Dict = {}


display_data: Optional[plot_data] = extract_year-mileage-data(processed_data, mpg_option.lower())
plot_type: Dict[str, str] = {
        'c': "City",
        'h': "Highway",
        'o': "Overall"}
fp = open("epadata2020.csv")
x,y = [], []
epa_plot = ''

for line in fp:
    line_lst = line.strip().split()
    x.append(str([1])) # year
    y.append(str([2])) # unadjusted highway MPG
    
fp.close()
#plotting the points
plt.plot(x, y)
plt.ylabel("Highway MPG")  #naming y axis
plt.xlabel("Year")         #naming x axis
plt.title("EPA Annual Average Highway MPG")#Giving a title to my graph

#function to show the plot
plt.show()
    #save file
plt.savefig(f"{epa_plot.png}")
savePlot = []
savefig = {}
if savePlot == 's':
        savefig('overallplot.png')
else:
        plt.show()

run = str(input("Press any key to exit  or 'y' to run again: ")).lower()
    
#epa_file = open("mileage_list.txt", "r")


# INTRODUCTION 

'''This application uses data from the US Environment Protection agency (EPA)
to generate an EPA vehicle fuel consumption information and the relevant trends over time.'''

#DRIVER

print("Welcome to Vehicle Fuel Consumption Information!\n\n")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<MAIN MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>")

print(" 1: Mileage Information\n 2: Trend over time\n ")
Selection = input(" Please enter your selection: ")

#open EPA data file object
epa_file = open("epadata2015.csv", "r")
mileage_list = create_mileage_list(epa_file)

if (option == 1):
    print("\nMake | Model\n")

if (option == 2):    
    input = str("Please select which MPG average you want to measure: \n")
    if ( option == 'C'): 
        print("City Average\n") 
 
    elif ( option == 'H'):
        print("Highway Average\n")
    elif ( option == 'O'):
        print("Overall Average \n")

    Selection: str = input(">> ")[0]
    print("Please select(D)to display on screen or(F)to Save to file?\n")

    input("Enter your choice: ")
    if (option == 'D'):       # Display results on screen
        print("Display on screen")
    elif (option == 'F'):       # Save results to file
        print("Save to file")
        
#plot
Dict = {}
display_data: Optional[plot_data] = extract_year-mileage-data(processed_data, mpg_option.lower())
plot_type: Dict[str, str] = {
        'c': "City",
        'h': "Highway",
        'o': "Overall"}
plt.plot(display_data, year, display_data.mpg_average)

print("Plot trend over time\n")