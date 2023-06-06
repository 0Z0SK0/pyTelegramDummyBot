import CConfig

import asyncio
import mysql.connector

class CDatabase():
    def __init__(self):
        self.connection = mysql.connector.connect(
            user=CConfig.CConfig().getDatabaseUsername(),
            password=CConfig.CConfig().getDatabasePassword(),
            host=CConfig.CConfig().getDatabaseHostname(),
            database=CConfig.CConfig().getDatabaseBase()
        )
        self.connection.autocommit = True

    async def query(self, request):
        with self.connection.cursor(buffered=True) as self.cursor:
            self.cursor.execute(request)
            try:
                return self.cursor.fetchall()
            except Exception:
                pass