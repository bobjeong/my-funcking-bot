import boto3
from utils.env import LocalEnv

class SessionMaker:
    def __init__(self) -> None:
        self._profile_name = LocalEnv.get_profile_name()
        self._region_name = LocalEnv.get_region_name()
        self._access_key_id = LocalEnv.get_access_key_id()
        self._secret_access_key = LocalEnv.get_secret_access_key()

    def makeSession(self):
        if self._profile_name is not None:
            return boto3.session.Session(profile_name=self._profile_name, region_name=self._region_name)
        else:
            return boto3.session.Session(aws_access_key_id=self._access_key_id, aws_secret_access_key=self._secret_access_key)
