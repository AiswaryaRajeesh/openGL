from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500
x=0.0
y=0.0
gy=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawbucket():
    global x
    global y
    global gy
    glClear(GL_COLOR_BUFFER_BIT)

    x1=x
    y1=y+100

    glLineWidth(6.0)
    glBegin(GL_LINES)
    glColor3f(0.0,1.0,1.0)
    glVertex2f(x,y)
    glVertex2f(x1,y1)
    glEnd()

    x2=x+65
    y2=y
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glColor3f(0.0,1.0,1.0)
    glVertex2f(x,y)
    glVertex2f(x2,y2)
    glEnd()

    x3=x+65
    y3=y+100

    glLineWidth(6.0)
    glBegin(GL_LINES)
    glColor3f(0.0,1.0,1.0)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,0.0)
    glVertex2f(x+1,y+1)
    glVertex2f(x+1,gy)
    glVertex2f(x+64,gy)
    glVertex2f(x+64,y+1)
    glEnd()
    glutSwapBuffers()

def animate(temp):
    global gy
    if(gy<100):
        gy=gy+1
    else:
        gy=0
    glutTimerFunc(int(1000/20),animate,0)
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("bucket")
    glutDisplayFunc(drawbucket)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawbucket)
    init()
    glutMainLoop()
main()