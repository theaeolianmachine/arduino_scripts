import colorsys


def scale_byte_to_float(val):
    return val / 255.0


def rgb_to_hex(r, g, b):
    return hex((r << 16) + (g << 8) + b)


def rgb_to_hsv_hex(hex):
    blue = scale_byte_to_float(hex & 0xFF)
    hex = hex >> 8

    green = scale_byte_to_float(hex & 0xFF)
    hex = hex >> 8

    red = scale_byte_to_float(hex & 0xFF)
    hex = hex >> 8
    return rgb_to_hsv(red, green, blue)


def hsv_to_rgb(hue, sat, val):
    scaled = (
        scale_byte_to_float(hue), scale_byte_to_float(sat),
        scale_byte_to_float(val))
    r, g, b = (
        int(round((i * 255))) for i in colorsys.hsv_to_rgb(*scaled))

    return r, g, b


def rgb_to_hsv(r, g, b):
    hue, sat, val = (
        int(round((i * 255))) for i in colorsys.rgb_to_hsv(r, g, b))

    return hue, sat, val
