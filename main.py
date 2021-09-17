from PIL import Image

image_monro = Image.open("m_image.png")

red , green, blue = image_monro.split()

monro = Image.merge("RGB", (red , green , blue))

width_red, height_red = red.size
width_blue, height_blue = blue.size
width_green, height_green = green.size

img_cr_red = red.crop((100 , 0 , width_red, height_red))
img_cr_red_2 = red.crop((50 , 0 , width_red - 50, height_red))
red_to_red = Image.blend(img_cr_red , img_cr_red_2,0.5)

img_cr_blue = blue.crop((0 , 0 , width_blue - 100, height_blue))
img_cr_blue_2 = blue.crop((50 , 0 , width_blue - 50, height_blue))
img_blend_2 = Image.blend(img_cr_blue , img_cr_blue_2 , 0.5)

img_cr_green = green.crop((50 , 0 , width_green - 50, height_green))


result = Image.merge("RGB", (red_to_red ,img_cr_green, img_blend_2 ))
result.thumbnail((80 , 70))
result.save("result.png")










