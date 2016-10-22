"""This is the entry point of the program."""


def create_box(height, width, character):
    if height < 1:
        if width < 1:
            return 'Box not big enough.'
    box = []
    for i in range(0,height):
        box.append(character * width)
    return '\n'.join(box) + '\n'
    
    
print(create_box(3,4,'o'))


def create_empty_box(height,width,character):
    if height < 3:
        if width < 3:
            return 'Box not big enough'
    box = []
    for i in range(0,height):
        if i == 0:
            box.append(character * width)
        elif 0<i<height:
            box.append(character + ' '* int(width-2) + character)
        if i == height-1:
            box.append(character * width)
    return '\n'.join(box) + '\n'

print(create_empty_box(3,4,'o'))


if __name__ == '__main__':
    create_box(3, 4, '*')
    
    