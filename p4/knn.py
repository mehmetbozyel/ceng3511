import time
import matplotlib.pyplot as plt
from csv import reader
from math import sqrt

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	del dataset[0]
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column])

# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	#print("Correct Result: " , correct)
	return correct / float(len(actual)) * 100.0

# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction

# kNN Algorithm
def k_nearest_neighbors(train, test, num_neighbors = 3):
	predictions = list()
	for row in test:
		output = predict_classification(train, row, num_neighbors)
		predictions.append(output)
	return(predictions)


trainset = load_csv('train.txt')
for i in range(len(trainset[0])-1):
	str_column_to_float(trainset, i)

testset = load_csv('test.txt')
for i in range(len(testset[0])-1):
	str_column_to_float(testset, i)

# create actual
actual = list()
for i in range(len(testset)):
    actual.append(testset[i][-1])


x_axis = list() # k value
y_axis = list() # accuracy
print("Please wait, Program is running...........")
ts = time.time()
for kValue in range(3,10):
	x_axis.append(kValue)
	predicted = k_nearest_neighbors(trainset, testset,kValue)
	accuracy = accuracy_metric(actual, predicted)
	y_axis.append(accuracy)
	#print('Mean Accuracy: %.3f%%' % (accuracy))
te = time.time()
print("Program is finished. Program takes ", ((te - ts), " time"))

f = plt.figure()
plt.plot(x_axis, y_axis)
plt.xlabel('K Values')
plt.ylabel('Accuracy(%)')
plt.title('Mobile Price KNN Classification')
f.savefig("plot.pdf", bbox_inches='tight')
plt.close()
