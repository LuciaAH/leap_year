def leap_year(year):
	if year % 4 != 0:
		return '平年'
	elif year % 4 == 0 and year % 100 != 0:
		return '閏年'
	elif year % 100 == 0 and year % 400 != 0:
		return '平年'
	elif year % 400 == 0 and year % 3200 != 0:
		return '閏年'

print(leap_year(int(input('請輸入年分：'))))