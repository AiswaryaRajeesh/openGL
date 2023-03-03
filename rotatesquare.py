from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOW_SIZE=500
x=0.0
y=0.0
r=100
angle=45
def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawsquare():
    global x
    global y
    global r,angle
    glClear(GL_COLOR_BUFFER_BIT)
    x1=r*math.cos(math.pi*angle/180)+x
    y1=r*math.sin(math.pi*angle/180)+y
    x2=r*math.cos(math.pi*(angle+90)/180)+x
    y2=r*math.sin(math.pi*(angle+90)/180)+y
    x3=r*math.cos(math.pi*(angle+180)/180)+x
    y3=r*math.sin(math.pi*(angle+180)/180)+y
    x4=r*math.cos(math.pi*(angle+270)/180)+x
    y4=r*math.sin(math.pi*(angle+270)/180)+y

    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,1.0)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glVertex2f(x4,y4)
    glEnd()
   
    glutSwapBuffers()
def animate(temp):
    global angle
    angle= angle+1
    glutTimerFunc(int(1000/60),animate,0)
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("square")
    glutDisplayFunc(drawsquare)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawsquare)
    init()
    glutMainLoop()
main()