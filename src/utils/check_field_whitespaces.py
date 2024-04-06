from flask_wtf import FlaskForm


class CheckFieldWhitespaces:
    @staticmethod
    def is_field_with_whitespaces(form: FlaskForm):
        for field in form:
            if field.name not in ["csrf_token", "submit"]:
                if field.data.startswith(" ") or field.data.endswith(" "):
                    return True
        return False
