from django.core.exceptions import ValidationError
import re

email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
alpha_regex = re.compile(r'\w*[A-Z]\w*')
digit_regex = re.compile(r'[0-9]+')

class EmailValidator:
    def validate(self, email, user=None):
        if not re.fullmatch(email_regex, email):
            raiseValidationError(
                'Email invalid',
                code='email_no_valid'
            )

    def get_help_text(self):
        pass


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not re.fullmatch(alpha_regex, password):
            raiseValidationError(
                'Le mot de passe doit au moins contenir une lettre majuscule et une lettre miniscule',
                code='password_no_letter'
            )

    def get_help_text(self):
        pass


class ContainsDigitValidator:
    def validate(self, password, user=None):
        if not re.fullmatch(digit_regex, password):
            raiseValidationError(
                'Le mot de passe doit au moins contenir un nombre',
                code='password_no_digit'
            )

    def get_help_text(self):
        pass