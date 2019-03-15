# This R environment comes with all of CRAN preinstalled, as well as many other helpful packages
# The environment is defined by the kaggle/rstats docker image: https://github.com/kaggle/docker-rstats
# For example, here's several helpful packages to load in 

#library(ggplot2) # Data visualization
library(readr) # CSV file I/O, e.g. the read_csv function
#library(gridExtra)
#library(grid)
#library(plyr)
library(qcc)


# Load the dataset
pistonrings=read.csv('/home/ivan/python-programming/R_qcc_process_capability_plot/pistonring.csv')

# List data
head(pistonrings,200)
#
diameter = with(pistonrings, qcc.groups(diameter, sample))
head(diameter,n=100)
q1 = qcc(diameter[1:25,], type="xbar", nsigmas=3, plot=FALSE)
process.capability(q1, spec.limits=c(73.95,74.05))

