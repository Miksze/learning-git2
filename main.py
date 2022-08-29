print("lista zakupów")
lista = {'piekarni': ["chleb", "pączek", "bułki"], 'warzywniaka':["marchew","seler","rukola"]}

for x, y in (lista.items()):
   
    print(f"Idę do  { x.capitalize()},   kupię tu następujące rzeczy:  {y}")

count = { k: len(v) for k, v in lista.items() }
count2 = sum(count.values())
print( f"W sumie kupię {count2} produktów." ) 
