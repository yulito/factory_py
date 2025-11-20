# En el archivo ifactory/factory.py

# Importaciones del punto anterior van aquí:
from classimpl.readpdf import ReadPDF
from classimpl.readdocx import ReadDOCX
from classimpl.readtxt import ReadTXT
#from classimpl.readxls import ReadXLS
from classimpl.default import DefaultClass
from ifactory.interface import ReadingInterface # Opcional: para sugerencia de tipo (Type Hinting)

class ReaderFactory:
    
    # El método estático no necesita una instancia de la clase para ser llamado.
    @staticmethod
    def get_reader_object(extension: str) -> ReadingInterface:
        
        extension = extension.lower() # Normalizar a minúsculas para evitar errores
        
        if extension == "pdf":
            # Creamos y retornamos una instancia de la clase ReadPDF
            return ReadPDF()
        
        elif extension == "txt":
            # Creamos y retornamos una instancia de la clase ReadTXT
            return ReadTXT()
        
        elif extension == "docx" or extension == "doc":
            # Creamos y retornamos una instancia de la clase ReadDOCX  #xlsx xls
             return ReadDOCX()             

        else:
            # retornamos clase default
            return DefaultClass()
        
        """ elif extension == "xlsx" or extension == "xls":
            # Creamos y retornamos una instancia de la clase ReadDOCX  #xlsx xls
             return ReadXLS() """  