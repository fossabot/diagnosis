# -*- coding: utf-8 -*-
"""REST API views."""

from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse, abort
from .models import Code
from .utils import create_code


blueprint = Blueprint('api', __name__)
api = Api(blueprint)


class DiagnosisCode(Resource):
    def get_or_404(self, code_id):
        code = Code.query.get(code_id)
        if not code:
            abort(404, message="Code {} doesn't exist".format(code_id))

        return code

    def get(self, id):
        "Retrieve diagnosis codes by ID"
        code = self.get_or_404(id)
        return code.as_dict()

    def put(self, id):
        "Edit an existing diagnosis code record"
        code = self.get_or_404(id)
        data = self._parse_code_request()
        code.update(**data).save()
        return code.as_dict()

    def _parse_code_request(self):
        parser = reqparse.RequestParser()
        parser.add_argument('diagnosis_code', type=str)
        parser.add_argument('full_code', type=str)
        parser.add_argument('abbreviated_description', type=str)
        parser.add_argument('full_description', type=str)
        return parser.parse_args()

    def delete(self, id):
        "Delete a diagnosis code by ID"
        code = self.get_or_404(id)
        code.delete(id)
        return {'status': 'ok'}


class Diagnosis(Resource):

    PER_PAGE = 20

    def get(self):
        """
        List diagnosis codes.
        batches of 20 (and paginate through the rest of the record)
        """
        page = int(request.args.get('page', 1))
        query = Code.query.paginate(page=page, per_page=self.PER_PAGE)
        return [code.as_dict() for code in query.items]

    def post(self):
        "Create a new diagnosis code record"
        data = self._parse_code_request()
        code = create_code(**data)
        return code.as_dict()

    def _parse_code_request(self):
        parser = reqparse.RequestParser()
        parser.add_argument('category_code', type=str)
        parser.add_argument('category_title', type=str)
        parser.add_argument('diagnosis_code', type=str)
        parser.add_argument('full_code', type=str)
        parser.add_argument('abbreviated_description', type=str)
        parser.add_argument('full_description', type=str)
        return parser.parse_args()


api.add_resource(DiagnosisCode, '/diagnosis/<int:id>')
api.add_resource(Diagnosis, '/diagnosis')
