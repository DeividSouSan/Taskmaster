from flask_wtf import FlaskForm

from ..repositories.user_repository import UserRepository


class CheckFormFields:
    @staticmethod
    def is_field_with_whitespaces(form: FlaskForm):
        for field in form:
            if field.name not in ["csrf_token", "submit"]:
                if field.data.startswith(" ") or field.data.endswith(" "):
                    return True
        return False


    @staticmethod
    def is_field_taken(self, values: list[dict[str, str]], repository: UserRepository) -> str | None:
        for field in values:
            if repository.exists_user_with_field(field["name"], field["value"]):
                return field["name"]

        return None
