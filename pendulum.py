from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500
x=0.0
y=0.0
angle=270
FPS=30
mode=1

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawpendulum():
    global x
    global y
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    
    x1=250*math.cos(math.pi*angle/180)+x
    y1=250*math.sin(math.pi*angle/180)+y

    glLineWidth(6.0)
    glBegin(GL_LINES)
    glColor3f(0.0,1.0,1.0)
    glVertex2f(x,y)
    glVertex2f(x1,y1)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(x1,y1)
    for i in range(0,361,1):
        glVertex2f(40*math.cos(math.pi*i/180)+x1,40*math.sin(math.pi*i/180)+y1)
    glEnd()
    glutSwapBuffers()

def animate(temp):
    global mode,angle
    if (mode==1):
        if (angle>330):
            mode=0
        else:
            angle=angle+5
    else:
        if(angle<210):
            mode=1
        else:
            angle=angle-5
    glutTimerFunc(int(1000/FPS),animate,0)
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("pendulum")
    glutDisplayFunc(drawpendulum)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawpendulum)
    init()
    glutMainLoop()
main()


