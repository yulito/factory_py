from ifactory.interface import ReadingInterface

class ReadTXT(ReadingInterface):
    def get_reading(self, file: str):
        return f"Leyendo contenidode archivo ...{file}"