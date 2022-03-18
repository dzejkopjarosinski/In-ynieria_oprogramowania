def hello(name):
	return "Hello" + str(name)

def dodaj(a,b):
	wynik = float(a) + float(b)
	return wynik

def odejmi(a,b):
	wynik = float(a) - float(b)
	return wynik


pierwsza = input()
druga = input()

print(dodaj(pierwsza,druga))
print(odejmi(pierwsza,druga))

