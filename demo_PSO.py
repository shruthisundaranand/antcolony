import sys, string, os
import subprocess
from pyswarm import pso
import pants
import math
import random

def get_throughput(output):
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

def iso3dfd(threads, cache_block_d1, cache_block_d2, cache_block_d3):
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
    n2_thrd_block = str(cache_block_d2)
    n3_thrd_block = str(cache_block_d2)

    output = os.popen("bin/iso3dfd_dev13_cpu_avx.exe " + n1 + " " + n2 + " " + n3 + " " + num_threads + " " + nreps + " " + n1_thrd_block + " " + n2_thrd_block + " " + n3_thrd_block)

    throughput = get_throughput(output)
    
    return throughput

#print(iso3dfd(32,256))

nodes = []
for _ in range(10):
    x = random.uniform(10, 30)
    y = random.uniform(100, 200)
    nodes.append((x, y))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

#    world = pants.World(nodes, iso3dfd)
#    solver = pants.Solver()
#    solution = solver.solve(world)
#    print(solution.distance)
#    print(solution.tour)  # Nodes visited in order
#    print(solution.path)  # Edges taken in order
#    print("\n")
    
    # best = float("inf")
    # for solution in solutions:
    #     if solution.distance < best:
    #         best = solution.distance
    # print(best)

lb = [31, 255, 11, 29]
ub = [32, 256, 12, 30]

xopt, fopt = pso(iso3dfd, lb, ub)

print(xopt)
print(fopt)
