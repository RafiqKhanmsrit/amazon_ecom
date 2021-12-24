import configparser

confile = configparser.RawConfigParser()
confile.read('.\\configarationfile\\config.ini')


class ConfigFile:
    @staticmethod
    def geturl():
        url = confile.get('comman useables', "url")
        return url

    @staticmethod
    def geuserid():
        userid = confile.get('comman useables', "userid")
        return userid

    @staticmethod
    def getpassword():
        password = confile.get('comman useables', "password")
        return password
