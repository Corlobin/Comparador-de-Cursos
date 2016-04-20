import requests
from lxml import html

def main2():

    ufes = requests.get('http://www4.ccv.ufes.br/ps2016/ps2016_Etp2_Resultado_Curso.htm')
    tree = html.fromstring(ufes.content)
    lista = [a.text for a in tree.xpath('//a')]
    print(lista)
    #print(intersecao)
    #escreve_dic(intersecao)
    
def escreve_dic(lista):
    for url in lista.keys():
        nome_arquivo = "Lista/" + url + ".txt"
        arquivo = open(nome_arquivo, 'w+')
        for pessoa in lista[url]:
            arquivo.write(pessoa+"\n")
        arquivo.close()    


def escreve(lista, arquivo):
    arquivo = open(arquivo, 'w+')
    for item in lista:
        arquivo.write(item+"\n")
    arquivo.close()    

main2()
    



