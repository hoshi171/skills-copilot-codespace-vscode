import cmpt120image
import random

# 1. Black Top Half
def blackTopHalf(img):
    height = len(img)
    width = len(img[0])
    for row in range(height // 2):
        for col in range(width):
            img[row][col] = [0, 0, 0]  # Set to black
    return img

# 2. Cover Right Half with Random Central Color
def coverRightHalf(img):
    height = len(img)
    width = len(img[0])
    rand_row = random.randint(height // 3, 2 * height // 3)
    rand_col = random.randint(width // 3, 2 * width // 3)
    color = img[rand_row][rand_col]  # Get a random central pixel color
    for row in range(height):
        for col in range(width // 2, width):
            img[row][col] = color
    return img

# 3. Swap Red and Blue Channels
def swapRedWithBlue(img):
    height = len(img)
    width = len(img[0])
    for row in range(height):
        for col in range(width):
            r, g, b = img[row][col]
            img[row][col] = [b, g, r]  # Swap red and blue
    return img

# 4. Place Two Images Side by Side
def placeTwoTogether(img1, img2):
    height = len(img1)
    width = len(img1[0])
    new_img = [[None] * (2 * width) for _ in range(height)]
    for row in range(height):
        new_img[row][:width] = img1[row]  # Left half original
        new_img[row][width:] = img2[row]  # Right half modified
    return new_img

# 5. Reduce Image to Half Size
def reduceToHalf(img):
    height = len(img)
    width = len(img[0])
    new_img = [[img[row * 2][col * 2] for col in range(width // 2)] for row in range(height // 2)]
    return new_img

# 6. Invert Image Colors
def invert(img):
    height = len(img)
    width = len(img[0])
    for row in range(height):
        for col in range(width):
            r, g, b = img[row][col]
            img[row][col] = [255 - r, 255 - g, 255 - b]
    return img

# 7. Add Green to Entire Image
def addgreenWhole(img):
    for row in img:
        for col in range(len(row)):
            r, g, b = row[col]
            row[col] = [r, min(g + 100, 255), b]  # Increase green, max 255
    return img

# 8. Add Green Stripes
def addGreenStripes(img, nstripes):
    height = len(img)
    width = len(img[0])
    stripe_width = width // (nstripes * 2)
    for i in range(nstripes):
        start_col = i * 2 * stripe_width
        for row in range(height):
            for col in range(start_col, start_col + stripe_width):
                if col < width:
                    r, g, b = img[row][col]
                    img[row][col] = [r, min(g + 100, 255), b]
    return img

# 10. Convert to Grayscale
def grayscale(img):
    for row in img:
        for col in range(len(row)):
            r, g, b = row[col]
            gray = (r + g + b) // 3
            row[col] = [gray, gray, gray]
    return img

# 11. Add Random Rectangles
def addRects(img, n, h, w, color):
    height = len(img)
    width = len(img[0])
    for _ in range(n):
        x = random.randint(0, width - w)
        y = random.randint(0, height - h)
        for row in range(y, y + h):
            for col in range(x, x + w):
                img[row][col] = color
    return img

# 12. Add Gradual Green
def addGradualGreen(img, initGreenValue):
    height = len(img)
    width = len(img[0])
    for row in range(height):
        for col in range(width):
            r, g, b = img[row][col]
            new_g = min(initGreenValue + (col * 255) // width, 255)
            img[row][col] = [r, new_g, b]
    return img

# 13. Repeat Top Stripe
def stripes(img, nstripes):
    height = len(img)
    width = len(img[0])
    stripe_height = height // nstripes
    for i in range(nstripes):
        for row in range(stripe_height):
            img[i * stripe_height + row] = img[row][:]
    return img

# 14. Flip Top Half Vertically
def flipVertical(img):
    height = len(img)
    width = len(img[0])
    for row in range(height // 2):
        img[row] = img[height - 1 - row][:]
    return img

# 15. Create Image Row Pattern
def createImgRow(img, rownum, cstart, cstop, w, h):
    row_segment = img[rownum][cstart:cstop]  # list of pixels
    new_img = []
    for _ in range(h):  # height of new image
        new_row = []
        for pixel in row_segment:
            new_row.extend([pixel] * w)  # repeat each pixel w times
        new_img.append(new_row)
    return new_img

# Testing each function with "ORIGINALPICTURE.jpg"
if __name__ == "__main__":
    img = cmpt120image.getImage("ORIGINALPICTURE.jpg")

    # Apply functions and save images
 #   cmpt120image.saveImage(blackTopHalf(img), "black_top_half.jpg")
    #cmpt120image.saveImage(coverRightHalf(img), "cover_right_half.jpg")
    #cmpt120image.saveImage(swapRedWithBlue(img), "swap_red_blue.jpg")
    #cmpt120image.saveImage(reduceToHalf(img), "reduced_half.jpg")
    #cmpt120image.saveImage(invert(img), "inverted.jpg")
    #cmpt120image.saveImage(addgreenWhole(img), "add_green_whole.jpg")
    #cmpt120image.saveImage(addGreenStripes(img, 10), "green_stripes.jpg")
    #cmpt120image.saveImage(grayscale(img), "grayscale.jpg")
    #cmpt120image.saveImage(addRects(img, 5, 50, 50, [255, 0, 0]), "add_rects.jpg")
    #cmpt120image.saveImage(addGradualGreen(img, 50), "gradual_green.jpg")
    #cmpt120image.saveImage(stripes(img, 3), "stripes.jpg")
    #cmpt120image.saveImage(flipVertical(img), "flip_vertical.jpg")
    cmpt120image.saveImage(createImgRow(img, 700, 500, 520, 100, 50), "row_pattern.jpg")

print("Image manipulations completed! Check your saved images.")

