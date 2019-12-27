from netmiko import ConnectHandler

username = 'ubuntu'
#password = 'password'
host='ec2-3-14-66-188.us-east-2.compute.amazonaws.com'

def Connect_to_server(username,host):
    Connected = False
    if Connected == False:
        try:
            server = ConnectHandler(device_type='linux',username=username,host=host,key_file='bla.pem',timeout=10)
            return server
        except:
            print('server is down')
            return False




def show_files(server):
    show_dir = server.send_command('ls -l')
    return show_dir


if __name__ == '__main__':
    print('Connecting to server..')
    server = Connect_to_server(username,host)
    if server:
        print('finding files..')
        file = show_files(server)
        print(file)
    if not server:
        print('server is down , files not found.')




