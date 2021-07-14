import http.client as httplib

host = "http://desarrollo.datamatic.com.uy"
port = 86
url = "/mt4/index.php?r=ws/clock2/start"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
}

data = {
    "deviceId" : "1485",
    "local" : 113,
    "ext": ".jpg",

    # This fields are NEEDED
    "time" : "2021-07-15 09:09:09",
    "image": "fruta trest"
}

conn = httplib.HTTPConnection(host, port, timeout=5)
print("CONNECTION %s" % type(conn)) if conn else print("ERROR")

response = False
try:
    conn.request("POST", url, data, headers)
    response = conn.getresponse()
except OSError as ex:
    print(ex)

if not response:
    print("NO Server Response")
    exit()

print(response.status, response.reason)
data = response.read()
print(data)
conn.close()