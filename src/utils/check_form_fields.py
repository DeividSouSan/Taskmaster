from flask_wtf import FlaskForm

from ..repositories.user_repository import UserRepository


class FieldWhitespaceChecker:
    def is_field_with_whitespaces(self, form: FlaskForm):
        for field in form:
            if field.name not in ["csrf_token", "submit"]:
                if field.data.startswith(" ") or field.data.endswith(" "):
                    return True
        return False


class FieldUniquenessChecker:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def is_field_taken(self, values: list[dict[str, str]]) -> str | None:
        for field in values:
            if self.__repository.exists_user_with_field(field["name"], field["value"]):
                return field["name"]
        return None
