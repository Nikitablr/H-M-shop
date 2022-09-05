from faker import Faker

fake = Faker()


class SignupData:
    def __init__(self, email, password, confirm_email, date, month, year):
        self.email = email
        self.password = password
        self.date = date
        self.month = month
        self.year = year
        self.confirm_email = confirm_email

    @staticmethod
    def random():
        email = fake.email()
        password = fake.password()
        date = fake.date()
        month = fake.month()
        year = fake.year()
        confirm_email = email
        return SignupData(email=email, password=password, date=date, month=month, year=year,
                          confirm_email=confirm_email)