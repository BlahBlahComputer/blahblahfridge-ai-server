import json

from flask import request, make_response
from flask_restx import Namespace, Resource

from blahblah.ocr import reader
from blahblah.s3.object import get_obj_binary

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
        res = reader.readtext(image_obj, detail=0)

        return make_response(json.dumps({"res": res}, ensure_ascii=False))