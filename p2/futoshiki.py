from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from ortools.sat.python import cp_model

model = cp_model.CpModel()

#Variables
A1 = model.NewIntVar(1, 4, 'A1')
A2 = model.NewIntVar(1, 4, 'A2')
A3 = model.NewIntVar(1, 4, 'A3')
A4 = model.NewIntVar(1, 4, 'A4')

B1 = model.NewIntVar(1, 4, 'B1')
B2 = model.NewIntVar(1, 4, 'B2')
B3 = model.NewIntVar(1, 4, 'B3')
B4 = model.NewIntVar(1, 4, 'B4')

C1 = model.NewIntVar(1, 4, 'C1')
C2 = model.NewIntVar(1, 4, 'C2')
C3 = model.NewIntVar(1, 4, 'C3')
C4 = model.NewIntVar(1, 4, 'C4')

D1 = model.NewIntVar(1, 4, 'D1')
D2 = model.NewIntVar(1, 4, 'D2')
D3 = model.NewIntVar(1, 4, 'D3')
D4 = model.NewIntVar(1, 4, 'D4')

model.AddAllDifferent([A1, A2, A3, A4])
model.AddAllDifferent([B1, B2, B3, B4])
model.AddAllDifferent([C1, C2, C3, C4])
model.AddAllDifferent([D1, D2, D3, D4])

model.AddAllDifferent([A1, B1, C1, D1])
model.AddAllDifferent([A2, B2, C2, D2])
model.AddAllDifferent([A3, B3, C3, D3])
model.AddAllDifferent([A4, B4, C4, D4])

futoshiki = open(sys.argv[1], "r")
for line in futoshiki:
    line = line.strip("\n")
    lineArray = line.split(", ")

    if lineArray[1].isdigit():
        model.Add(vars()[lineArray[0]] == int(lineArray[1]))
    else:
        model.Add(vars()[lineArray[0]] > vars()[lineArray[1]])


"""
with open("futoshiki_input.txt", "r") as futoshiki:
    for line in futoshiki:
        line = line.strip("\n")
        lineArray = line.split(", ")

        if lineArray[1].isdigit():
            model.Add(vars()[lineArray[0]] == int(lineArray[1]))
        else:
            model.Add(vars()[lineArray[0]] > vars()[lineArray[1]])
"""

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
    fileOutput = open("futoshiki_output.txt", "w+")
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(solver.Value(A1), solver.Value(A2), solver.Value(A3), solver.Value(A4)))
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(solver.Value(B1), solver.Value(B2), solver.Value(B3), solver.Value(B4)))
    fileOutput.write("{0}, {1}, {2}, {3}\n".format(solver.Value(C1), solver.Value(C2), solver.Value(C3), solver.Value(C4)))
    fileOutput.write("{0}, {1}, {2}, {3}".format(solver.Value(D1), solver.Value(D2), solver.Value(D3), solver.Value(D4)))
    fileOutput.close()
