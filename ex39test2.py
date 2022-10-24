#test dict
states = {'Lagos': 'Ikeja',
        'Ondo': 'Akure',
        'Kaduna': 'Jos'}

cities = {'Lagos': 'Lag',
          'Ondo': 'ON',
          'Kaduna': 'KN'}


#Key to remember u always use the key in a dictionary to lookup a value
# Items ==> 1 Dictionary
#Items ==> 2 Key
# Item ==> 3 value
#To get the value of an item:==> Syntax ==>  Dictionary[Key name/number]
for i, k in  list(states.items()):
    print(list(cities.items()))
    print(i, k)
    print(">>> i=", i, "k =", k)
    print(f"has an abbreviation of {cities[i]}")
    print("<<< cities[i] =", cities[i])
