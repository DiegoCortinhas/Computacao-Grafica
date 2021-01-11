from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, heigth = 800, 600


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glLoadIdentity()
    glPopMatrix()
    glutSwapBuffers()  # It is important for double buffering


# Initialization

glutInit()  # Initialize GlUT
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(width, heigth) #set window size
glutInitWindowPosition(200,200)  #window position
window = glutCreateWindow("Opengl Window in Python")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()


