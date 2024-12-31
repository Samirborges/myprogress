def leiaDinheiro(value):
    while True:
        value = str(input('Digite um valor: R$')).strip()
        if value.isnumeric():
            value = float(value)
            break
            
        else:
            if ',' in value:
               value = value.replace(',', '.')
            
            if '.' in value:
                verify = value.index('.')
                if value[0: verify].isnumeric():
                    value = float(value)
                    break
            
            else:
                print(f'\033[1;31mErro:\033[m \033[31m"{value}" é um preço inválido!\033[m')
        
    return value

