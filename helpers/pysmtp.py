import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURACIÓN NECESARIA ---

# 1. Tu dirección de Gmail
SENDER_EMAIL = "tu_correo_de_gmail@gmail.com"

# 2. La contraseña de aplicación (NO es tu contraseña normal de Gmail)
#    Debes generarla en la configuración de seguridad de tu cuenta de Google.
SENDER_PASSWORD = "tu_contraseña_de_aplicacion"

# 3. El destinatario (puede ser el mismo SENDER_EMAIL)
RECEIVER_EMAIL = SENDER_EMAIL #"correo_destino@ejemplo.com"


# --- FUNCIÓN DE ENVÍO ---

def enviar_email(SUBJECT, BODY):
    """
    Establece una conexión segura con el servidor SMTP de Gmail y envía el correo.
    """
    
    # Crea el objeto MIME para el mensaje (permite formato de texto y otros adjuntos)
    mensaje = MIMEMultipart()
    mensaje["From"] = SENDER_EMAIL
    mensaje["To"] = RECEIVER_EMAIL
    mensaje["Subject"] = SUBJECT
    
    # Adjunta el cuerpo del mensaje como texto plano
    mensaje.attach(MIMEText(BODY, "html")) #plain
    
    try:
        # 1. Establece la conexión con el servidor SMTP de Gmail (puerto 587 para TLS)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls() # Inicia la seguridad TLS (Transport Layer Security)
        
        # 2. Inicia sesión en la cuenta de Gmail
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        # 3. Envía el correo
        texto_a_enviar = mensaje.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, texto_a_enviar)
        
        print("-> Correo enviado exitosamente.\n")
        
    except Exception as e:
        print(f"-> Error al enviar el correo: {e}")
        print("\n--- POSIBLES SOLUCIONES ---")
        print("1. Verifica que el correo y la contraseña de aplicación sean correctos.")
        print("2. Asegúrate de haber generado una CONTRASEÑA DE APLICACIÓN en tu cuenta de Google.")
        
    finally:
        # Cierra la conexión
        if 'server' in locals():
            server.quit()
