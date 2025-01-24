from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.apis.teachers.schema import TeachersSchema
from core.models.teachers import Teacher


principal_teachers_resources = Blueprint("principal_teachers_resources", __name__)


# GET /principal/teachers
@principal_teachers_resources.route("/", methods=["GET"], strict_slashes=False)
@decorators.authenticate_principal
def get_all_teachers(p):
    """Get all the teachers"""
    teachers = Teacher.get_all_teachers()
    teachers_dump = TeachersSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teachers_dump)
