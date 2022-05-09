from PIL import Image

from app import app

from flask import render_template, request

from app import services
from app import run_inpaint

@app.route("/", methods=('GET', 'POST'))
def main():
    if request.method == 'POST':
        form = request.form
        filename = run_inpaint.inpaint(form.get('text'), form.get('images'))
        my_image = Image.open(filename)
        img_tag = services.serve_pil_image(my_image)
        return render_template('base.html', image=img_tag)
    return render_template('base_get.html')
