from PIL import Image
from PIL import ImageDraw
import math

width = 800
height = 800

spacing = 10# the degrees between each intial point

numOfFrames = int(360/spacing)

radius = .9

iterations = 10;

strokeWidth = 1;

pList = []

def getPoint(degree):
    return (math.sin(degToRad(degree))*radius*(width/2)+(width/2), math.cos(degToRad(degree))*radius*(height/2)+(height/2))

def degToRad(degree):
    return math.pi*degree/180
    

img = Image.new('RGB', (width, height), "white")
draw = ImageDraw.Draw(img)

for x in range(0, numOfFrames):
    draw.point(getPoint(x*spacing), "black") 

img.save("test.png")
