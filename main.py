from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open('pespatron.jpeg') as pic_original:
    print('Розмір:', pic_original.size)
    print('Формат:', pic_original.format)
    print('Тип:', pic_original.mode)
    pic_original.show()
#робимо картинку чорнобілою
    pic_gray = pic_original.convert('L')
    pic_gray.save('bw.jpg')
    print('Розмір:',pic_gray.size)
    print('Формат:',pic_gray.format)
    print('Тип:', pic_gray.mode)
    pic_gray.show()
    # заблюрина картинка
    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('blured.jpg')
    print('Розмір:',pic_blured.size)
    print('Формат:',pic_blured.format)
    print('Тип:', pic_blured.mode)
    pic_blured.show()
# повертаємо картинку на 180 градусів
    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save('up.jpg')
    pic_up.show()
    #відзеркалюємо картинку
    pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirrow.save('mirrow.jpg')
    pic_mirrow.show()
    # робимо картинку контрастною
    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save('contr.jpg')
    pic_contrast.show()
    #додамо більш розмитий чб ефект
    img_gray_smooth = pic_original.filter(ImageFilter.SMOOTH)
    img_gray_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
    img_gray_smooth.save('img_gray_smooth.jpg')
    img_gray_smooth.show()
    #перевертаємо картинку на 90 градусів
    rotated_img = pic_original.rotate(90, expand=True)
    rotated_img.save('rotated.jpg')
    rotated_img.show()

