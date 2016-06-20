import requests

def getCatFacts(num):
    #Thanks to CatFacts-API.apppot.com!
    r = requests.get("http://catfacts-api.appspot.com/api/facts?number="+str(num))
    p = r.text
    p2 = p.replace('{"facts": [','')
    p2 = p2.replace("]","")
    p2 = p2.replace("]","")
    p3 = p2.split('", "')
    p3[0] = p3[0].replace('"',"")
    outputString = ""
    for i in range(0,num,1):
        outputString += "- "+p3[i] + "\n"
    return outputString

def getCatPic():
    #Thanks to TheCatAPI.com!
    r = requests.get("http://thecatapi.com/api/images/get?format=src")
    return r.url

def YandereGET(tag,num,site):
    #Thanks to Yande.re!
    #site 0 = yand.re
    #site 1 = konachan
    if site == 0:
        siteURL = "https://yande.re/post.json?limit=1&page="
    elif site == 1:
        siteURL = "http://konachan.com/post.json?limit=1&page="
    if tag.replace(" ","") == "":
        r = requests.get(siteURL+str(num))
    else:
        r = requests.get(siteURL+str(num)+"&limit=1&tags="+tag)
    #print(r)
    p = r.text.replace("[{","")
    p = p.replace("}]","")
    p2 = p.split(",")
    if len(p2) == 1:
        return "Invalid Tag"
    else:
        p3 = p2[10].replace('"file_url":"',"")
        p3 = p3.replace('"',"")
        return p3

#def YandereTagSearch(SearchTerm,limit,order)
