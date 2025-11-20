from ifactory.interface import ReadingInterface

class ReadDOCX(ReadingInterface):
    def get_reading(self, file: str):
        return f"Leyendo contenidode archivo ...{file}"