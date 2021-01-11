import glfw
from OpenGL.GL import *
import numpy as np
from math import sin,cos

#incializndo biblioteca glfw
if not glfw.init():
    raise Exception("glfw não pode ser inicializado")

#criando a janela
window = glfw.create_window(1280,720,"Janela do OpenGl",None,None)

#verifica se janela foi criada
if not window:
    glfw.terminate()
    raise Exception("Janela não pode ser criada")

#seta a posição da janela
glfw.set_window_pos(window,400,200)

#make the context current
glfw.make_context_current(window)

glClearColor(0,0.1,0.1,1)

#Loop para a main
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    glfw.swap_buffers(window)




#terminar glfw - desalocar recursos
glfw.terminate()



