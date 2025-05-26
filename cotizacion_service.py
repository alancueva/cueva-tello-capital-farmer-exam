from datetime import datetime
import uuid

# clase CotizacionService que maneja la lógica de cotización
class CotizacionService:
    def __init__(self, db):
        self.db = db
        self.precios = {
            'Constitución de empresa - S/ 1,500': 1500,
            'Defensa laboral - S/ 2,000': 2000,
            'Consultoría tributaria - S/ 800': 800
        }

    """Genera un código único para la cotización."""
    def generar_codigo(self):
        return f'COT-2025-{str(uuid.uuid4())[:8].upper()}'

    """Realiza la cotización de un servicio y guarda los datos en la base de datos."""
    def cotizar(self, data):

        if not data.get('nombre') or not data.get('email'):
            return {
                'success': False,
                'descripcion': "Nombre y email son obligatorios."
            }
        servicio = data['servicio']
        precio = self.precios.get(servicio, 0)
        numero = self.generar_codigo()
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:
            self.db.insertar_cotizacion(
                numero, data['nombre'], data['email'], servicio, precio, fecha
            )
            return {
                'success': True,
                'descripcion': "Cotización registrada correctamente."
            }
        except Exception as e:
            return {
                'success': False,
                'descripcion': f"Error al registrar la cotización: {str(e)}"
            }
