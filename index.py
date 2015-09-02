for x in range (101):
        if x%3==0 and x%5==0:
            print("fizz buzz")
        elif x%3==0:
            print('fizz')
        elif x%5==0:
            print('buzz')
        else:
            print (x)


================================

for x in range(1,101):
		s = ""
		if x % 3 == 0:
			s += "Fizz"
		if x % 5 == 0:
			s += "Buzz"
		if s == "":
			s = x
		print (s)
==============================
    for i in range(1, 101):
        if i % 15 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print (i)
================================

for x in range(1,101):
		s = ""
		if x % 3 == 0:
			s += "Fizz"
		if x % 5 == 0:
			s += "Buzz"
		print (s or x)
