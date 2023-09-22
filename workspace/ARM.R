library(arules)

data("IncomeESL")
trans <- transactions(IncomeESL)
rules <- apriori(trans, supp = 0.1, conf = 0.9, target = "rules")

inspect(head(rules, n = 3, by = "lift"))


######################################################

df <- read.csv("C://Users//sidac//Desktop//Capstone//workspace//pre_arm_F20.csv")

df2 <- df[,-1]

trans <- as(df2>0, "transactions")

rules <-apriori(data = trans, parameter = list(support = 0.01, confidence = 0.6))
real_rules <- subset(rules, subset = rhs %in% c('Good','Fair','Poor'))
inspect(real_rules)

######################################################

df_pf <- read.csv("C://Users//sidac//Desktop//Capstone//workspace//pre_arm_pf_F20.csv")

df_pf2 <- df_pf[,-1]

trans <- as(df_pf2>0, "transactions")

rules <-apriori(data = trans, parameter = list(support = 0.01, confidence = 0.6))
real_rules <- subset(rules, subset = rhs %in% c('Passed','Failed'))
inspect(real_rules)

p_rules <- subset(rules, subset = rhs %in% 'Passed')
f_rules <- subset(rules, subset = rhs %in% 'Failed')
inspect(p_rules)
inspect(f_rules)


########################################################

#with clusters
library(arules)
df_pf <- read.csv("C://Users//sidac//Desktop//Capstone//workspace//pre_arm_pf_with_clusters_F20.csv")

df_pf2 <- df_pf[,-1]

trans <- as(df_pf2>0, "transactions")

rules <-apriori(data = trans, parameter = list(support = 0.01, confidence = 0.6))
real_rules <- subset(rules, subset = rhs %in% c('Passed','Failed'))
inspect(real_rules)

########################################################

#with clusters
#high and medium exchanged
library(arules)
df_pf <- read.csv("C://Users//sidac//Desktop//Capstone//workspace//pre_arm_pf_with_clusters_corrected_F20.csv")

df_pf2 <- df_pf[,-1]

trans <- as(df_pf2>0, "transactions")

rules <-apriori(data = trans, parameter = list(support = 0.01, confidence = 0.6))
real_rules <- subset(rules, subset = rhs %in% c('Passed','Failed'))
inspect(real_rules)
