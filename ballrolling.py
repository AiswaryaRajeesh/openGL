from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOW_SIZE=500
x=0.0
y=0.0
x1=230
y1=250
cx=x1-50
cy=y1
dx=x1-x
dy=y1-y
m=dy/dx

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def draw():
    global x,y,x1,y1,cx,cy
    glClear(GL_COLOR_BUFFER_BIT)

    glLineWidth(6.0)
    glBegin(GL_LINES)
    glColor3f(0.0,1.0,1.0)
    glVertex2f(x,y)
    glVertex2f(x1,y1)
    glEnd()
   
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(cx,cy)
    for i in range(0,361,1):
        glVertex2f(40*math.cos(math.pi*i/180)+cx,40*math.sin(math.pi*i/180)+cy)
    glEnd()
    glutSwapBuffers()

def animate(temp):
    global x,y,x1,y1,cx,cy,dx,dy,m

    if(cy>y+30 and cx>x-50):
        if(dx>dy):
            cx=cx-1
            cy=cy-m
        else:
            cx=cx-1/m
            cy=cy-1
    else:
        cx=x1-50
        cy=y1

    glutTimerFunc(int(1000/50),animate,0)
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("draw")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(draw)
    init()
    glutMainLoop()
main()
