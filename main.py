from bottle import route, run, template, static_file
import sys

file_path = sys.argv[1]

integer = 0
html = ''
with open('index.html', 'r') as f:
    html = f.read()

@route('/')
def index():
    number = 0
    with open(file_path, 'r') as f:
        number = f.read()

    try:
        integer = int(number.strip().split(',')[-1][0:2])
    except TypeError:
        integer = 0
        print(number)
    except ValueError:
        integer = 0
        print(number)

    if 0 <= integer <= 24:
        image = '/static/dog.png'
    if 25 <= integer <= 49:
        image = '/static/cock.png'
    if 50 <= integer <= 74:
        image = '/static/bull.png'
    if 75 <= integer <= 99:
        image = '/static/deer.png'
    return template(html, image=image)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')

run(host='localhost', port=8080)
