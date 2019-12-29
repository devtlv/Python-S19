# HTTP Request

### 1 - Start line
Contains three elements:<br>
-  The HTTP method<br>
-  The request target<br>
> It can be an absolute path, a URL, a domain name..
-  The HTTP version<br>
__Example:__<br>
POST / HTTP/1.1
GET /background.png HTTP/1.0
### 2 - Headers
Headers are additional informations on the request, it's represented as a case-insensitive string followed by a colon `:`.
-  General headers <br>
like Via, apply to the message as a whole.<br><br>
-  Request headers<br>
like User-Agent, Accept-Type, modify the request by specifying it further (like Accept-Language), by giving context (like Referer), or by conditionally restricting it (like If-None).<br><br>
-  Entity headers<br>
like Content-Length which apply to the body of the request. Obviously, there is no such header transmitted if there is no body in the request.<br><br>
__Example:__
Host: net.tutsplus.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 300
Connection: keep-alive
Cookie: PHPSESSID=r2t5uvjq435r4q7ib3vtdjq120
Pragma: no-cache
Cache-Control: no-cache
<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers">More on headers</a>

## 3 - Body
Not all request have one, it's the content of the request.<br><Br>
HTTP messages with a body need two headers: <a href="/en-US/docs/Web/HTTP/Headers/Content-Type" title="The Content-Type entity header is used to indicate the media type of the resource."><code>Content-Type</code></a> and <a href="/en-US/docs/Web/HTTP/Headers/Content-Length" title="The Content-Length entity header indicates&nbsp;the size of the entity-body, in bytes, sent to the recipient."><code>Content-Length</code></a> <br><Br>
Body can be html, text, json etc..<Br><Br>
__Example of a full HTTP request:__
GET /hello.htm HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-AliveHTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Length: 12
Content-Type: text/html

Hello world!
## GET and POST
GET and POST are the two methods that are used to send data to the server.<br>
<br>
GET data is passed in the url request, example:<br>
`/action_page.php?firstname=Mickey&lastname=Mouse`<br>
<Br>
While POST sends data in the body of the HTTP request.<br>
Thus POST method doesn't display the data, use it in any cases you need to send sensitive information.

***
# HTTP Response

The start line of an HTTP response, called the status line, contains the following information:<br>

-  The protocol version, usually HTTP/1.1.
-  A status code, indicating success or failure of the request. Common status codes are 200, 404, or 302
-  A status text. A brief, purely informational, textual description of the status code to help a human understand the HTTP message.<br><br>
__Example:__

HTTP/1.1 404 Not Found.
## Status codes

### 200 OK
The request has succeeded. The meaning of a success varies depending on the HTTP method:

### 400 Bad Request
This response means that server could not understand the request due to invalid syntax.
 
### 401 Unauthorized
Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.

### 403 Forbidden
The client does not have access rights to the content, i.e. they are unauthorized, so server is rejecting to give proper response. Unlike 401, the client's identity is known to the server.

### 404 Not Found
The server can not find requested resource. In the browser, this means the URL is not recognized. 

### 500 Internal Server Error
The server has encountered a situation it doesn't know how to handle.
<br>
<br>
<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status">More on status codes</a>

__Example of an HTTP response:__
HTTP/1.1 400 Bad Request
Date: Sun, 18 Oct 2012 10:36:20 GMT
Server: Apache/2.2.14 (Win32)
Content-Length: 230
Content-Type: text/html; charset=iso-8859-1
Connection: Closed

  
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
<head>
   <title>400 Bad Request</title>
</head>
<body>
   <h1>Bad Request</h1>
   <p>Your browser sent a request that this server could not understand.</p>
   <p>The request line contained invalid characters following the protocol string.</p>
</body>
</html>