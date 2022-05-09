from PIL import Image

from flask import Flask, render_template, request

import services
import run_inpaint


app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def main():
    if request.method == 'POST':
        form = request.form
        filename = run_inpaint.inpaint(form.get('text'), form.get('images'))
        my_image = Image.open(filename)
        img_tag = services.serve_pil_image(my_image)
        return render_template('base.html', image=img_tag)
    return render_template('base_get.html')


if __name__ == '__main__':
    app.run(debug=True)
