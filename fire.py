from bs4 import BeautifulSoup
from time import sleep
from random import randint
width = 40
height = 40
f = open("render.html", "r")
fireColorsPallete = [[7, 7, 7],[31, 7, 7],[47, 15, 7],[71, 15, 7],[87, 23, 7],[103, 31, 7],[119, 31, 7],[143, 39, 7],[159, 47, 7],[175, 63, 7],[191, 71, 7],[199, 71, 7],[223, 79, 7],[223, 87, 7],[223, 87, 7],[215, 95, 7],[215, 95, 7],[215, 103, 15],[207, 111, 15],[207, 119, 15],[207, 127, 15],[207, 135, 23],[207, 135, 23],[199, 135, 23],[199, 143, 23],[199, 151, 31],[191, 159, 31],[191, 159, 31],[191, 167, 39],[191, 167, 39],[191, 175, 47],[183, 175, 47],[183, 183, 47],[183, 183, 55],[207, 207, 111],[223, 223, 159],[239, 239, 199],[255, 255, 255],]

def start():
    FirePixels = createDataStructure()
    renderFire(FirePixels)
    createFireSource(FirePixels)

    while True:
        calculateFirePropagation(FirePixels)
        
        sleep(0.1)

def createDataStructure():
    pixArray = []
    pixArray = [0 for i in range(width*height)]  
    return pixArray


def createFireSource(FirePixels):
    lastPixel = len(FirePixels)
    for collumn in range(width):
        source_index = (lastPixel - width) + collumn
        FirePixels[source_index] = 36

def calculateFirePropagation(FirePixels):
    for collumn in range(width):
        for row in range(height):
            index = collumn + row*width
            if index >= len(FirePixels) - width:
                continue
            else:
                decay = randint(0,2)
                FirePixels[index-decay] = FirePixels[index+width] - decay
                createFireSource(FirePixels)
                if FirePixels[index-decay] < 0:
                    FirePixels[index-decay] = 0
    
    renderFire(FirePixels)

            

def renderFire(FirePixels):
    debug = False
    html = '        <table cellpadding = 0 cellspacing = 0>'
    
    for row in range(height):
        html += '<tr>'
        for collumn in range(width):
            index = collumn + row*width
            if debug:
                html += '<td>'
                html += str(FirePixels[index])
                html += '</td>'
            
            else:
                color = fireColorsPallete[FirePixels[index]]
                colorString = str(color[0])+',' + str(color[1])+ ',' +str(color[2])
                html += '<td style = "background-color: rgb(' + colorString + ')">'
                html += '</td>'
        html += '</tr>'

    html += '</table>'
    html += '<META HTTP-EQUIV="refresh" CONTENT="0.1">'
    html += '</body>'
    html += '<html>'
    insertHtml(html)


def insertHtml(html):
    html_file = open('render.html','r')
    lines = html_file.readlines()
    for i, line in enumerate(lines):
        if line == """        <div id = 'FireCanvas'></div>\n""":
            lines[i] = line +"        " + html
        if line.startswith('                <table',0,23):
            lines.pop(i)

    new_html_file = open('render.html','w')
    new_html = ''.join(lines)
    new_html_file.write(new_html)

start()