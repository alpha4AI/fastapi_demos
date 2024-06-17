"""
Author: alpha<alpha@57blocks.com>
Time: 2024-06-17,
Description: This script is used to local fastapi demo
"""

import requests
import base64
import cv2
import numpy as np
import json

# 3.149.239.133 is the Public IPv4 address of the server
# 8000 is the port number of the server
# '/predict/' is the path of the server

url = 'http://3.149.239.133:8000/predict/'
# The local function(post,put,get,delete) must be  same with the server
files = {'file': open('01.JPG', 'rb')}  # 替换为你的图像文件路径

response = requests.delete(url, files=files)
# 解析JSON响应来获取base64编码的图像数据
response_json = response.json()
base64_image = response_json['base64_image']
# 解码base64图像数据
image_data = base64.b64decode(base64_image)
# 将字节流转换成 numpy 数组
nparr = np.frombuffer(image_data, dtype=np.uint8)
# 从 numpy 数组解码图像
image = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
cv2.imwrite("02.jpg", image)
# 检查图像矩阵的形状
print(image.shape)
