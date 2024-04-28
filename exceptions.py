class DuplicateOid(Exception):
    def __init__(self, oid, message="Duplicate OID found"):
        super().__init__(message)
        self.oid = oid


class DuplicateEmail(Exception):
    def __init__(self, email, message="Duplicate email found"):
        super().__init__(message)
        self.email = email
