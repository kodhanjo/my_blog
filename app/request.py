import urllib.request,json
# base_url = None

def get_blogs():
    get_blogs_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_blogs_url) as url:
        blogs = url.read()
        get_blogs_response = json.loads(blogs)
        
    return get_blogs_response