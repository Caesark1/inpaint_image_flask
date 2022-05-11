from PIL import Image

from app import app

from flask import render_template, request

from app import services
from app import run_inpaint

@app.route("/", methods=('GET', 'POST'))
def main():
    if request.method == 'POST':
        form = request.form
        print(form)
        filename = run_inpaint.inpaint(form.get('text'), form.get('images'))
        my_image = Image.open(filename)
        img_tag = services.serve_pil_image(my_image)
        return render_template('base.html', image=img_tag)
    first_my_image = Image.open('images/image.jpg')
    first_img_tag = services.serve_pil_image(first_my_image)
    second_my_image = Image.open('images/image2.jpg')
    second_img_tag = services.serve_pil_image(second_my_image)
    third_my_image = Image.open('images/image3.jpg')
    third_img_tag = services.serve_pil_image(third_my_image)
    fourth_my_image = Image.open('images/audacious.jpg')
    fourth_img_tag = services.serve_pil_image(fourth_my_image)
    first_img_mask = Image.open('mask_images/first_image_mask.jpeg')
    second_img_mask = Image.open('mask_images/second_image_mask.jpeg')
    third_img_mask = Image.open('mask_images/third_image_mask.jpeg')
    fourth_img_mask = Image.open('mask_images/fourth_image_mask.jpeg')
    first_image_mask_tag = services.serve_pil_image(first_img_mask)
    second_image_mask_tag = services.serve_pil_image(second_img_mask)
    third_image_mask_tag = services.serve_pil_image(third_img_mask)
    fourth_image_mask_tag = services.serve_pil_image(fourth_img_mask)

    return render_template(
        'base_get.html', 
        image1=first_img_tag, 
        image1_mask=first_image_mask_tag,
        image2=second_img_tag, 
        image2_mask=second_image_mask_tag,
        image3=third_img_tag,
        image3_mask=third_image_mask_tag,
        image4=fourth_img_tag,
        image4_mask=fourth_image_mask_tag
    )
