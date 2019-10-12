def get_opendata(event_name, filename):
    import requests
    import urllib
    html = request_opendata_event(event_name)
    data = get_opendata_links(html, filename)
    return data

def request_opendata_event(event_name):
    """Build open data event parsing url call"""
    import requests
    import urllib
    url_base = "https://www.digitalglobe.com/ecosystem/open-data/"
    event=event_name
    html = requests.get(url_base + event_name)
    return html

def get_opendata_links(html, filename):
    soup = BeautifulSoup(html.text, "html.parser")
    for link in soup.find_all('a'):
        href = link['href']
        filename = filename
        if href.endswith('.tif'):
            with open(f"{filename}.txt", "a") as f:
                f.write(href+"\n") # write on new line
    return f

def get_dgopendata(event, filename):
    html = request_opendata_event(event)
    data = get_opendata_links(html)
    return data