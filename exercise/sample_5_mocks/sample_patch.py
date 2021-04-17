import os


class RemovalService:

    def rm(self, filepath):
        os.remove(filepath)
