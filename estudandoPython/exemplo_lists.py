states = [ 'Alabama','Alaska','Arizona','Arkansas','California',
            'Colorado','Connecticut','Delaware','Florida','Georgia',
            'Hawaii','Idaho','Illinois','Indiana','Iowa',
            'Kansas','Kentucky','Louisiana','Maine','Maryland',
            'Massachusetts','Michigan','Minnesota','Mississippi','Missouri',
            'Montana','Nebraska','Nevada','New Hampshire','New Jersey',
            'New Mexico','New York','North Carolina','North Dakota','Ohio',
            'Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina',
            'South Dakota','Tennessee','Texas','Utah','Vermont',
            'Virginia','Washington','West Virginia','Wisconsin','Wyoming' ]

def mostraEstados(list):
    x = 0
    while x < list.__len__():
        print(f"{x+1} - {list[x]}")
        x += 1

def mostraEstadosM(list):
    x = 0
    while x < list.__len__():
        if (list[x].startswith('M')):
            print(f"{x+1} - {list[x]}")
        x += 1
           

#mostraEstados(states) 
#mostraEstadosM(states) 

list_ = [ (3,6), (4,7), (5,9), (8,4), (3,1) ]
list_.sort(key=lambda x: x[1])
print(list_)

