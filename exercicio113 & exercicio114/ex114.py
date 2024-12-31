import requests # O professor usou a biblioteca urllib
# import urllib
# import urllib.request
def verSite(url):
    try:
        siteView = requests.get(url)
        # siteView = urllib.request.urlopen(url)
        print('\033[33mConsegui estabelecer conexão com a URL fornecida.\033[m')
    except:
        print('\033[31mErro! Não consegui estabelecer conexão com a URL fornecida. \033[m')  
    
verify = str(input('Insira uma URL: '))
verSite(verify)
# O professor queria que fosse verificar se o site do Pudim estava no ar. Porém, estava tentando
# fazer o teste com a URL do site, mas o programa não estava funcionando com a URL do pudim. Mas
# está funcionando em outras URLs.
