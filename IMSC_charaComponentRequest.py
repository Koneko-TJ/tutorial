import requests
from bs4 import BeautifulSoup

charaUrlList = []
charaNameList = []
groupNameList = []
cardList = []

searchUrl = ""

r = ""
soup = ""

recentSearchCardNumber = 0
recentCardCountValue = 0
recentProduceCardList = []
recentProduceCardUrl = "https://wikiwiki.jp"

idolEventListAll = []
idolEventList = []
cardWingEventList = []
cardFesEventList = []
cardGradEventList = []
morningEventList = []
beforeOditionSelectList = []



def printList(n = []):
    for i in n:
        print(i)



def fileLoadingToList():
    global charaUrlList
    global charaNameList
    global groupNameList
    
    
    
    with open("charactorURL_List.txt", mode = 'r') as f_url:
        with open("charactorName_List.txt", mode = 'r') as f_name:
            for i in f_url:
                charaUrlList.append(str(i.split("\n"))\
                                    .replace("['", '').replace("', '']", ''))
            for i in f_name:
                charaNameList.append(str(i.split("\n"))\
                                     .replace("['", '').replace("', '']", '')\
                                     .replace('["', '').replace(", '']", '')\
                                     .replace('"', ''))
        
    for i in charaNameList:
        j = charaNameList.index(i)
        if j in {0, 3, 8, 13, 16, 19}:
            charaUrlList.pop(j)
            groupNameList.append(charaNameList.pop(j))



def askingToUser():
    print()
    for i in groupNameList:
        print(str(groupNameList.index(i)+1) + ":  " + str(i))
    userInput_group = input("Please choose the group name: ")
    
    count = 0
    searchIndexNumber = 0
    if userInput_group == "1":
        searchIndexNumber = 0
        for i in charaNameList[0:3]:
            count += 1
            print (str(count) + ":  " + str(i))
    elif userInput_group == "2":
        searchIndexNumber = 3
        for i in charaNameList[3:8]:
            count += 1
            print (str(count) + ":  " + str(i))
    elif userInput_group == "3":
        searchIndexNumber = 8
        for i in charaNameList[8:13]:
            count += 1
            print (str(count) + ":  " + str(i))
    elif userInput_group == "4":
        searchIndexNumber = 13
        for i in charaNameList[13:16]:
            count += 1
            print (str(count) + ":  " + str(i))
    elif userInput_group == "5":
        searchIndexNumber = 16
        for i in charaNameList[16:19]:
            count += 1
            print (str(count) + ":  " + str(i))
    elif userInput_group == "6":
        searchIndexNumber = 19
        for i in charaNameList[19:23]:
            count += 1
            print (str(count) + ":  " + str(i))
            
    userInput_name = input("Please choose the charactor name: ")
    
    global searchUrl
    searchUrl = str(charaUrlList[searchIndexNumber + int(userInput_name) - 1])



def produceCardVacume():
    r = requests.get(searchUrl)
    soup = BeautifulSoup(r.text, "html.parser")
    elements_1 = soup.select(".contents")
    
    cardTextList = []
    elements_2 = ""
    
    for i in elements_1:
        elements_2 += str(i.getText())
        
    cardTextList = elements_2.split("\n")
    while ('' in cardTextList):
        cardTextList.remove('')
    
    for i in cardTextList:
        if('サポート' in i):
            break
        elif('プロデュース' in i):
            continue
        else:
            recentProduceCardList.append(i)
            
    
    
def askingWhatCardToUser():
    print()
    count = 1
    for i in recentProduceCardList:
        if(('SSR' in i) or ('SR' in i) or ('R' in i)):
            print(i)
        else:
            print(str(count) + ": " + i)
            count += 1
            
    global recentCardCountValue
    recentCardCountValue = count
            
    userInput_card = input("Please choose the card: ")
    
    global recentSearchCardNumber
    recentSearchCardNumber = int(userInput_card)
    
    
    
def searchCardUrl():
    r = requests.get(searchUrl)
    soup = BeautifulSoup(r.text, "html.parser")
    elements_1 = soup.select("h4 a")
    
    cardUrlList = []
    
    for i in elements_1:
        cardUrlList.append(i.get("href"))
        
    while(None in cardUrlList):
        cardUrlList.remove(None)
        
    global recentProduceCardUrl
    recentProduceCardUrl = "https://wikiwiki.jp" + str(cardUrlList[(recentSearchCardNumber-1)*2])
    
    
    
    
def cardInfoVacume():
    r = requests.get(recentProduceCardUrl)
    soup = BeautifulSoup(r.text, "html.parser")
    elements_1 = soup.select(".h-scrollable")
    
    tempList = []
    for i in elements_1:
        tempList.append(i.getText())
    
    for a in range(10):
        for i in tempList:
            if('冒頭' not in i):
                tempList.remove(i)
           
    global idolEventListAll
    idolEventListAll = tempList.copy()




def cardEventDistribute():
    global morningEventList
    global beforeOditionSelectList
    
    
    for i in idolEventListAll:
        if('パーフェクト' in i):
            if('ノーマル' in i):
                morningEventList.append(str(i))
            
    for i in idolEventListAll:
        if('テンションアップ' in i):
            beforeOditionSelectList.append(str(i))
    
    
    
    
def selectVacume():
    r = requests.get(recentProduceCardUrl)
    soup = BeautifulSoup(r.text, "html.parser")
    elements_1 = soup.select(".h-scrollable")
    elements_2_text = soup.get_text()
    elements_2_List = elements_2_text.split("\n")
    
    for i in elements_2_List:
        elements_2_List[elements_2_List.index(i)].replace()
    
    printList(elements_2_List)
    

    
    


def exportFile():
    with open("-----CardSearchResult-----.txt", mode = 'w') as f:
        f.write("Morning event:" + "\n\t")
        for i in morningEventList:
            processStr = str(i)
            
            stripStr1 = '冒頭'
            stripStr2 = '選択肢前'
            stripStr3 = 'パーフェクト'
            stripStr4 = 'グッド'
            stripStr5 = 'ノーマル'
            
            f.write(stripStr1 + ": ")
            processStr = processStr.replace(stripStr1, '')
            f.write(processStr[0:processStr.find(stripStr2)] + "\n\t")
            processStr = processStr.replace(processStr[0:processStr.find(stripStr2)], '')
            
            f.write(stripStr2 + ": ")
            processStr = processStr.replace(stripStr2, '')
            f.write(processStr[0:processStr.find(stripStr3)] + "\n\n\t\t")
            processStr = processStr.replace(processStr[0:processStr.find(stripStr3)], '')
            
            f.write(stripStr3 + ": ")
            processStr = processStr.replace(stripStr3, '')
            f.write(processStr[0:processStr.find(stripStr4)] + \
                               "\n ----------------------------"+\
                               "-------------------------------"+\
                               "-------------------------------"+\
                               "-------------------------------"+\
                               "-------------------------------\n\t")
            processStr = processStr.replace(processStr[0:processStr.find(stripStr4)], '')
            '''
            f.write(stripStr4 + ": ")
            processStr = processStr.replace(stripStr4, '')
            f.write(processStr[0:processStr.find(stripStr5)] + "\n\t\t")
            processStr = processStr.replace(processStr[0:processStr.find(stripStr5)], '')
            
            f.write(stripStr5 + ": ")
            processStr = processStr.replace(stripStr5, '')
            f.write(processStr + "\n\n\t")
            '''
            
        print("The morning event text export complete.")
            
        f.write("\n")

        f.write("Before Odition event:" + "\n\t")
        for i in beforeOditionSelectList:
            processStr = str(i)
            
            stripStr1 = '冒頭'
            stripStr2 = '選択肢前'
            stripStr3 = 'テンションアップ'
            stripStr4 = '変化なし'
            stripStr5 = 'テンションダウン'
            
            f.write(stripStr1 + ": ")
            processStr = processStr.replace(stripStr1, '')
            f.write(processStr[0:processStr.find(stripStr2)] + "\n\t")
            processStr = processStr.replace(processStr[0:processStr.find(stripStr2)], '')
            
            f.write(stripStr2 + ": ")
            processStr = processStr.replace(stripStr2, '')
            f.write(processStr[0:processStr.find(stripStr3)] + "\n\n\t\t")
            processStr = processStr.replace(processStr[0:processStr.find(stripStr3)], '')
            
            f.write(stripStr3 + ": ")
            processStr = processStr.replace(stripStr3, '')
            f.write(processStr[0:processStr.find(stripStr4)] + \
                               "\n ----------------------------"+\
                               "-------------------------------"+\
                               "-------------------------------"+\
                               "-------------------------------"+\
                               "-------------------------------\n\t")
            processStr = processStr.replace(processStr[0:processStr.find(stripStr4)], '')
            
        print("The before odition event text export complete.")
        
    print("<<All text export complete.>>")



def main():
    fileLoadingToList()
    askingToUser()
    produceCardVacume()
    askingWhatCardToUser()
    searchCardUrl()
    cardInfoVacume()
    cardEventDistribute()
    #selectVacume()
    exportFile()
    
    
    
main()