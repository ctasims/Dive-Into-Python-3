# Chapter 14: HTTP Web Services

## Summary

14.1 "Exchanging data with remote servers using nothing but the operations of HTTP".
14.2 `httplib2` handles the intricacies of caching, redirects, compression.
14.3 Don't use `urllib.request.urlopen()` in production because it's inefficient.
14.4 `urllib` doesn't utilize compression or caching well.
14.5 `httplib2` and caching, compression, redirects.
14.6 HTTP.POST
14.7 HTTP.DELETE

It appears `httplib2` isn't well-supported these days, and doesn't have good proxy support.
`requests` module is recommended over `httplib2`.
Keep in mind: the former relies on `urllib`.

## 14.1 Diving in
HTTP web services: exchanging data with remote servers using nothing but the operations of HTTP.  


## 14.2 Features of HTTP
Five important features: caching, compression, redirects

### Caching
Network access is expensive in terms of time and latency.  
Caching minimizes network access. HTTP is built for caching.  
Can use caching proxy as an "extra" cache between you and remote server.  
Python's HTTP libraries do not support caching.

### HTTP headers
HTTP uses headers to transmit metadata:
* `Cache-Control` (client) provides max-age of data and whether it can be retrieved from public proxy. `no-cache` means don't return cached content.
* `Expires` (client) gives expiration date for the data on client. Can be overidden if data not modified on server yet.
* `Last-Modified` (server) gives date this data was last changed on server.
* `If-Modified-Since` (client) can be sent with `Last-Modified` date to only update data if it has changed. If it has, get code 200. If it hasn't, get code 304 `Not Modified`.
* `ETag` (server) same purpose as `Last-Modified` header, but it's a hash. Sent as value for `If-Modified-Since`.
* `Accept-encoding` (client) lists which compression algorithms client supports.
* `Content-encoding` (server) algorithm used to compress data.
* `Location` (server) address of resource on server.

### Compression
HTTP supports gzip and deflate compression algorithms.

### Redirects
Status code 302 is temporary redirect, 301 is permanent redirect.


## 14.3 How not to fetch data over HTTP

    >>> import urllib.request as req
    >>> url = 'http://diveintopython3.org/examples/feed.xml'
    >>> data = req.urlopen(url).read()
    >>> type(data)
    <class 'bytes'>
    >>> print(data)
    b'\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head><title></title>\r\n<script src="http://ak2.imgaft.com/script/
    jquery-1.3.1.min.js" type="text/javascript"></script>\r\n<script type="text/javascript" language="javascript">\r\n$(docu
    ment).ready(function () {\r\n\tjQuery.ajax({ url: \'http://mcc.godaddy.com/parked/park.aspx/?q=pFHmpKS2nKW2LJqvL2kaqJWuZ
    l5vMKDyZwMzqaRyZ3RkAmH4AwR5WGV2L3MkWGAkZmHjAQtmAQx0Awt5BQZ5AwDmZvHlAzIaWGAkZwNkZmRjZwHjBGNlZwRyZwMwrFHmpGR=-1\', dataTyp
    e: \'jsonp\', type: \'GET\', jsonpCallback: \'parkcallback\',\r\n\t    success: function (data) { if (data["returnval"]
    != null) { window.location.href = \'http://diveintopython3.org?nr=\' + data["returnval"]; } else { window.location.href
    = \'http://diveintopython3.org?hg=0\' } }\r\n\t});\r\n    var t = setTimeout(function () { window.location.href = \'http
    ://diveintopython3.org?nr=0\'; }, 3000);\r\n});\r\n</script></head><body></body></html>'

This method works for testing and dev but is inefficient.


## 14.4 What's on the wire?

    >>> from http.client import HTTPConnection
    >>> HTTPConnection.debuglevel = 1
    >>> from urllib.request import urlopen
    >>> response = urlopen('http://diveintopython3.org/examples/feed.xml')
    send: b'GET http://diveintopython3.org/examples/feed.xml HTTP/1.1\r\nAccept-Encoding: identity\r\nUser-Agent: Python-url
    lib/3.3\r\nHost: diveintopython3.org\r\nConnection: close\r\n\r\n'
    reply: 'HTTP/1.0 302 Moved Temporarily\r\n'
    header: Pragma header: Cache-Control header: Location header: Age header: Date header: X-Cache header: X-Cache-Lookup he
    ader: Via header: Connection send: b'GET http://diveintopython3.org/examples/feed.xml HTTP/1.1\r\nAccept-Encoding: ident
    ity\r\nUser-Agent: Python-urllib/3.3\r\nHost: diveintopython3.org\r\nConnection: close\r\n\r\n'
    reply: 'HTTP/1.0 200 OK\r\n'
    header: Cache-Control header: Pragma header: Content-Type header: Expires header: Server header: X-AspNet-Version header
    : X-Powered-By header: Date header: Content-Length header: Age header: X-Cache header: X-Cache-Lookup header: Via header
    : Connection >>>

Access the actual data using `response.read()`.
`urllib` is just too inefficient for production use.


## 14.5 Introducing `httplib2`

The primary way to utilize the `httplib2` is through the `Http` object:

    h = httplib2.Http('.cache')

Pass a directory for caching.
`h.request` returns a response and content.
Note that the content is a `bytes` object.
Content-sniffing and determining what encoding to use can be difficult!

`httplib2` utilizes the local cache passed in to make requests more efficient.
To check if a response came from the cache, check `response.fromcache`.

When the response returns cached content, look in `response.dict[...]` to see what the server actually returned.

`httplib2` issues another request when given a temporary redirect. Nothing magic.
`response.previous` to get info on the original request.

If caching is enabled, the redirected request won't hit the server, but the first one will.

With permanent redirectrs `httplib2` will rewrite the url so there won't be an intermediate request.


## 14.6 Beyond `HTTP GET`
Use `HTTP POST` to send data (payload) to the server.

    >>> from urllib.parse import urlencode
    >>> data = {'status': 'test update from Python 3'}
    >>> urlencode(data)
    'status=test+update+from+Python+3'

To use HTTP authentication, do `h.add_credentials()` where `h` is our `Http` object.
`httplib2` will never send authentication headers unless asked by the server.


## 14.7 Beyond `HTTP POST`
`PUT`, `DELETE`, `PATCH`.
