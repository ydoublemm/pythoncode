#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

last_year_score = 72
this_year_score = 85
print('提升百分比 %.1f%%' % ((this_year_score-last_year_score)/last_year_score*100))