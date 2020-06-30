


rm(list = ls())
setwd(choose.dir())

library(tidyverse)
library(ggpubr)
library(reshape2)
library(ggbeeswarm)

sem <- function(x) sqrt(var(x)/length(x))


df <- read.csv('calculated_index.csv')

df$age <- factor(df$age, levels = c('E14', 'P4', 'P30', 'P100', 'Old'))
df$sex <- factor(df$sex, levels = c('M', 'F'))
df$tx <- factor(df$tx, levels = c('N/A', 'Sal', 'Lpc'))

df_grouped <- df %>%
  group_by(age, sex, tx) %>%
  summarise(sem = sem(Index), mean = mean(Index))


ggplot(df, aes(x = interaction(sex, age, tx), y = Index, fill = interaction(sex, age)))+
  #geom_bar(stat = 'identity', df_grouped, mapping = aes(x = interaction(sex, age, tx), y = mean, fill = interaction(sex, age)))+
  geom_quasirandom(size = 8, shape = 21, color = 'black')+
  geom_errorbar(data = df_grouped, mapping = aes(x = interaction(sex, age, tx), y = mean, ymin = mean - sem, ymax = mean + sem), color = 'black', width = .2)+
  theme_classic()+
  ggtitle('Stevens 2019, MGLA Development')+
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1)
    
  )



