###########################################################################
### COP 4045 - Python Programming - Jordan Burgher - FAU - Summer 2021 ###
###            A5: Iris Dataset and dictionaries (in Python!)          ###
###             July 01, 2021                                         ###

# Instructions:
# 1. Print a brief (2-5 lines) message explaining the purpose of this “app”
# 2. Read in the data from the iris.csv file.
# 3. Create a dictionary with the key as the species name and the values as(placeholders for)the averages of each of the four attributes/features of each data point: petal length, petal width, sepal length, and sepal width.
# 4. Compute the averages of each attribute for each species.
# 5. (“Pretty”) print the results.



# [1] https://colab.research.google.com/notebooks/intro.ipynb 
# [2] https://github.com/alan-turing-institute/the-turing-way/blob/master/workshops/boost-research-reproducibility-binder/workshop-presentations/zero-to-binder-python.md

###########################################################################

import csv
csv.reader(',')
csv.DictReader(',')


print("In this program, you  will be reviewing the chart of the iris flower data file. ")
print("There are 3 classes of 50 instances each, where each class refers to a type of iris plant.")
print("The type of plants are setosa, virginica, and versicolor. Each has 4 attributes: petal length, petal width, sepal length, and sepal width. ")
print("The dictionaries are used to store and process the contents of the dataset.")

#Classes for Data Storage:
#data class store individual values from the petals and sepals of setosa
class iris_species_setosa():
    #Setosa petal list
    avg_petal_length = []
    avg_petal_width = []

    #Setosa sepal list
    avg_sepal_length = []
    avg_sepal_width = []

#data class store individual values from the petals and sepals of virginica
class iris_species_virginica():
    #Virginica petal list
    avg_petal_length = []
    avg_petal_width = []

    #Virginica sepal list
    avg_sepal_length = []
    avg_sepal_width = []

#data class store individual values from the petals and sepals of versicolor
class iris_species_versicolor():
    #Versicolor petal list
    avg_petal_length = []
    avg_petal_width = []

    #Versicolor sepal list
    avg_sepal_length = []
    avg_sepal_width = []

#Reading the data function
def read_iris(csvfile):
    try:
        with open("iris.csv", "r") as opened_file:
            csvreader = csv.reader(opened_file)
            headers = next(csvreader)
            print(headers)
            for row in csvreader:
                print(row)

    except FileNotFoundError:
        print("Error: File not found!")
        raise
my_read_iris = read_iris("iris.csv")



#Computing  the averages of each attribute for each species.
def average_iris(species, species_content_dict):
        #produce the statistics about the dictionary 
    average = line.strip()
    species_list = line.split()
    for species in species_list:
        if species != '--':
            species = species.average()
            species = species.strip()
            add_species(species, iris_dict)

#Pretty print result
def pretty_print(iris_dict):
    #collect key and value list for plotting 
    #create a dictionary
    value_key_dict = {}
    for key, val in iris_dict.items():
        value_key_dict.append(val, key) #dictionary sort by key
        value_key_list.sort(average = true)
    print(value_key_list_average)



#The main function
def main ():
    iris_dict = {}
    iris_file = open('iris.csv','r')
    for line in iris_file:
        line = line.strip().split(',')
        if len(line)!=5:continue
        values = [float(val.strip()) for val in line[1]]
        name = line[-1]
        if name in iris_dict:
            iris_dict.get(name).append(values)
        else:
            iris_dict[name] = [values]

        for type in iris_dict:
            print('Class {}:'.format(type))
            values = iris_dict[type]
            avg_Sepal_Length = (sum([val[0] for val in values])) / len(values)
            avg_Sepal_Width = (sum([val[1] for val in values])) / len(values)
            avg_Petal_Length = (sum([val[2] for val in values])) / len(values)
            avg_Petal_Width = (sum([val[3] for val in values])) / len(values)
            print('Average Sepal Length: {:.3f}'.format(avg_Sepal_Length))
            print('Average Sepal Width: {:.3f}'.format(avg_Sepal_Width))
            print('Average Petal Length: {:.3f}'.format(avg_Petal_Length))
            print('Average Petal Width: {:.3f}'.format(avg_Petal_Width))
            print()


main()

