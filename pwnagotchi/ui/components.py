import logging
import pwnagotchi
import pwnagotchi.ui.fancygotchi as fancygotchi
from PIL import Image, ImageDraw, ImageOps, ImageFont
from textwrap import TextWrapper
import sys
import os

class Widget(object):
    def __init__(self, xy, color=0):
        self.xy = xy
        self.color = color
        self.icolor = 0
        self.colors = []

    def draw(self, canvas, drawer):
        raise Exception("not implemented")

    def text_to_rgb(self, text, tfont, color, width, height):
        try:
            th_opt = pwnagotchi._theme['theme']['options']
            if color == 'white' : color = (254, 254, 254, 255)
            w,h = tfont.getsize(text)
            nb_lines = text.count('\n') + 1
            h = (h + 1) * nb_lines
            if nb_lines > 1:
                lines = text.split('\n')
                max_char = 0
                tot_char = 0
                for line in lines:
                    tot_char = tot_char + len(line)
                    char_line = len(line)
                    if char_line > max_char: max_char = char_line
                w = int(w / (tot_char / max_char))
            imgtext = Image.new('1', (int(w), int(h)), 0xff)
            dt = ImageDraw.Draw(imgtext)
            dt.text((0,0), text, font=tfont, fill=0x00)
            if color == 0: color = 'black'
            imgtext = ImageOps.colorize(imgtext.convert('L'), black = color, white = 'white')
            imgtext = imgtext.convert('RGB')
            return imgtext
        except Exception as e:
            logging.warning("Error:", str(e))
            return None

    def adjust_image(image_path, zoom, mask=False):
        try:
            # Open the image
            image = Image.open(image_path)
            image = image.convert('RGBA') 
            #image.save('/home/pi/original.png')
            # Get the original width and height
            original_width, original_height = image.size
            # Calculate the new dimensions based on the zoom factor
            new_width = int(original_width * zoom)
            new_height = int(original_height * zoom)
            # Resize the image while maintaining the aspect ratio
            adjusted_image = image.resize((new_width, new_height))
            if mask:
                image = adjusted_image.convert('RGBA') 
                width, height = image.size
                pixels = image.getdata()
                new_pixels = []
                for pixel in pixels:
                    r, g, b, a = pixel
                    # If pixel is not fully transparent (alpha is not 0), convert it to black
                    #if a > 50:
                    if a > 150:
                        new_pixel = (0, 0, 0, 255)
                    else:
                        new_pixel = (0, 0, 0, 0)
                    new_pixels.append(new_pixel)
                # Create a new image with the modified pixel data
                new_img = Image.new("RGBA", image.size)
                new_img.putdata(new_pixels)
                adjusted_image = new_img
            return adjusted_image
        except Exception as e:
            logging.warning("Error:", str(e))
            return None

class Bitmap(Widget):
    def __init__(self, path, xy, color=0):
        super().__init__(xy, color)
        self.image = Image.open(path)

    def draw(self, canvas, drawer):
        canvas.paste(self.image, self.xy)


class Line(Widget):
    def __init__(self, xy, color=0, width=1):
        super().__init__(xy, color)
        self.width = width

    def draw(self, canvas, drawer):
        drawer.line(self.xy, fill=self.color, width=self.width)


class Rect(Widget):
    def draw(self, canvas, drawer):
        drawer.rectangle(self.xy, outline=self.color)


class FilledRect(Widget):
    def draw(self, canvas, drawer):
        drawer.rectangle(self.xy, fill=self.color)


class Text(Widget):
#    def __init__(self, value="", position=(0, 0), font=None, color=0, wrap=False, max_length=0):
    def __init__(self, value="", position=(0, 0), font=None, color=0, wrap=False, max_length=0, icon=False, f_awesome=False, f_awesome_size=0, face=False, zoom=1):

        super().__init__(position, color)
        th_opt = pwnagotchi._theme['theme']['options']
        logging.warning(color)

        self.value = value
        self.font = font
        self.wrap = wrap
        self.max_length = max_length
        self.wrapper = TextWrapper(width=self.max_length, replace_whitespace=False) if wrap else None
        self.icon = icon
        self.image = None
        self.f_awesome = f_awesome
        self.f_awesome_size = f_awesome_size
        self.face = face
        self.zoom = zoom
        th = pwnagotchi._theme['theme']['main_elements']
        self.face_map = {}
        self.friend_map = {}
        th_faces = th['face']['faces']
        th_img_t = th['face']['image_type']
        if not th_opt['main_text_color'] == '':
            self.mask = True
        else:
            self.mask = False

    def get_font(self):
        return self.font

    def draw(self, canvas, drawer):
        if self.value is not None:
            if self.wrap:
                text = '\n'.join(self.wrapper.wrap(self.value))
            else:
                text = self.value
            drawer.text(self.xy, text, font=self.font, fill=self.color)


class LabeledValue(Widget):
    def __init__(self, label, value="", position=(0, 0), label_font=None, text_font=None, color=0, label_spacing=9, icon=False, label_line_spacing=0, f_awesome=False, f_awesome_size=0, zoom=1):
        th_opt = pwnagotchi._theme['theme']['options']
        label_spacing = th_opt['label_spacing']
        super().__init__(position, color)
        self.label = label
        self.value = value
        self.label_font = label_font
        self.text_font = text_font
        self.label_spacing = label_spacing
        self.label_line_spacing = label_line_spacing
        self.icon = icon
        self.image = None
        self.zoom = zoom
        self.f_awesome = f_awesome
        self.f_awesome_size = f_awesome_size
        if not th_opt['main_text_color'] == '':
            self.mask = True
        else:
            self.mask = False
        if icon:
            if not self.f_awesome:
                icon_path = '%simg/%s' % (pwnagotchi._fancy_theme, label)
                self.image =  adjust_image(icon_path, self.zoom, self.mask)#Image.open(icon_path)
                if th_opt['main_text_color'] != '':
                    self.image.convert('1')
            else:
                fa = ImageFont.truetype('font-awesome-solid.otf', self.f_awesome_size)
                code_point = int(self.label, 16)
                icon = code_point
                w,h = fa.getsize(icon)
                icon_img = Image.new('1', (int(w), int(h)), 0xff)
                dt = ImageDraw.Draw(icon_img)
                dt.text((0,0), icon, font=fa, fill=0x00)
                icon_img = icon_img.convert('RGBA')
                self.image = icon_img

    def draw(self, canvas, drawer):
        if self.label is None:
            drawer.text(self.xy, self.value, font=self.label_font, fill=self.color)
        else:
            pos = self.xy
            drawer.text(pos, self.label, font=self.label_font, fill=self.color)
            drawer.text((pos[0] + self.label_spacing + 5 * len(self.label), pos[1]), self.value, font=self.text_font, fill=self.color)
