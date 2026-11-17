# Changelog

Todos los cambios notables en el proyecto **RetailEngine** se documentan en este archivo, siguiendo los estándares de control de versiones para el Trabajo Final de Máster.

## [1.1.0] - 2026-04-24

### ✨ Añadido

* **Módulo de Analítica Temporal:** Implementación de la función `plot_temporal_revenue` para el análisis de estacionalidad mensual.
* **Exportación Automática:** Sistema de guardado automático de gráficos en `/plots` con resolución de 300 DPI para su inclusión directa en la memoria.
* **Detección Dinámica de Atributos:** Nuevo motor en `transformations.py` que identifica variables privadas (`__`) mediante inspección de diccionarios internos.

### 🛠️ Corregido

* **Error de Tipos:** Solucionado el conflicto `could not convert string to float` mediante un sistema de clasificación de datos por tipo (identificación de descripciones vs precios).
* **Problema de Fechas:** Corrección del error de "1970" asegurando la conversión forzada a `datetime` de Pandas tras la extracción del objeto.
* **Validación de Facturas:** Se ajustó la expresión regular (RegEx) en `services.py` para permitir mayor flexibilidad en el formato de los registros del dataset original sin perder integridad.

## [1.0.0] - 2026-04-22

### Añadido

* Integración final del módulo `app.py` como orquestador principal del pipeline.
* Generación de visualizaciones finales con **Matplotlib** y **Seaborn** para la memoria técnica.
* Finalización del empaquetado distribuible con `setup.py` y validación de instalación en entornos limpios.

## [0.9.0] - 2026-04-18

### Añadido

* Desarrollo del módulo `analytics.py` con lógica de visualización profesional.
* Implementación de la clase `RetailAnalytics` para el reporte de segmentación RFM.
* Documentación exhaustiva de todos los métodos siguiendo el estándar  **Numpy** .

## [0.8.0] - 2026-04-15

### Añadido

* Creación del módulo `transformations.py` para el procesamiento masivo de datos.
* Implementación de operaciones **GroupBy** para la síntesis de métricas de negocio.
* Lógica de **Join** para el enriquecimiento del dataset transaccional con datos maestros.

## [0.5.0] - 2026-04-11

### Añadido

* Desarrollo del módulo `services.py` con el motor de validación  **RegEx** .
* Implementación de la jerarquía de excepciones personalizadas en `exceptions.py`.

### Cambios

* Refactorización de la lógica de limpieza para manejar nulos críticos en `CustomerID` y `InvoiceNo`.

## [0.3.0] - 2026-04-07

### Añadido

* Definición de la arquitectura **POO** en el módulo `models.py`.
* Implementación de clases abstractas (`BaseTransaction`) y especializadas (`OnlineRetailTransaction`).
* Configuración de visibilidad de atributos (privados `__` y protegidos `_`).

## [0.1.0] - 2026-04-03

### Añadido

* Concepción inicial del proyecto y definición del alcance del motor analítico.
* Configuración del entorno de desarrollo y estructura de carpetas del paquete.
* Análisis exploratorio inicial del dataset "Online Retail" para identificar desafíos técnicos.
