import os
import time

cwd = os.getcwd()


def open_list():
    credentials = {}
    try:
        with open(cwd + '/list.txt', 'r') as f:
            print('opened the file correctly')
            for lines in f:
                email_pass_list = lines.split(':')
                if len(email_pass_list) == 2:
                    credentials[email_pass_list[0]] = email_pass_list[1].strip('\n')
                else:
                    print('list.txt is not formatted properly')
                    time.sleep(5000)
                    exit()
        return credentials
    except FileNotFoundError as fileNotFound:
        print(f'File not found \n Please make sure there is a file called list.txt in this folder')
        print(f'\n  {fileNotFound}')


def output_credentials(credentials):
    # mode a+ will create the file if it doesn't exist, a would throw an exception if the file wouldn't exist
    with open(cwd + '/output.txt', 'a+') as f:
        f.writelines(credentials[0] + ':' + credentials[1])
        print('result stored in output.txt')


# proxies.txt ----> ipAddress:port
def proxy_setup():
    proxies = {}
    try:
        with open(cwd + '/proxies.txt', 'r') as f:
            for lines in f:
                proxy_list = lines.split(':')
                if len(proxy_list) == 2:
                    proxies[proxy_list[0]] = proxy_list[1].replace('\n', "").rstrip()
                    return proxies
                else:
                    print('proxies.txt not formatted properly')
    except FileNotFoundError:
        print('Proxies aren\'t set up correctly')
        time.sleep(5000)
        exit()


if __name__ == '__main__':
    exit()
