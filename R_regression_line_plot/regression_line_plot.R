# This R environment comes with all of CRAN preinstalled, as well as many other helpful packages
# The environment is defined by the kaggle/rstats docker image: https://github.com/kaggle/docker-rstats
# For example, here's several helpful packages to load in 

library(ggplot2) # Data visualization
library(readr) # CSV file I/O, e.g. the read_csv function
library(gridExtra)
library(grid)
library(plyr)

# Load the dataset
iris=read.csv('/home/ivan/python-programming/R_regression_line_plot/iris.csv')


# First let's get a random sampling of the data
iris[sample(nrow(iris),10),]

ggplot(data = iris, aes(x = petal_length, y = petal_width))+
  xlab("Petal Length")+
  ylab("Petal Width") +
  geom_point(aes(color = Species,shape=Species))+
  geom_smooth(method='lm')+
  ggtitle("Petal Length vs Width")

