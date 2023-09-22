#using "long" approach for mcWeather
weatherStates <- c("rainy", "nice", "sunny")
weatherMatrix <- matrix(data = c(0.50, 0.25, 0.25, 0.5, 0.0, 0.5, 0.25, 0.25, 0.5), byrow = TRUE, nrow = 3,dimnames = list(weatherStates, weatherStates))
mcWeather <- new("markovchain", states = weatherStates, byrow = TRUE, transitionMatrix = weatherMatrix, name = "Weather")

#using "quick" approach on Mathematica's DTMC
mathematicaMatr <- matrix(c(1/2, 1/2, 0, 0, 1/2, 1/2, 0, 0, 1/4, 1/4, 1/4, 1/4, 0, 0, 0, 1),byrow=TRUE, nrow=4)
mathematicaMc<-as(mathematicaMatr, "markovchain")


plot(mcWeather ^ 2, main="Weather Markov Chain")
mcWeather ^ 2

initialState <- c(0, 1, 0)
after2Days <- initialState * mcWeather
after2Daysp


plot(mathematicaMc)

###################################

transition_p <- c(0, 0, 0, 0, 0.72, 0.14, 0.12, 0.02, 0, 0, 0, 0, 0, 0, 0, 0, 0.38, 0.26, 0.21, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0.21, 0.43, 0.27, 0.09, 0, 0, 0, 0, 0, 0, 0, 0, 0.67, 0.0, 0.33, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.85, 0.12, 0.03, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.52, 0.24, 0.2, 0.04, 0, 0, 0, 0, 0, 0, 0, 0, 0.69, 0.22, 0.06, 0.03, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.64, 0.27, 0.09, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
names_1 <- c("Period-I-0", "Period-I-1", "Period-I-2", "Period-I-3", "Period-II-0", "Period-II-1", "Period-II-2", "Period-II-3")
names_2 <- c("Period-I-0", "Period-I-1", "Period-I-2", "Period-I-3", "Period-II-0", "Period-II-1", "Period-II-2", "Period-II-3", "Period-III-0", "Period-III-1", "Period-III-2", "Period-III-3")
periodMatrix <- matrix(data = transition_p, byrow = TRUE, nrow = 12,dimnames = list(names_2, names_2))
periodMc <- new("markovchain", states = names_2, byrow = TRUE, transitionMatrix = periodMatrix, name = "Period")

transition_p[transition_p == 1] <- 0

periodMc@transitionMatrix <- transition_p

plot(periodMc)

###################################

transition_p <- c(0, 0, 0, 0, 0.72, 0.14, 0.12, 0.02, 0, 0, 0, 0, 0, 0, 0, 0, 0.38, 0.26, 0.21, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0.21, 0.43, 0.27, 0.09, 0, 0, 0, 0, 0, 0, 0, 0, 0.67, 0.0, 0.33, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.85, 0.12, 0.03, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.52, 0.24, 0.2, 0.04, 0, 0, 0, 0, 0, 0, 0, 0, 0.69, 0.22, 0.06, 0.03, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.64, 0.27, 0.09, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
names_2 <- c("Period-I-0", "Period-I-1", "Period-I-2", "Period-I-3", "Period-II-0", "Period-II-1", "Period-II-2", "Period-II-3", "Period-III-0", "Period-III-1", "Period-III-2", "Period-III-3")
tm <- matrix(data = transition_p, byrow = TRUE, nrow = 12,dimnames = list(names_2, names_2))
mc <- new("markovchain", states=names_2, transitionMatrix=tm, name="Period")

tm[tm==1] <- 0
mc@transitionMatrix <- tm

plot(mc)

mcg.igraph <- as(mc, "igraph")
coords <- layout_in_circle(mcg.igraph)

#SCC <- clusters(mcg.igraph, mode="strong")
#V(mcg.igraph)$color <- rainbow(SCC$no)[SCC$membership]

plot(mc, layout = coords)


##################################

#with clusters

library(markovchain)
library(igraph)
library(igraphdata)
transition_p <- c(0, 0, 0, 0, 0.84, 0.04, 0.12, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0.7, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.52, 0.01, 0.47, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.03, 0.0, 0.0, 0.97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.8, 0.0, 0.2, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.09, 0.82, 0.09, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.16, 0.0, 0.84, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5)
names <- c("Period-I-High", "Period-I-Medium", "Period-I-Low", "Period-I-None", "Period-II-High", "Period-II-Medium", "Period-II-Low", "Period-II-None", "Period-III-High", "Period-III-Medium", "Period-III-Low", "Period-III-None")
tm <- matrix(data = transition_p, byrow = TRUE, nrow = 12,dimnames = list(names, names))
mc <- new("markovchain", states=names, transitionMatrix=tm, name="Period")

tm[tm==0.5] <- 0
mc@transitionMatrix <- tm

plot(mc)

mcg.igraph <- as(mc, "igraph")
coords <- layout_in_circle(mcg.igraph)

plot(mc, layout = coords)
