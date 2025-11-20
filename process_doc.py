# Importar la clase ReaderFactory desde su módulo
from ifactory.factory import ReaderFactory

# --- Funciones Auxiliares ---

def get_extension(cadena: str) -> str:
   
    # Encontrar el índice (posición) del ÚLTIMO punto.
    ultimo_punto_indice = cadena.rfind('.')
    
    # Si no se encuentra un punto, retorna la cadena vacía.
    if ultimo_punto_indice == -1:
        return ""
    
    # Usar el slicing para obtener la subcadena desde el índice del punto + 1 hasta el final.
    return cadena[ultimo_punto_indice + 1:]

# --- Clase Principal ---

class ProcessDOC:
    """
    Clase que encapsula la lógica para procesar un documento 
    usando el patrón Factory.
    """
    
    def __init__(self, filename: str):
        """Inicializa la clase con el nombre del archivo a procesar."""
        self.filename = filename

    def process(self):
        """
        Método principal para procesar el archivo, obtener el lector 
        y extraer la información.
        """
        file = self.filename
        ext = get_extension(file) # obtenemos la extension del archivo

        if ext != "":
            try:
                # Obtenemos la instancia del objeto (ReaderPDF, ReaderTXT, etc.)
                doc_reader = ReaderFactory.get_reader_object(ext)

                # Llamamos al método implementado y extraemos su información
                # (Asumiendo que 'get_reading' es el método en la interfaz)
                get_info = doc_reader.get_reading(file)

                if get_info == "":
                    # Este mensaje lo guardamos en el log
                    print(f"[{file}] | LOG: No podemos extraer datos de este tipo de archivo con la extensión '{ext}'.")

                else:
                    # Mostramos la información extraída
                    print(f"--- Obteniendo la información de {file} ({ext.upper()}) ---")
                    print(str(get_info))                    
                
            except ValueError as e:
                # Manejo de error si la extensión no es soportada por la Factory
                print(f"[{file}] | LOG: Error al crear objeto: {e}")

        else:
            # Archivo sin extensión
            print(f"[{file}] | LOG: Archivo SIN extensión. No se puede procesar.")