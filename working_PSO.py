import sys, string, os
import subprocess
from pyswarm import pso
import pants
import math
import random

def get_throughput(output):
    throughput = 0.0
    result = ""
   
    try:
        lines = output.read().split("\n")
        for line in lines:
            if line.__contains__("throughput"):  
                result = line
    finally:
        output.close();

    if result is None:
        throughput = -1;
    else:
        for t in result.split():
            try:
                throughput = float(t)
            except ValueError:
                pass
                
    return throughput

def get_time(output):
    time = 100.0
    result = ""
   
    try:
        lines = output.read().split("\n")
        for line in lines:
            if line.__contains__("time"):  
                result = line
    finally:
        output.close();

    if result is None:
        time = -1;
    else:
        for t in result.split():
            try:
                time = float(t)
            except ValueError:
                pass
                
    return time

def iso3dfd_throughput(parms):
# size of the problem in three dimensions
    n1 = "256"
    n2 = "256"
    n3 = "256"

    # number of threads
    num_threads = str(parms[0])
    
    # number of iterations
    nreps = "100"

    # cache blocking for each dimension
    n1_thrd_block = str(parms[1])
    n2_thrd_block = str(parms[2])
    n3_thrd_block = str(parms[3])

    output = os.popen("bin/iso3dfd_dev13_cpu_avx.exe " + n1 + " " + n2 + " " + n3 + " " + num_threads + " " + nreps + " " + n1_thrd_block + " " + n2_thrd_block + " " + n3_thrd_block)

    output = -1.0*float(get_throughput(output))
    return output

def iso3dfd_time(parms):
# size of the problem in three dimensions
    n1 = "256"
    n2 = "256"
    n3 = "256"

    # number of threads
    num_threads = str(parms[0])
    
    # number of iterations
    nreps = "100"

    # cache blocking for each dimension
    n1_thrd_block = str(parms[1])
    n2_thrd_block = str(parms[2])
    n3_thrd_block = str(parms[3])

    output = os.popen("bin/iso3dfd_dev13_cpu_avx.exe " + n1 + " " + n2 + " " + n3 + " " + num_threads + " " + nreps + " " + n1_thrd_block + " " + n2_thrd_block + " " + n3_thrd_block)

    output = float(get_time(output))
    return output

lb = [31,255,1,1]
ub = [32,256,12,30]

default_parameters = [4,256,12,30]

default_time = iso3dfd_time(default_parameters)
print("default parameters:   256 256 256 4* 100 256* 12* 30*") 
print("time with default parameters: " + str(default_time))
print(" ")

xopt, fopt = pso(iso3dfd_time, lb, ub, maxiter=1) 
xopt_rounded = [math.ceil(xopt[0]), math.ceil(xopt[1]), round(xopt[2]), round(xopt[3])]
print(" ")

time_with_pso_parameters = iso3dfd_time(xopt_rounded)
#print("PSO optimized parameters: " + str(xopt_rounded))
print("optimized parameters: 256 256 256 " + str(xopt_rounded[0]) + " 100 " + str(xopt_rounded[1]) + " " + str(xopt_rounded[2]) + " " + str(xopt_rounded[3]))
print("PSO optimized time:           " + str(time_with_pso_parameters))

#testable = [31.84855215, 256, 3.24319125, 9.34893488]
#testable_rounded = [round(testable[0]), round(testable[1]), round(testable[2]), round(testable[3])]
#pso_testable = iso3dfd_time(testable)
#pso_testable_rounded = iso3dfd_time(testable_rounded)

#print("testable rounded parameters: " + str(testable_rounded))
#print("time with testable rounded: " + str(pso_testable_rounded))
