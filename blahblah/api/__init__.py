from flask_restx import Namespace, Resource

from blahblah.common.response import create_response

main_api = Namespace(
    "main",
    path="/",
    description="기본 api",
)

@main_api.route("/analyze")
class AnalyzeApi(Resource):
    def post(self):
        return create_response("hi", 200)