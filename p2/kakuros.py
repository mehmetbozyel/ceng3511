from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
from ortools.sat.python import cp_model

print(sys.argv[1])

kakuroinp = open(sys.argv[1], "r")

line1 = kakuroinp.readline()
line1 = line1.strip("\n")
line1 = line1.split(", ")
print(line1)
line2 = kakuroinp.readline()
line2 = line2.strip("\n")
line2 = line2.split(", ")
print(line2)

"""
with open("kakuro_input.txt", "r") as kakuro:
    line1 = kakuro.readline()
    line1 = line1.strip("\n")
    line1 = line1.split(", ")
    print(line1)
    line2 = kakuro.readline()
    line2 = line2.strip("\n")
    line2 = line2.split(", ")
    print(line2)"""

model = cp_model.CpModel()

#Variables
a1 = model.NewIntVar(1, 9, 'a1')
a2 = model.NewIntVar(1, 9, 'a2')
a3 = model.NewIntVar(1, 9, 'a3')
b1 = model.NewIntVar(1, 9, 'b1')
b2 = model.NewIntVar(1, 9, 'b2')
b3 = model.NewIntVar(1, 9, 'b3')
c1 = model.NewIntVar(1, 9, 'c1')
c2 = model.NewIntVar(1, 9, 'c2')
c3 = model.NewIntVar(1, 9, 'c3')


model.AddAllDifferent([a1, a2, a3])
model.AddAllDifferent([b1, b2, b3])
model.AddAllDifferent([c1, c2, c3])

model.AddAllDifferent([a1, b1, c1])
model.AddAllDifferent([a2, b2, c2])
model.AddAllDifferent([a3, b3, c3])


model.Add(a1+a2+a3 == int(line2[0]))
model.Add(b1+b2+b3 == int(line2[1]))
model.Add(c1+c2+c3 == int(line2[2]))

model.Add(a1+b1+c1 == int(line1[0]))
model.Add(a2+b2+c2 == int(line1[1]))
model.Add(a3+b3+c3 == int(line1[2]))

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
    fileOutput = open("kakuro_output.txt", "w+")
    fileOutput.write("x, {0}, {1}, {2}\n".format(line1[0], line1[1], line1[2]))
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(line2[0], solver.Value(a1), solver.Value(a2), solver.Value(a3)))
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(line2[1], solver.Value(b1), solver.Value(b2), solver.Value(b3)))
    fileOutput.write("{0}, {1}, {2}, {3}".format(line2[2], solver.Value(c1), solver.Value(c2), solver.Value(c3)))
    fileOutput.close()
