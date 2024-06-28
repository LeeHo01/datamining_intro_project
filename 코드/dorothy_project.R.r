setwd("d:/data_analysis")
install.packages("arules")
library(arules)
#기초 패키지 다운드

dorothy<-read.transactions("Selected_Menu.txt",format="basket" ,sep=",")
#텍스트파일로 골라진 메뉴를 옮긴 후, dorothy 객체로 옮겨놓기

summary(dorothy)
#기본적인 확인(가장 많이 선택된 메뉴 등)

itemFrequency(dorothy[,1:46])
itemFrequencyPlot(dorothy, support = 0.1)
itemFrequencyPlot(dorothy, topN = 10)
#순서대로 전체 지지도, 지지도가 0.1을 넘는 플랏, 지지도 순위대로 10개 줄세우기.

dorothy_rules <- apriori(data = dorothy, parameter = list(support=0.05, confidence=0.1, minlen=2))
dorothy_rules
summary(dorothy_rules)
inspect(dorothy_rules)
#모델 학습
#순서대로 최소 지지도, 최소 신뢰도, 최소 규칙 제품 설정.
#값을 계속 변경하면서 규칙을 찾아야 함.