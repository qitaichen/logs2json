import urlparse

def toParseUrl(res, urlKey): 
    url = res[urlKey]
    rs = urlparse.urlparse(url)
    queryDict = urlparse.parse_qs(rs.query)
    for key in queryDict: 
        res[key] = queryDict[key][0]

    return res
