from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOW_SIZE=500
x=0.0
y=0.0
FPS=60
angle=40

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawrectangle(x,y):
    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex2f(x-100,y-50)
    glVertex2f(x-100,y+50)
    glVertex2f(x+100,y+50)
    glVertex2f(x+100,y-50)
    glEnd()

def drawcircle(x,y,s):
    global angle
    if s==0:
        y=y-50
        x=x-50
    else:
        y=y-50
        x=x+50
    glColor3f(0.0,1.0,1.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,361,1):
        glVertex(25*math.cos(math.pi*i/180)+x,25*math.sin(math.pi*i/180)+y)
    glEnd()

    x1=25*math.cos(math.pi*angle/180)+x
    y1=25*math.sin(math.pi*angle/180)+y
    glColor3f(0.0,0.0,0.0)
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(x1,y1)
    glEnd()

def drawcar():
    global x
    global y
    glColor3f(1.0,0.0,0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    drawrectangle(x,y)
    drawcircle(x,y,0)
    drawcircle(x,y,1)
    glutSwapBuffers()

def animate(temp):
    global x
    global y
    global angle
    global WINDOW_SIZE
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if (x-100>-WINDOW_SIZE):
        x=x+1
        angle=angle-10
    else:
        x=400

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("car")
    glutDisplayFunc(drawcar)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawcar)
    init()
    glutMainLoop()
main()

    



