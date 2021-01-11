from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

width,heigth = 800,600

def draw ():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.0,0.0,1.0,0.0)
    glutWireTeapot(0.6)

    glFlush()

#Initialize GLUT Window

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(width,heigth)
glutInitWindowPosition(200,200)
glutCreateWindow("Opengl Wire Teapot")
glutDisplayFunc(draw)
glutMainLoop()

