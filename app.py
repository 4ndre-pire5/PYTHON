print("ola mundo")

def main():
    text = 'this is a text'
    text2 = "double quotes"
    integer_val = 30
    decimal_val = 30.50
    array = list()
    array2 = []
    dictionary = dict()
    dictionary2 = {}

    print(type(array))
    print(type(dictionary))

    x = 2
    x2 = raiz_quadrada(x)
    print(x2)

    loggerFct = logger_builder("[fct]")
    loggerObj = Logger("[obj]")

    loggerFct("txt to log...")
    loggerObj.log("txt to log...")


def raiz_quadrada(nro):
    return nro ** nro

def logger_builder(prefix):
    return lambda txt: print(f'{prefix}{txt}')
    
class Logger():
    def __init__(self, prefix):
        self.prefix = prefix

    def log(self, txt):
        print(f'{self.prefix}{txt}')

main()