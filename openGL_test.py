import pygame
from pygame.locals import *
from OpenGL.GL import *

# 初始化 Pygame
pygame.init()

# 視窗大小
width, height = 800, 600

# 建立 Pygame 視窗
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# 渲染循環
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glBegin(GL_TRIANGLES)
    
    glColor3f(1, 0, 0)  # 紅色
    glVertex3f(0, 1, 0)
    
    glColor3f(0, 1, 0)  # 綠色
    glVertex3f(-1, -1, 0)
    
    glColor3f(0, 0, 1)  # 藍色
    glVertex3f(1, -1, 0)
    
    glEnd()

    pygame.display.flip()
