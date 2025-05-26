from flask import Flask, render_template, request, jsonify
from database import Database
from cotizacion_service import CotizacionService

app = Flask(__name__)

# Instancias de la base de datos y el servicio de cotización
db = Database()
cotizacion_service = CotizacionService(db)

@app.route('/')
def formulario():
    return render_template('index.html')


# Esta ruta recibe los datos del formulario,
# procesa la cotización y devuelve el resultado en formato JSON
@app.route('/cotizar', methods=['POST'])
def cotizar():
    data = request.form
    resultado = cotizacion_service.cotizar(data)
    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True)
