from flask import Flask, request, render_template, send_file
from venn_diagram import create_venn_diagram
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        genes1 = request.form['genes1'].split(',')
        genes2 = request.form['genes2'].split(',')
        venn_path = create_venn_diagram(genes1, genes2)
        return render_template('index.html', venn_image=venn_path)
    return render_template('index.html', venn_image=None)

if __name__ == '__main__':
    app.run(debug=True)
