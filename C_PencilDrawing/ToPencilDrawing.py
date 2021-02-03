from PIL import Image    #图像处理模块
import numpy as np


# 将图像以灰度图的方式打开并将数据转为float存入np中
filePath = 'team.jpg'
a = np.asarray(Image.open(filePath).convert('L')).astype('float')

depth = 10.                      # (0-100)
grad = np.gradient(a)             #取图像灰度的梯度值
grad_x, grad_y =grad               #分别取横纵图像梯度值
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A
#建立一个位于图像斜上方的虚拟光源
vec_el = np.pi/2.2                   # 光源的俯视角度，弧度值
vec_az = np.pi/4.                    # 光源的方位角度，弧度值
dx = np.cos(vec_el)*np.cos(vec_az)   #光源对x 轴的影响
dy = np.cos(vec_el)*np.sin(vec_az)   #光源对y 轴的影响
dz = np.sin(vec_el)                  #光源对z 轴的影响
#计算各点新的像素值
b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)     #光源归一化
b = b.clip(0,255)    #clip函数将区间外的数字剪除到区间边缘

im = Image.fromarray(b.astype('uint8'))  #重构图像

# "这里是输出图片的路径"
outputPath = "./output_pencil_drawing.jpg"
im.save(outputPath)