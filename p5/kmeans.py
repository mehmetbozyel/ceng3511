import math
import random
from csv import reader
import matplotlib.pyplot as plt

k = int(input("Select k point (Between 1 and 10)  "))

def load_csv(filename = "data.txt"):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	del dataset[0]
	return dataset

dataset = load_csv()
income = list()
speed = list()

for row1,row2 in dataset:
	income.append(int(row1))
	speed.append(int(row2))

def kPointSelection(x_axis,y_axis,k):
    x_axis =x_axis.copy()
    y_axis = y_axis.copy()
    x_axis.sort()
    y_axis.sort()

    points = []
    for i in range(k):
        tempList = []
        x = random.randrange(x_axis[0], x_axis[-1])
        y = random.randrange(y_axis[0], y_axis[-1])
        tempList.append(x)
        tempList.append(y)
        points.append(tempList)
    return points

selectedPoints = kPointSelection(income,speed,k)

x_axis_point = list()
y_axis_point = list()
for xpoint,ypoint in selectedPoints:
	x_axis_point.append(xpoint)
	y_axis_point.append(ypoint)

def k_means_clustering(point_coordinate,data_coordinate,k):
	allData = list()
	for _ in range(k):
		allData.append([])
	for data1,data2 in data_coordinate:
		tempList = []
		for point1,point2 in point_coordinate:
			distance = (((point1) - (int(data1))) ** 2) + (((point2) - (int(point2))) ** 2)
			distance = math.sqrt(distance)
			tempList.append(distance)
			min_index = int()
			minVal = min(tempList)
		for index, value in enumerate(tempList):
			if value == minVal:
				min_index = index

		for i in range(k):
			if min_index == i:
				allData[i].append([data1,data2])
	return allData

result = k_means_clustering(selectedPoints, dataset, k)
print(result)

color = ["ro","bo","go","mo","ko","co","r^","m^","g^","b^"]

x_axis = list()
y_axis = list()
last = k - 1

for data_row in result:
	for dataRow1,dataRow2  in data_row:
		x_axis.append(int(dataRow1))
		y_axis.append(int(dataRow2))

	index = random.randint(0, last)
	plt.plot(x_axis, y_axis, color[index])
	del color[index]

	x_axis.clear()
	y_axis.clear()
	last -= 1


plt.plot(x_axis_point,y_axis_point,"y*",label="Points")
plt.xlabel("income")
plt.ylabel("spend")
plt.title("K-means clustering")

fig = plt.gcf()
plt.show()
fig.savefig("plot.pdf")