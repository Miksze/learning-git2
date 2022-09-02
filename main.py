print("lista zakupów")
lista = {'piekarni': ["chleb", "pączek", "bułki"], 'warzywniaka':["marchew","seler","rukola"]}

for x, y in (lista.items()):
   
    print(f"Idę do  { x.capitalize()},   kupię tu następujące rzeczy:  {y}")

count = { k: len(v) for k, v in lista.items() }
count2 = sum(count.values())
print( f"W sumie kupię {count2} produktów." ) 
# Zadanie 2
zbior = []
for i in range(0,100):
    if i % 5 == 0:
        zbior.append(i)
print(zbior)
x3 = [number * number * number for number in zbior]
print(f"Te sześciany {x3}")
#zadanie 3
print(commit)
# zadanie 4
print(test)