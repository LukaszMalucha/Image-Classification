from flask import Response, render_template, request
from flask_restful import Resource


import requests
import subprocess
import json

import os.path


## PATHS ############################################################################

my_path = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(my_path, "../../static/classify_image/classify_image.py")
folder_path = os.path.join(my_path, "../../static/classify_image/")
file_path = os.path.join(my_path, "../../static/classify_image/text.txt")
image_path = os.path.join(my_path, "../../static/classify_image/temp.jpg")


## RESOURCES #########################################################################


class ImageClassify(Resource):
    def get(self):

        return Response( render_template("classify_image.html"))


    def post(self):


        ## Get the Image URL
        url = request.form['url']
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            return Response(render_template('404.html'))


        warning = ''

        ## Pass image to the TF model
        with open(image_path, 'wb') as m:
            m.write(r.content)
            proc = subprocess.Popen \
                ('python {} --model_dir={} --image_file={}'.format(model_path, folder_path, image_path), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            ret = proc.communicate()[0]
            proc.wait()
        with open(file_path) as f:
            retJson = json.load(f)


        ## Get Percentage Value
        retJson.update((x, y* 100) for x, y in retJson.items())

        if not retJson:
            warning = "File path not recognized"

        return Response(
            render_template('imageclassify.html', retJson=retJson, url=url, warning=warning, mimetype='text/html'))
