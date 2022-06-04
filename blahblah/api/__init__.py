import json

from flask import request, make_response
from flask_restx import Namespace, Resource

from blahblah.ocr import reader
from blahblah.s3.object import get_obj_binary
from blahblah.rekognition.detect import detect_labels
from blahblah.rekognition import ingredient_list
from blahblah.ocr import source_list

main_api = Namespace(
    "main",
    path="/",
    description="기본 api",
)

@main_api.route("/analyze")
class AnalyzeApi(Resource):
    def post(self):
        data = request.get_json()

        bucket = data.get("bucket")
        key = data.get("key")
        if bucket is None or key is None:
            return {"msg": "Bad Request"}, 400

        image_obj = get_obj_binary(bucket, key)

        # ocr
        ocr_res = reader.readtext(image_obj, detail=0)

        ocr_kor_res = set()
        for i in ocr_res:
            for j in source_list:
                if i in j :
                    ocr_kor_res.append(j)

        # label
        label_res = detect_labels(image_obj)

        label_kor_res=[ingredient_list[i] for i in label_res if(i in ingredient_list.keys())]
       

        return make_response(json.dumps({"res": ocr_kor_res + label_kor_res}, ensure_ascii=False))