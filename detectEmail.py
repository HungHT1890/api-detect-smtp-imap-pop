from requests import session
def detect_smtp_imap_pop3(email):
    api = f'https://prod-autodetect.outlookmobile.com/detect?services=none&protocols=imap,smtp,pop3'
    header = {
        "Accept":"*/*",
        "User-Agent":"microsoft.windowscommunicationsapps",
        "X-Email":email,
        "Accept-Language":"en-US",
        "Host":"prod-autodetect.outlookmobile.com",
        "Connection":"Keep-Alive",
        "Accept-Encoding":"gzip, deflate"
        }
    try:
        ss = session()
        respond_detect = ss.get(url=api , headers= header).json()['protocols']
        for x in range(len(respond_detect)):
            protocol = respond_detect[x]['protocol']
            host_name = respond_detect[x]['hostname']
            port = respond_detect[x]['port']
            # return (protocol,host_name,port)

    except Exception as f:
        print(f)
        pass


a , b , c = (detect_smtp_imap_pop3(email='hungsaki2003@gmail.com'))
print(a)
