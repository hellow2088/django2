import random
from io import BytesIO

from PIL import ImageDraw, Image, ImageFont


def get_ramdom_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def getValidCode(request):

    img = Image.new('RGB', (230, 40), color=get_ramdom_color())

    draw = ImageDraw.Draw(img)
    valid_font = ImageFont.truetype("arial.ttf", 32)
    # valid_font = ImageFont.truetype("static/plugins/font-awesome-4.7.0/fonts/FontAwesome.otf", 32)

    validCode_string = ''
    for i in range(5):
        rnum = str(random.randint(0, 9))
        low_alpha = chr(random.randint(95, 122))
        up_alpha = chr(random.randint(65, 90))
        r_char = random.choice([rnum, low_alpha, up_alpha])
        draw.text((i * 45, 5), r_char, get_ramdom_color(), font=valid_font)
        validCode_string += r_char

    request.session['validCode_string'] = validCode_string
    # with open('static/images/validCode.png','wb') as f:
    # 	img.save(f,'png')
    # with open('static/images/validCode.png','rb') as f:
    # 	dimg = f.read()

    # 验证码添加噪声
    # width = 230
    # height = 40
    # for i in range(10):
    #     x1 = random.randint(0,width)
    #     x2 = random.randint(0,width)
    #     y1 = random.randint(0,height)
    #     y2 = random.randint(0,height)
    #     draw.line((x1,y1,x2,y2),fill=get_ramdom_color())
    #
    # for i in range(50):
    #     draw.point([random.randint(0,width),random.randint(0,height)],fill=get_ramdom_color())
    #     x = random.randint(0,width)
    #     y = random.randint(0,height)
    #     draw.arc((x,y,x+4,y+4),0,90,fill=get_ramdom_color())

    f = BytesIO()
    img.save(f, 'png')
    dimg = f.getvalue()
    print(validCode_string)
    return dimg
