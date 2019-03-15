# This R environment comes with all of CRAN preinstalled, as well as many other helpful packages
# The environment is defined by the kaggle/rstats docker image: https://github.com/kaggle/docker-rstats
# For example, here's several helpful packages to load in 

library(ggplot2) # Data visualization
library(readr) # CSV file I/O, e.g. the read_csv function
library(gridExtra)
library(grid)
library(plyr)

# Load the dataset
iris=read.csv('/home/ivan/python-programming/R_correlation_plot/iris.csv')


# First let's get a random sampling of the data
iris[sample(nrow(iris),10),]

# Based on all the plots we have done we can see there is certain correlation. Let's take a look at the pairwise correlation numerical values to 
# ascertain the relationships in more detail.

library(GGally)
ggpairs(data = iris[1:4],
        title = "Iris Correlation Plot",
        upper = list(continuous = wrap("cor", size = 5)), 
        lower = list(continuous = "smooth")
)

