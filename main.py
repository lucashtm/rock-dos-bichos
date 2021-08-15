from bottle import route, run, template, static_file
import sys

PORT = 8080

file_path = sys.argv[1]

context = {
    'integer': 0,
    'html': ''
}

integer = 0
html = ''
with open('index.html', 'r') as f:
    context['html'] = f.read()


def select_image(number):
    if 0 <= number <= 24:
        return '/static/dog.png'
    if 25 <= number <= 49:
        return '/static/cock.png'
    if 50 <= number <= 74:
        return '/static/bull.png'
    if 75 <= number <= 99:
        return '/static/deer.png'

@route('/')
def index():
    with open(file_path, 'r') as f:
        number = f.read()

    try:
        context['integer'] = int(number.strip().split(',')[-1][0:2])
        print(context['integer'])
    except TypeError:
        pass
    except ValueError:
        pass

    image = select_image(context['integer'])
    return template(context['html'], image=image)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./images')

run(host='localhost', port=PORT)
