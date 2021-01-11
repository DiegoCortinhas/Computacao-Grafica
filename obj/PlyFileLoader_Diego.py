from plyfile import PlyData
import numpy as np
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


def read_ply_vertices(filename):
    # ler coordenadas dos pontos XYZ do arquivo .ply usando numpy
    plydata = PlyData.read(filename)
    x = np.asarray(plydata.elements[0].data['x'])
    y = np.asarray(plydata.elements[0].data['y'])
    z = np.asarray(plydata.elements[0].data['z'])
    #confidence = np.asarray(plydata.elements[0].data['confidence'])
    #intensity = np.asarray(plydata.elements[0].data['intensity'])
    return np.stack([x, y, z], axis=1)

def read_ply_faces(filename):
    plydata = PlyData.read(filename)
    faces = plydata['face'].data['vertex_indices']
    list_faces = []
    for face in faces:
        list_faces.append(face)
    return list_faces

class PLY:
    def __init__(self, filename, frontFace=GL_CCW, cor=[0, 0, 1]):
        with open(filename, 'r') as file:
            self.end_of_header = 0
            self.n_vertex = 0
            self.n_faces = 0
            self.vertices = []
            self.faces = []
            self.cor = cor

            self.vertices = read_ply_vertices(filename)
            self.faces = read_ply_faces(filename)

            print(self.faces)

            self.gl_list = glGenLists(1)
            glNewList(self.gl_list, GL_COMPILE)
            glFrontFace(GL_CW)
            self.render()
            glEndList()

    def render(self):
        for face in self.faces:
            glBegin(GL_POLYGON)
            for vertex in face:
                glVertex3fv(self.vertices[vertex][0:3])
            glEnd()

    def draw(self):
        glPushMatrix()
        glCallList(self.gl_list)
        glPopMatrix()