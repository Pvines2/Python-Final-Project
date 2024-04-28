import yagmail


class Emailer:
    sender_address = None
    _sole_instance = None

    @classmethod
    def configure(cls, sender_address):
        cls.sender_address = sender_address

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    def send_plain_email(self, recipients, subject, message):
        for recipient in recipients:
            print(f"Sending mail to: {recipient}")

    yag = yagmail.SMTP('parker.fake.cpsc@gmail.com')
    contents = [
        "This is the body, and here is just text http://somedomain/image.png",
        "You can find an audio file attached.", '/local/path/to/song.mp3'
    ]
    yag.send('to@someone.com', 'subject', contents)
