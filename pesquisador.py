import requests
from lxml import html

def main():
    # Apenas cursos de ciencia e sistemas
    ifes = requests.get('http://sisu.mec.gov.br/selecionados?co_oferta=127115')
    tree = html.fromstring(ifes.content)
    lista_ifes = [a.text for a in tree.xpath('//td') if a.attrib['class'] == 'no_candidato']

    cursos = requests.get('http://www4.ccv.ufes.br/ps2016/ps2016_Etp2_Resultado_Curso.htm')
    tree = html.fromstring(cursos.content)
    lista_cursos = [a for a in tree.xpath('//a')]
    print(lista_cursos)

    ufes = requests.get('http://www4.ccv.ufes.br/ps2016/ps2016_Etp2_ENGENHARIA_DE_COMPUTACAO_Bach_Integral.htm')
    tree = html.fromstring(ufes.content)
    lista_ufes_engenharia = [a.text[1:] for a in tree.xpath('//td') if 'class' in a.attrib and a.attrib['class'] == 'nome']


    ufes = requests.get('http://www4.ccv.ufes.br/ps2016/ps2016_Etp2_CIENCIA_DA_COMPUTACAO_Bach_Integral.htm')
    tree = html.fromstring(ufes.content)
    lista_ufes_ciencia = [a.text[1:] for a in tree.xpath('//td') if 'class' in a.attrib and a.attrib['class'] == 'nome']


    interseccao = [nome for nome in lista_ifes if nome in lista_ufes_engenharia or nome in lista_ufes_ciencia]

    escreve(lista_ufes_engenharia, "EngenhariaUfes.txt")
    escreve(lista_ufes_ciencia, "CienciaUfes.txt")
    escreve(lista_ifes, "SistemasIfes.txt")

    escreve(interseccao, "PassaramIfesMasPassaramUfes.txt")
    
    
    
    
def main2():
    # Curso Ifes x todos da ufes
    ifes = requests.get('http://sisu.mec.gov.br/selecionados?co_oferta=127115')
    tree = html.fromstring(ifes.content)
    lista_ifes = [a.text for a in tree.xpath('//td') if a.attrib['class'] == 'no_candidato']

    cursos = requests.get('http://www4.ccv.ufes.br/ps2016/ps2016_Etp2_Resultado_Curso.htm')
    tree = html.fromstring(cursos.content)
    lista_cursos = [a.attrib['href'] for a in tree.xpath('//a') if 'href' in a.attrib]
    intersecao = {}
    for url in lista_cursos:
        ufes = requests.get('http://www4.ccv.ufes.br/ps2016/' + url)
        tree = html.fromstring(ufes.content)
        
        lista = [a.text[1:] for a in tree.xpath('//td') if 'class' in a.attrib and a.attrib['class'] == 'nome' and a.text != None]
        #print(lista)
        for nome in lista:
            if nome in lista_ifes:
                if url not in intersecao:
                    intersecao[url] = []
                intersecao[url].append(nome)

    #print(intersecao)
    escreve_dic(intersecao)
    
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
    



