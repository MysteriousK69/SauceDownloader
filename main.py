import requests
from bs4 import BeautifulSoup, SoupStrainer


# f.write(requests.get("https://i3.nhentai.net/galleries/768915/1.jpg").content)


def findLinks(sauce:str):
    response = requests.get(f'http://nhentai.net/g/{sauce}').text
    links = []
    for link in BeautifulSoup(response, "html.parser", parse_only=SoupStrainer("a")):
        if link.has_attr("href") and sauce in link["href"]:
            links.append(link["href"])
    links.pop(0)
    return links

def downloadImg(links:list, path:str):
    for link in links:
        response = requests.get("http://nhentai.net" + link).text
        for link2 in BeautifulSoup(response, "html.parser", parse_only=SoupStrainer("img")):
            if link2.has_attr("src") and "galleries" in link2["src"]:
                img = requests.get(link2["src"]).content
                with open(f"{path}/{link.split('/')[-2]}.png", "wb") as f:
                    f.write(img)

def main():
    print("Enter the sauce you want to download:")
    sauce = input()
    links = findLinks(sauce)
    print("Enter the path you want to save the images in:")
    path = input()
    downloadImg(links, path)
    print(f"Sauce downloaded in {path}!")

main()
