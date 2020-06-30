

rm(list = ls())
setwd(choose.dir())

library(tidyverse)
library(ggpubr)
library(reshape2)
library(ggbeeswarm)

sem <- function(x) sqrt(var(x)/length(x))


df <- read.csv('index_per_mouse.csv')

df <- filter(df, genotype == 'C57BL/6' | genotype == '5XFAD')

df_grouped <- df %>%
  group_by(genotype, label) %>%
  summarise(sem = sem(index), index = mean(index))


ggplot(df, aes(x = interaction(genotype, label), y = index, color = genotype, fill = genotype))+
  geom_bar(df_grouped, mapping = aes(x = interaction(genotype, label), y = index), stat = 'identity')+
  geom_quasirandom(color = 'black')+
  geom_errorbar(df_grouped, mapping = aes(ymin = index - sem, ymax = index + sem), color = 'black', width = 0.02)+
  ggtitle('Keren-Shaul 2017, DAM Paper')+
  theme_classic()+
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1)
    
  )

output <- aov(index ~ genotype, data = df)

summary(output)

