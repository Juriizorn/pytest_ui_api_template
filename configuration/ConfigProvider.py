import configparser


class ConfigProvider:

    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config.read("test_config.ini")

    def get(self, section: str, prop: str) -> str:
        return self.config[section].get(prop)

    def getint(self, section: str, prop: str) -> int:
        return self.config[section].getint(prop)

    def get_ui_url(self) -> str:
        return self.config["ui"].get("base_url")