# RetailEngine_TFM

# 📊 Arquitectura de Software Orientada a Objetos para el Procesamiento y Visualización de Grandes Volúmenes de Datos en el Sector Retail (RetailEngine)

## Descripción (Español)

RetailEngine es un ecosistema analítico desarrollado en **Python** diseñado para transformar datos transaccionales brutos en inteligencia de negocio accionable. El sistema implementa un pipeline completo de datos, desde la ingesta masiva hasta la segmentación avanzada de clientes mediante el modelo  **RFM (Recency, Frequency, Monetary)** .

Este proyecto desarrolla un paquete profesional de Python para el análisis de comportamiento transaccional utilizando el dataset real **Online Retail** de la UCI.

El software realiza la extracción, validación, limpieza y segmentación de clientes mediante un motor orientado a objetos, siguiendo estrictamente los criterios de evaluación:

* Estilo **PEP8**.
* Documentación **Numpy**.
* **Programación Orientada a Objetos (** **POO** **)**.
* **Empaquetamiento distribuible**.

## 🛠️ Arquitectura Técnica y Soluciones Implementadas

Para este proyecto se han desarrollado soluciones a medida para desafíos comunes en el análisis de datos reales:

* **Ingesta Dinámica:** Soporte para codificación `latin1` y normalización de cabeceras, permitiendo procesar archivos con caracteres especiales (ej. £) y variaciones en los nombres de las columnas.
* **Tratamiento de Atributos Privados:** Implementación de un motor de transformación basado en inspección de diccionarios internos, garantizando la compatibilidad con el encapsulamiento de datos (POO).
* **Pipeline de Limpieza:** Filtrado preventivo de registros nulos y validación de facturas mediante  **Expresiones Regulares (RegEx)** .
* **Dashboard de Alta Resolución:** Generación automatizada de 6 gráficos clave exportados a 300 DPI, optimizados para documentación técnica y presentaciones ejecutivas.

### Funcionalidades principales:

* **Validación Robusta** **: Uso de expresiones regulares (** **RegEx** **) para garantizar la integridad de facturas y clientes**.
* **Análisis RFM**: Cálculo automatizado de Recencia, Frecuencia y Monetización mediante **Pandas**.
* **Visualización Avanzada** : Generación de reportes de estacionalidad y segmentación con **Matplotlib.**
* **Gestión de Errores** **: Jerarquía de excepciones personalizadas para entornos de producción**.
* **Arquitectura** : Aplicación de patrones de **Herencia** y **Composición**.
* **Pipeline POO Robusto:** Arquitectura basada en Programación Orientada a Objetos para separar la extracción, transformación y analítica.
* **Ingesta Inteligente:** Soporte para archivos CSV con codificación `latin1` y normalización dinámica de cabeceras.
* **Validación con RegEx:** Motor de validación para asegurar la integridad de los números de factura y registros.
* **Dashboard Automático:** Generación de 6 visualizaciones clave en alta resolución (300 DPI) para la memoria del TFM.

📌 **Diagrama UML del diseño de clases:**

![1776887680121](image/README/1776887680121.png)

## Description (English)

This project develops a professional Python package for transactional behavior analysis using the real **Online Retail** dataset from UCI.

The software performs extraction, validation, cleaning, and customer segmentation through an object-oriented engine, strictly following the evaluation criteria:

* **PEP8** coding style.
* **Numpy-style** documentation.
* **Object-Oriented Programming (** **OOP** **)**.
* **Distributable packaging**.

---

## 📂 Estructura del Proyecto / Project Structure

```
retail_engine/
│
├── data/
│   └── online_retail.csv
│
├── src/
│   └── retail_engine/
│       ├── __init__.py
│       ├── analytics.py      # Lógica de visualización y reportes
│       ├── app.py            # Orquestador y punto de entrada
│       ├── exceptions.py     # Jerarquía de errores personalizados
│       ├── models.py         # Definición de clases y POO
│       ├── services.py       # Extracción y validación RegEx
│       └── transformations.py # Operaciones GroupBy y Join
│
├── setup.py                  # Script de instalación del paquete
├── requirements.txt          # Dependencias del sistema
├── README.md                 # Documentación principal
├── CHANGELOG.md              # Registro de control de versiones
└── diagrama_uml.png          # Documentación visual de arquitectura
```

## 🛠️ Visualizaciones Generadas

El sistema genera automáticamente los siguientes análisis en la carpeta `/plots`:

1. **Evolución Temporal:** Análisis de ingresos mensuales para detectar estacionalidad.
2. **Dispersión RFM:** Correlación entre la frecuencia de compra y el valor monetario.
3. **Distribución de Ventas:** Histograma de la facturación por cliente.
4. **Análisis de Recency:** Distribución de días desde la última compra.
5. **Top 10 Productos:** Clasificación por volumen de ingresos.
6. **Top 5 Países:** Distribución geográfica de las ventas.

---

## 🛠️ Cómo ejecutar / How to Run

1. Asegúrate de tener instalado Python 3.10+ y las librerías necesarias:

   **Bash**

   ```
   pip install pandas matplotlib seaborn
   ```
2. **Instalar el paquete** en modo desarrollo para que las dependencias se gestionen automáticamente:

**Bash**

```
pip install -e .
```

3. **Ejecutar el motor analítico** desde el punto de entrada principal:

**Bash**

```
python src/app.py
```

---

## 📜 Funcionalidades de los Módulos

### `app.py`

**Archivo principal que orquesta el ciclo de vida del dato**:

* Coordina la extracción desde el `DataService`.
* Ejecuta el pipeline de limpieza y transformación.
* Dispara la generación de gráficos de negocio.

### `models.py`

Define la arquitectura **POO** del sistema:

* **Herencia** : Implementa una clase base abstracta para transacciones.
* **Encapsulamiento** **: Uso de atributos privados (**`<span class="citation-1372">__customer_id</span>`) y protegidos para seguridad de datos.

### `services.py`

Encargado de la robustez en la entrada de datos:

* **Implementa validaciones con **RegEx** para evitar "datos falsos" (prohibidos por normativa).
* Instancia los modelos de datos tras verificar su integridad.

### `transformations.py`

Módulo de procesamiento masivo con **Pandas**:

* Realiza operaciones de **GroupBy** para sintetizar el comportamiento del cliente.
* Ejecuta **Joins** para enriquecer el análisis con fuentes externas.

---

## 👨‍💻 Autor / Author

* **Nombre:** Nuria Torres Prada
* **Institución:** Centro de Estudios de Innovación (CEI)

---

## 🔖 Licencia / License

Este proyecto se entrega como **Proyecto Final de Máster** (TFM) para el CEI.

**Uso estrictamente académico y profesional bajo los criterios de evaluación de Python.**
