""" Code to create a transparent background for an image on greyscale background
In this project, this file takes the rock image and returns a transparent background version."""

from PIL import Image


def transparent(filename: str):
    img = Image.open(filename)
    img = img.convert("RGBA")
    img_data = img.getdata()
    new_img = img.copy()
    new_data = []
    for pixel in img_data:
        if pixel[0] == pixel[1] and pixel[1] == pixel[2] and pixel[0] != 0:
            new_color = (0, 0, 0, 0)
            new_data.append(new_color)
        else:
            new_data.append(pixel)
    new_img.putdata(new_data)
    return new_img


if __name__ == "__main__":
    rock_transparent = transparent("Images/rock.png")
    rock_transparent.show()
    # rock_transparent.save("Images/rock_transparent.png")

    # If rock_transparent is not 360x360, make a note using TODO
