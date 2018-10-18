from bs4 import BeautifulSoup
import requests
import requests_cache

requests_cache.install_cache('demo_cache')

def download(url, num_retries=2):
    page = None
    try:
        response = requests.get(url)
        page = response.text
    except requests.exceptions.RequestException as e:
        print('Download error:', e.reason)
    return page



def menu():
    url = 'http://www.tce.pi.gov.br/'
    html = download(url)
    soup = BeautifulSoup(html, 'html.parser')
    tr = soup.find(attrs={'id': 'latestnews'})
    td = tr.find(attrs={'class': 'latestnews'})
    tf = td.find_all(attrs={'class': 'latestnews'})
    linklist = []
    contador = 1
    for link in tf:
        a = link.find(attrs={'class': 'latestnews'})
        if a is not None:
            print(str(contador) + ' - ' + a.text)
            linklist.append([link, contador])
            contador += 1
    print('6 - Sair')

    ver_noticia(linklist)

def mostrar_texto(url, num_retries=2):
    html = download(url)
    soup = BeautifulSoup(html, 'html.parser')
    tr = soup.find(attrs={'class':'the_post post_content'})
    td = tr.find_all('p')
    for p in td:
        print(p.text + '\n')


def ver_noticia(linklist):
    opcao = input('Escolha uma opcao: ')
    if opcao == '1':
        a = linklist[0][0].find(attrs={'class': 'latestnews'});
        link = a['href']
        mostrar_texto(link)
        menu();
    elif opcao == '2':
        a = linklist[1][0].find(attrs={'class': 'latestnews'});
        link = a['href']
        mostrar_texto(link)
        menu();
    elif opcao == '3':
        a = linklist[2][0].find(attrs={'class': 'latestnews'});
        link = a['href']
        mostrar_texto(link)
        menu();
    elif opcao == '4':
        a = linklist[3][0].find(attrs={'class': 'latestnews'});
        link = a['href']
        mostrar_texto(link)
        menu();
    elif opcao == '5':
        a = linklist[4][0].find(attrs={'class': 'latestnews'});
        link = a['href']
        mostrar_texto(link)
        menu();


menu()
