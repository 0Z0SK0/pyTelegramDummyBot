import json
import os

class CConfig():
    def __init__(self):
        self.workDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.configDir = self.workDir + "\\config"
        self.logDir = self.workDir + "\\logs"
        self.imagesDir = self.workDir + "\\public\\images"

        # Загружаем конфиг
        CONFIG_PATH = self.configDir + "\\config.json"
        with open(CONFIG_PATH) as config:
            data = json.load(config)

            self.APIKey = data['api_key']

            self.dbHost = data['db_host']
            self.dbUser = data['db_user']
            self.dbPass = data['db_pass']
            self.dbBase = data['db_base']

    def getWorkDirectory(self):
        # Рабочая директория
        return self.workDir
    
    def getConfigDirectory(self):
        # Директория конфиг-файлов
        return self.configDir
    
    def getLogDirectory(self):
        # Директория лог-файлов
        return self.logDir
    
    def getImagesDirectory(self):
        # Директория изображения
        return self.imagesDir
    
    def getAPIKey(self):
        # Telegram BOT API key
        return self.APIKey
    
    def getDatabaseHostname(self):
        # SQL Database Hostname
        return self.dbHost
    
    def getDatabaseUsername(self):
        # SQL Database Username
        return self.dbUser
    
    def getDatabasePassword(self):
        # SQL Database Password
        return self.dbPass
    
    def getDatabaseBase(self):
        # SQL Database base
        return self.dbBase