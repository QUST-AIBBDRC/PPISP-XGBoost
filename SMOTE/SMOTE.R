
#SMOTE
VnewData <- SMOTE(cla ~ ., X164ub, perc.over = m, perc.under=m*2)
table(VnewData$cla)

library(DMwR)

require(methods)

setwd("D: ")
data_train = read.csv(" .csv",header = F)
data_train$V1=factor(data_train$V1)
train_data_SMOTEdata <- SMOTE(V1~.,data_train,perc.over =m, perc.under=m*2)
jishu<-table(train_data_SMOTEdata$V1)

write.csv(train_data_SMOTEdata,file='out_SMOTE.csv')



