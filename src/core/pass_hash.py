import hashlib

from .settings import appsettings


class PassHash:
    def __init__(
        self,
        salt: str
    ) -> None:
        self.salt = salt
    
    def pass_hash(
        self,
        password: str
    ) -> str:
        sha_256 = hashlib.sha256()
        sha_256.update(
            f"{self.salt}{password}".encode()
        )
        return sha_256.hexdigest()
    
    def pass_check(
        self,
        password: str,
        password_hash: str,
    ) -> bool:
        return self.pass_hash(password) == password_hash
        

pass_hash = PassHash(salt=appsettings.HASH_SALT)
