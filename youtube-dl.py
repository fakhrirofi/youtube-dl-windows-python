import os

print("youtube-dl interface")
username = input("Username: ")
password = input("Password: ")
url = input("URL: ")

def Engine(command):
    data = {
        '1' : 'os.system(f".\youtube-dl -F -u {username} -p {password} {url}")',
        '2' : 'select = input("format code: ");os.system(f".\youtube-dl -f {select} -u {username} -p {password} {url}")'}
    access = data.get(f'{command}')
    exec(access)

def NewURL():
    new = input("New URL: ")
    return new

def Start():
    print(f"Selected URL: {url}")
    print("""Command:
    1. List download
    2. Download file
    3. Edit Url""")
    command = int(input("> "))
    if command != 3:
        Engine(command)
        print("\n \a \a \a")
        Start()

while True:
    Start()
    url = NewURL()
