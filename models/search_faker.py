from faker import Faker

fake = Faker()
fake.pystr(min_chars=None, max_chars=3)


class SearchData:
    def __init__(self, text):
        self.text = text


    @staticmethod
    def random():
        text = fake.text()
        return SearchData(text=text)