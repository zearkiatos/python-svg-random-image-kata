import random


def create_figure(position: tuple, size: tuple) -> dict:
    new_figure = {"position": position, "size": size}

    cornerX = random.randrange(0, 1)
    cornerY = random.randrange(0, 1)
    thickness = random.randrange(0, 6)
    red_internal_color = random.randrange(0, 255)
    green_internal_color = random.randrange(0, 255)
    blue_internal_color = random.randrange(0, 255)
    red_line_color = random.randrange(0, 255)
    green_line_color = random.randrange(0, 255)
    blue_line_color = random.randrange(0, 255)
    x = random.randrange(0, 380)
    y = random.randrange(0, 380)
    z = random.randrange(0, 380)

    new_figure["corner"] = (cornerX, cornerY)
    new_figure["thickness"] = thickness
    new_figure["internal_color"] = (
        red_internal_color, green_internal_color, blue_internal_color)
    new_figure["line_color"] = (
        red_line_color, green_line_color, blue_line_color)
    new_figure["rotation"] = (x, y, z)

    return new_figure


def create_image(figures: dict) -> None:
    file = open('image.svg', 'w')
    file.write("<svg height='500px' version='1.1' width='500px' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>")
    for figure in figures:
        redBg, greenBg, blueBg = figure['internal_color']
        file.write("<rect fill='rgb("+str(redBg)+","+str(greenBg)+","+str(blueBg)+")'")



def generate_image() -> None:
    figures = []
    count = 0
    while (count < 3):
        positionX = random.randrange(0, 500)
        positionY = random.randrange(0, 500)
        width = random.randrange(0, 500)
        height = random.randrange(0, 500)

        position = (positionX, positionY)
        size = (width, height)

        figure = create_figure(position, size)

        figures.append(figure)
        count += 1

    create_image(figures)

generate_image()
