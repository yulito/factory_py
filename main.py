# Importamos la clase de lógica que acabamos de crear
from process_doc import ProcessDOC
from helpers.pysmtp import enviar_email

def main():
    """
    Función de entrada principal que inicializa y ejecuta el proceso.
    """
    
    # Enviando nombre de archivo con HU
    archivo_ext = "reporte_mensual.pdf"
    processor_ext = ProcessDOC(archivo_ext)
    processor_ext.process()
    print("---------------------------------\n")    

    # enviar correo con detalle de archivos guardados
    # --- CONFIGURACIÓN DEL MENSAJE ---
    file1="archivo.pdf"
    file2="archivo.docx"
    file3="archivo.txt"
    print("Enviando CORREO a cuenta de gmail...")
    SUBJECT = "Archivos subidos"
    BODY = f"""
        <h1 style='color:blue;'>TestGroup</h1><hr>
        <h3 style='color:green;'>Esta es la lista de archivos que contiene la tarjeta</h3>
        <ul>
            <li><strong>{file1}</strong></li>
            <li><strong>{file2}</strong></li>
            <li><strong>{file3}</strong></li>
        </ul>
        """
    enviar_email(SUBJECT, BODY)

# Ejecutar la función main si el archivo es el punto de entrada principal
if __name__ == "__main__":
    main()