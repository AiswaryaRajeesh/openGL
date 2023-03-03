from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

WINDOW_SIZE=500
FPS=80
x1=0
y1=0
x2=150
y2=260
dx=x2-x1
dy=y2-y1
m=dy/dx
cx=x2-40
cy=y2

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def draw():
	global m,dx,dy,x2,x1,y2,y1,cx,cy
	glClear(GL_COLOR_BUFFER_BIT)
	glLineWidth(10.0)
	glBegin(GL_LINES)
	glColor3f(0.0,0.0,0.0)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2) 
	glEnd()
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(cx,cy)
	for i in range(0,361,1):
		glVertex2f(30*math.cos(math.pi*i/180.0)+cx,30*math.sin(math.pi*i/180.0)+cy)
	glEnd()
	glutSwapBuffers()

def animate(temp):
	global m,dx,dy,x2,x1,y2,y1,cx,cy
	if(cy>y1+20 and cx>x1-40): 
		if(dx>=dy):
			cx=cx-1
			cy=cy-m
		else:
			cx=cx-(1/m)
			cy=cy-1
	else:
		cx=x2-40
		cy=y2
	glutTimerFunc(int(1000/FPS),animate,0)
	glutPostRedisplay()

def main():
	glutInit(sys.argv)
	glutInitWindowPosition(0,0)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitDisplayMode(GLUT_RGBA)
	glutCreateWindow("inclined")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	init()
	glutMainLoop()
main()