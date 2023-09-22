
library(markovchain)
library(igraph)
library(igraphdata)
transition_p <- c(0, 0, 0, 0, 0.53, 0.23, 0.18, 0.06, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0.61, 0.18, 0.11, 0, 0, 0, 0, 0, 0, 0, 0, 0.12, 0.19, 0.53, 0.16, 0, 0, 0, 0, 0, 0, 0, 0, 0.12, 0.14, 0.37, 0.37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0.1, 0.1, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0.11, 0.52, 0.21, 0.16, 0, 0, 0, 0, 0, 0, 0, 0, 0.12, 0.17, 0.31, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0.16, 0.11, 0.26, 0.47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
names <- c("Period-I-Most", "Period-I-Moderate", "Period-I-Least", "Period-I-None", "Period-II-Most", "Period-II-Moderate", "Period-II-Least", "Period-II-None", "Period-III-Most", "Period-III-Moderate", "Period-III-Least", "Period-III-None")
tm <- matrix(data = transition_p, byrow = TRUE, nrow = 12,dimnames = list(names, names))
mc <- new("markovchain", states=names, transitionMatrix=tm, name="Period")

tm[tm==1] <- 0
mc@transitionMatrix <- tm

plot(mc)

mcg.igraph <- as(mc, "igraph")
coords <- layout_in_circle(mcg.igraph)

plot(mc, layout = coords)


############################################

#with clusters

library(markovchain)
library(igraph)
library(igraphdata)
transition_p <- c(0, 0, 0, 0, 0.67, 0.33, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.05, 0.83, 0.11, 0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.49, 0.51, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.03, 0.0, 0.97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.75, 0.1, 0.1, 0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.82, 0.18, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.17, 0.83, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5)
names <- c("Period-I-High", "Period-I-Medium", "Period-I-Low", "Period-I-None", "Period-II-High", "Period-II-Medium", "Period-II-Low", "Period-II-None", "Period-III-High", "Period-III-Medium", "Period-III-Low", "Period-III-None")
tm <- matrix(data = transition_p, byrow = TRUE, nrow = 12,dimnames = list(names, names))
mc <- new("markovchain", states=names, transitionMatrix=tm, name="Period")

tm[tm==0.5] <- 0
mc@transitionMatrix <- tm

plot(mc)

mcg.igraph <- as(mc, "igraph")
coords <- layout_in_circle(mcg.igraph)

plot(mc, layout = coords)
