
library(arules)
df_pf <- read.csv("C://Users//sidac//Desktop//Capstone//workspace//pre_arm_pf_distance_F20.csv")

df_pf2 <- df_pf[,-1]

trans <- as(df_pf2>0, "transactions")

rules <-apriori(data = trans, parameter = list(support = 0.01, confidence = 0.7))
real_rules <- subset(rules, subset = rhs %in% c('Passed','Failed'))
inspect(real_rules)


###########################################


#with clusters
library(arules)
df_pf <- read.csv("C://Users//sidac//Desktop//Capstone//workspace//pre_arm_pf_distance_with_clusters_F20.csv")

df_pf2 <- df_pf[,-1]

trans <- as(df_pf2>0, "transactions")

rules <-apriori(data = trans, parameter = list(support = 0.01, confidence = 0.6))
real_rules <- subset(rules, subset = rhs %in% c('Passed','Failed'))
inspect(real_rules)
