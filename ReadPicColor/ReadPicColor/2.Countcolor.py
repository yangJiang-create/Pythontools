from PIL import Image

file_path = r'test.png'
img = Image.open(file_path)
imgSize = img.size  #大小/尺寸
w = img.width       #图片的宽
h = img.height      #图片的高

im = Image.open(file_path)
rgb_im = im.convert('RGB')

green = 0
white = 0
red = 0
other = {}

for a in range(w):
    for b in range(h):
        r, g, b = rgb_im.getpixel((a, b)) #获取指定像素的rgb值
        if (r, g, b) == (0,128,0): #判断是否为绿色
            green +=1
        elif (r, g, b) == (191,191,191):#判断是否为白色
            white +=1
        elif (r, g, b) == (145,4,38):#判断是否为红色
            red +=1
        else:
            if (r, g, b) not in other:
                other[(r, g, b)] = 1
            else :
                other[(r, g, b)] += 1

cell = green/18
print(
f'''绿色有{green/cell}个
白色有{white/cell}个
红色有{red/cell}个

其他颜色如下
{other}
''')