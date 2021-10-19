import requests

def check_address(companyname,address1,address2,city,state,urbanCode,zipcode):
    payload = {
    'companyName' : companyname,
    'address1': address1,
    'address2':address2,
    'city':city,
    'state': state,
    'urbanCode':urbanCode,
    'zip':zipcode,

    }
    sess = requests.Session()
    sess.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    response = sess.post('https://tools.usps.com/tools/app/ziplookup/zipByAddress' , data=payload)

    if response.status_code == requests.codes.ok:
        return True
    else:
        return False