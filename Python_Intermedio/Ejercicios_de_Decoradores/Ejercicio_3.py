from datetime import date


class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

def validate_decorator(func):
    def validate_age(user):
        if user.age < 18:
            raise ValueError("Es MENOR de edad")
        func(user)

    return validate_age


@validate_decorator
def is_adult(User):
    print("Es mayor de edad")


my_user = User(date(1992, 1, 1))
is_adult(my_user)

my_user = User(date(2025, 1, 1))
is_adult(my_user)