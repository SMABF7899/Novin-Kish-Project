from dotenv import dotenv_values


def set_config(envAddress):
    configName = None
    ENV = dotenv_values(envAddress)
    if ENV.get("BROWSER") == "Firefox":
        from Configs import firefoxConfig
        configName = firefoxConfig
    elif ENV.get("BROWSER") == "Chrome":
        from Configs import chromeConfig
        configName = chromeConfig
    return configName