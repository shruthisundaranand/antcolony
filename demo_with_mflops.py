import sys, string, os
import subprocess
from pyswarm import pso
import pants
import math
import random

def iso3dfd(threads, cache__block_d1):
# size of the problem in three dimensions
    n1 = "256"
    n2 = "256"
    n3 = "256"

    # number of threads
    #num_threads = "32"
    num_threads = string(threads)
    
    # number of iterations
    nreps = "100"

    # cache blocking for each dimension
    #n1_thrd_block = "256" #str(parms[1])
    n1_thrd_block = string(cache_block_d1)
    n2_thrd_block = "12" #str(parms[2])
    n3_thrd_block = "30" #str(parms[3])

    throughput = os.popen("bin/iso3dfd_dev13_cpu_avx.exe " + n1 + " " + n2 + " " + n3 + " " + num_threads + " " + nreps + " " + n1_thrd_block + " " + n2_thrd_block + " " + n3_thrd_block)

    # Output = os.system("bin/iso3dfd_dev13_cpu_avx.exe " + n1 + " " + n2 + " " + n3 + " " + num_threads + " " + nreps + " " + n1_thrd_block + " " + n2_thrd_block + " " + n3_thrd_block  + " | grep 'throughput' | tr -s ' ' | cut -f2 -d ' '")

    return throughput
   

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def getMflops(output):
    # replace the above ls -l with the actual exe
    result = ""
   
    try:
        lines = output.read().split("\n")
        for line in lines:
            if line.__contains__("throughput"):  # change the "iso-3dfd_main.cc" to throughput
                result = line
    finally:
        output.close();

    if result is None:
        flops = -1;
    else:
        flops = int(''.join(i for i in result if i.isdigit()))

    return flops

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    output = os.popen("bin/iso3dfd_dev13_cpu_avx.exe")
    print(getMflops(output))
