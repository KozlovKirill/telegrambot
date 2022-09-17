from PIL import Image, ImageDraw, ImageFont
from config import FONT
import os.path, os


def photoredactor(name, sign):
    # Функция открывает фотогафию, сохраненную в папку userphotos и добавляет на нее подпись
    # Если при подсчете размеров сгенерированной подписи оказывается, что она не полностью помещается на фотографию,
    # то размер шрифта корректируется
    # После обработки фотографии функция сохраняет ее в папку processedphotos
    userimage = Image.open(f"userphotos//{name}.jpg")
    add_text = ImageDraw.Draw(userimage)

    fnt = ImageFont.truetype(f"fonts//{FONT}", size=userimage.width // 7)
    text_lenght = fnt.getlength(sign)
    text_height = fnt.getbbox(sign)[-1]

    if text_lenght > (userimage.width * 0.9):
        c = text_lenght / (userimage.width * 0.9)
        fnt = ImageFont.truetype(f"fonts//{FONT}", size=int((userimage.width // 7) / c))
        text_lenght = fnt.getlength(sign)
        text_height = fnt.getbbox(sign)[-1]

    add_text.text(((userimage.width - text_lenght) // 2, userimage.height * 0.95 - text_height + 2), sign,
                  fill=("#000000"), font=fnt)
    add_text.text(((userimage.width - text_lenght) // 2, userimage.height * 0.95 - text_height), sign,
                  fill=("#FFFFFF"), font=fnt)

    if not os.path.exists("processedphotos"):
        os.mkdir("processedphotos")
    userimage.save(f'processedphotos//{name}processed.jpg')
