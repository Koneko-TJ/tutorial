import requests
from bs4 import BeautifulSoup

def main():
    # Shiny colors URL
    url = "https://wikiwiki.jp/shinycolors/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    elements_1 = soup.find_all("a")
    
    link_list = []
    with open("IMSC_HTML_List.txt", mode = 'w') as f:
        for i in elements_1:
            link_list.append(i)
            f.write(str(i) + "\n")
            #print(i)
            
    linkAndMemberUser = link_list[107:136]
    
    charaURL_list = []
    charaName_list = []
    for i in linkAndMemberUser:
        charaURL_list.append\
            (str(i).replace('<a href="/shinycolors/', '').split('"')[0])
        charaName_list.append\
            (str(i).replace('<a href="/shinycolors/', '').split('>')[1].replace('</a', ''))
            
    with open("charactorURL_List.txt", mode = 'w') as f:
        for i in charaURL_list:
            f.write(str(url + i + "\n"))
            #print(i)
            
    with open("charactorName_List.txt", mode = 'w') as f:
        for i in charaName_list:
            f.write(str(i + "\n"))
            #print(i)

main()