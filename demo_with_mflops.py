import subprocess
from pyswarm import pso
import pants
import math
import random

def getMflops(output):
    result = ""
   
    try:
        lines = output.read().split("\n")
        for line in lines:
            if line.__contains__("throughput"):  
                result = line
    finally:
        output.close();

    if result is None:
        flops = -1;
    else:
        flops = int(''.join(i for i in result if i.isdigit()))

    return flops

def iso3dfd(threads, cache_block_d1):
# size of the problem in three dimensions
    n1 = "256"
    n2 = "256"
    n3 = "256"

    # number of threads
    num_threads = str(threads)
    
    # number of iterations
    nreps = "100"

    # cache blocking for each dimension
    n1_thrd_block = str(cache_block_d1)
    n2_thrd_block = "12"
    n3_thrd_block = "30"

    output = os.popen("bin/iso3dfd_dev13_cpu_avx.exe " + n1 + " " + n2 + " " + n3 + " " + num_threads + " " + nreps + " " + n1_thrd_block + " " + n2_thrd_block + " " + n3_thrd_block)

    throughput = getMflops(output)
    
    return throughput


if __name__ == '__main__':
    print(iso3dfd(32,256))
