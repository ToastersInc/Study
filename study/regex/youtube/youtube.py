from bs4 import BeautifulSoup
# import webbrowser
# import time
# html_string = """<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0?si=NCrDLA6Zgw18O_z1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"""
def main():
    html_string = input("HTML: ")
    soup = BeautifulSoup(html_string, 'lxml')
    print(soup)
    parse(soup)
    #webbrowser.open(url)
    #time.sleep(5)

def parse(s):
    links = s.find_all('iframe')
    for link in links:
        url = link.get('src')
        if url:
            new_url = url.replace("embed/", "")
            print(f"Found link URL: {new_url}")
            #return url

    

if __name__ == "__main__":
    main()
