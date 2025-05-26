# Sistema de Cotizaciones - Capital & Farmer

Este proyecto es una aplicación web desarrollada con Flask que permite a los usuarios solicitar cotizaciones para servicios jurídicos de manera sencilla y rápida. Los datos de las cotizaciones se almacenan en una base de datos SQLite para su posterior consulta y gestión.

## Características

- Formulario web moderno y responsivo para solicitar cotizaciones.
- Procesamiento de cotizaciones en el backend con generación automática de código único.
- Almacenamiento seguro de las cotizaciones en una base de datos SQLite.
- Respuesta inmediata con los detalles de la cotización generada.
- Código organizado en módulos para fácil mantenimiento y escalabilidad.

## Estructura del Proyecto

```
.
├── app.py                   # Archivo principal de la aplicación Flask
├── cotizacion_service.py    # Lógica de negocio para cotizaciones
├── database.py              # Manejo de la base de datos SQLite
├── database.db              # Archivo de la base de datos SQLite
├── static/
│   └── css/
│       └── style.css        # Estilos CSS personalizados
├── templates/
│   └── index.html           # Plantilla HTML principal
└── README.md                # Documentación del proyecto
```

## Instalación y Ejecución

1. **Clona el repositorio**  
   ```bash
   git clone https://github.com/alancueva/cueva-tello-capital-farmer-exam.git
   cd cueva-tello-capital-farmer-exam
   ```

2. **Instala las dependencias**  
   Se recomienda usar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install flask
   ```

3. **Ejecuta la aplicación**  
   ```bash
   python app.py
   flask run
   ```
   La aplicación estará disponible en [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Uso

1. Accede a la página principal.
2. Completa el formulario con tus datos y selecciona el servicio jurídico.
3. Haz clic en "Generar Cotización".
4. Recibirás una cotización con un código único y el precio correspondiente.

## Archivos principales

- **app.py**: Configura las rutas de Flask y conecta el frontend con el backend.
- **cotizacion_service.py**: Lógica para calcular precios y generar códigos de cotización.
- **database.py**: Inicializa y gestiona la base de datos SQLite.
- **index.html**: Formulario web para la solicitud de cotizaciones.
- **style.css**: Estilos visuales modernos y responsivos.

## Personalización

Puedes modificar los servicios y precios en el archivo `cotizacion_service.py` dentro del diccionario `self.precios`.

## Licencia

Este proyecto está licenciado bajo los términos de la [licencia MIT](LICENSE).
