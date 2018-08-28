try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

def run(args):
    urls = [
        "http://www.example.com/foo.php?id=4",
        "http://admin.example.com/bar.php?page=home",
        "http://www.example.com/baz.jsp?size=124"
    ]

    results = []
    for url in urls: results.append(urlparse(url.encode("utf-8")))

    return results

