height = input('請輸入你的身高: ')
weight = input('請輸入你的體重: ')
bmi = float(weight)/(float(height)/100*float(height)/100)
print('你的BMI值是: ',bmi)
if bmi < 18.5:    
	print('體重過輕')
elif bmi >=18.5 and bmi < 24:
	print('正常範圍')
elif bmi >= 24 and bmi < 27:
	print('過重')
elif bmi >= 27 and bmi < 30:    
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:    
	print('肥胖')
else:
	print('too fat')