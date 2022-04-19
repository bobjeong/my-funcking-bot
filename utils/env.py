from os import environ
class LocalEnv:
    @classmethod
    def get_profile_name(cls):
        return LocalEnv._isExist('APP_PROFILE')
    
    @classmethod
    def get_region_name(cls):
        return LocalEnv._isExist('APP_REGION', 'ap-northeast-2')

    @classmethod
    def get_access_key_id(cls):
        return LocalEnv._isExist('AWS_ACCESS_KEY_ID')

    @classmethod
    def get_secret_access_key(cls):
        return LocalEnv._isExist('AWS_SECRET_ACCESS_KEY')

    @staticmethod
    def _isExist(env, default=""):
        print(env ,default)
        return environ.get(env) if environ.get(env) is not None else default