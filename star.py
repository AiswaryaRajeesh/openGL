from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOW_SIZE=500
x=0.0
y=0.0
r=70
mode=1

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawstar():
    global x,y,r
    glClear(GL_COLOR_BUFFER_BIT)
    
    x1=r*math.cos(math.pi*90/180)+x
    y1=r*math.sin(math.pi*90/180)+y
    x2=r*math.cos(math.pi*225/180)+x
    y2=r*math.sin(math.pi*225/180)+y
    x3=r*math.cos(math.pi*315/180)+x
    y3=r*math.sin(math.pi*315/180)+y
    x4=r*math.cos(math.pi*45/180)+x
    y4=r*math.sin(math.pi*45/180)+y
    x5=r*math.cos(math.pi*135/180)+x
    y5=r*math.sin(math.pi*135/180)+y
    x6=r*math.cos(math.pi*270/180)+x
    y6=r*math.sin(math.pi*270/180)+y

    glBegin(GL_TRIANGLES)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(x4,y4)
    glVertex2f(x5,y5)
    glVertex2f(x6,y6)
    glEnd()

    glutSwapBuffers()

def animate(temp):
    global mode,r

    if(mode==1):
        if(r>150):
            mode=0
        else:
            r=r+1
    else:
        if(r<70):
            mode=1
        else:
            r=r-1
    glutTimerFunc(int(1000/60),animate,0)
    glutPostRedisplay

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("star")
    glutDisplayFunc(drawstar)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawstar)
    init()
    glutMainLoop()
main()

