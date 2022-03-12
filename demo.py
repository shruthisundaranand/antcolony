# Import system modules
import sys, string, os

# size of the problem in three dimensions
var1 = "256"
var2 = "256"
var3 = "256"

# number of threads
var4 = "4"

# number of iterations
var5 = "100"

# cache blocking for each dimension
var6 = "256"
var7 = "12"
var8 = "30"

os.system("bin/iso3dfd_dev13_cpu_avx.exe " + var1 + " " + var2 + " " + var3 + " " + var4 + " " + var5 + " " + var6 + " " + var7 + " " + var8)

