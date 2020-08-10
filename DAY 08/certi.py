import cv2

img = cv2.imread("CertificateTemplate.jpg")

def generate_certificate(img, name):
    copy_img = img.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    coordinate = (700, 750)
    font_size = 3.5
    font_color = (55,55,55)
    font_thickness = 10
    cv2.putText(copy_img, name, coordinate, font, font_size, font_color, font_thickness)
    return copy_img

def save_img(generate_img, name):
    path = "certi-{}.jpg".format(name)
    cv2.imwrite(path, generate_img)


name = input("Enter your name : ")
generate_img = generate_certificate(img, name)
save_img(generate_img, name)