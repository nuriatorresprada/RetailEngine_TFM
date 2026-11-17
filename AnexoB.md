## Anexo B: Guía de Instalación y Despliegue

Esta guía detalla los pasos necesarios para configurar el entorno y ejecutar el paquete **RetailEngine** de manera exitosa. El software ha sido diseñado para ser agnóstico al sistema operativo, funcionando correctamente en Windows, macOS y Linux.

### B.1. Requisitos Previos

Antes de iniciar, asegúrese de contar con lo siguiente:

* **Python 3.8 o superior** instalado en el sistema.
* Gestor de paquetes **pip** actualizado.
* Acceso a una terminal (cmd, bash o zsh) o un entorno de  **Jupyter Notebook / Google Colab** .

### B.2. Instalación en Entorno Local (Recomendado)

Para evitar conflictos con otras librerías, se recomienda el uso de un entorno virtual.

1. **Clonar o descargar el proyecto** :
   Extraiga los archivos en una carpeta local (ej. `C:/Proyectos/RetailEngine`).
2. **Crear un entorno virtual** :
   **Bash**

```
   python -m venv venv
```

1. **Activar el entorno** :

* *Windows* : `venv\Scripts\activate`
* *macOS/Linux* : `source venv/bin/activate`

1. **Instalar el paquete en modo desarrollo** :
   Este paso es crucial, ya que utiliza el archivo `setup.py` para configurar todas las dependencias (Pandas, Matplotlib, Seaborn, etc.) automáticamente.
   **Bash**

```
   pip install -e .
```

### B.3. Ejecución del Sistema

Una vez instalado, el motor analítico puede dispararse mediante el orquestador principal:

**Bash**

```
python src/retail_engine/app.py
```

Al ejecutarse, el sistema realizará las siguientes acciones de forma automática:

* Validación de la estructura del dataset mediante  **RegEx** .
* Limpieza de nulos y duplicados.
* Generación de la matriz  **RFM** .
* Apertura de las ventanas gráficas con los resultados visuales.

### B.4. Despliegue en Google Colab

Si el tribunal desea ejecutar el proyecto en la nube para mayor comodidad, el procedimiento es el siguiente:

1. Subir la carpeta del proyecto a  **Google Drive** .
2. Abrir un nuevo Notebook en Colab y montar la unidad de Drive:
   **Python**

   ```
   from google.colab import drive
   drive.mount('/content/drive')
   ```
3. Navegar a la ruta del proyecto e instalar las dependencias:
   **Python**

   ```
   %cd /content/drive/MyDrive/RetailEngine
   !pip install .
   ```
4. Ejecutar el pipeline:
   **Python**

   ```
   !python src/retail_engine/app.py
   ```

### B.5. Solución de Problemas Frecuentes (Troubleshooting)

* **Error: FileNotFoundError** : Asegúrese de que el archivo `online_retail.csv` se encuentra dentro de la carpeta `data/`.
* **Error de Visualización** : En entornos Linux sin interfaz gráfica, el sistema guardará los gráficos automáticamente en la carpeta `/plots` en lugar de intentar abrirlos en pantalla.
