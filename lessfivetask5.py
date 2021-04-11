slovar = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
for key, value in dict(slovar).items():
    if value == None:
        del slovar[key]
        print(slovar)
