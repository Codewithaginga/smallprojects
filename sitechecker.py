# import urlib
# use urlib.request to get the data fro url
# write a function that takes a url
# returns the data from url

import urllib.request as urlib

def main(url):

    print('checking connectivity ')

    response = urlib.urlopen(url)
    print(f'connected to {url} succesfully')

    print(f'The response code was : {response.getcode()} ' )


print(f'connectivity check up ')

site_url = input('write the url of the site: ')
  
main(site_url)