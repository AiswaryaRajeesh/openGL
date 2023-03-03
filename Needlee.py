from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500
x=0.0
y=0.0
angle=90.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawneedle():
    global x
    global y
    global angle
    glClear(GL_COLOR_BUFFER_BIT)

    x1=300*math.cos(math.pi*angle/180)+x
    y1=300*math.sin(math.pi*angle/180)+y

    glLineWidth(5.0)
    glBegin(GL_LINES)
    glColor3f(0.0,0.0,0.0)
    glVertex2f(x,y)
    glVertex2f(x1,y1)
    glEnd()

    x2=80*math.cos(math.pi*(angle)/180)+x1
    y2=80*math.sin(math.pi*(angle)/180)+y1
    x3=80*math.cos(math.pi*(angle+90)/180)+x1
    y3=80*math.sin(math.pi*(angle+90)/180)+y1
    x4=80*math.cos(math.pi*(angle+270)/180)+x1
    y4=80*math.sin(math.pi*(angle+270)/180)+y1

    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glVertex2f(x4,y4)
    glEnd()
    glutSwapBuffers()

def animate(temp):
    global x,y,angle

    angle=angle+1
    glutTimerFunc(int(1000/60),animate,0)
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("needle")
    glutDisplayFunc(drawneedle)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawneedle)
    init()
    glutMainLoop()
main()
