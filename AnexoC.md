## Anexo C: Diccionario de Datos

Este diccionario describe la estructura de los datos procesados por el paquete  **RetailEngine** , detallando las variables originales del dataset *Online Retail* y las transformaciones realizadas para asegurar la integridad analítica.

### C.1. Variables de Entrada (Dataset Original)

| Nombre del Campo | Tipo Original | Descripción de Negocio                      | Tratamiento en RetailEngine                                                     |
| ---------------- | ------------- | -------------------------------------------- | ------------------------------------------------------------------------------- |
| `InvoiceNo`    | Object        | Identificador único de la transacción.     | Validado mediante**RegEx**para separar ventas de cancelaciones.           |
| `StockCode`    | Object        | Código alfanumérico del producto.          | Mantenido como identificador de catálogo.                                      |
| `Description`  | Object        | Nombre o descripción del artículo.         | Limpieza de espacios y normalización de texto.                                 |
| `Quantity`     | Int64         | Unidades vendidas por línea.                | Filtrado para excluir valores negativos no asociados a cancelaciones.           |
| `InvoiceDate`  | Object        | Fecha y hora de la operación.               | Transformado a tipo**datetime**para cálculos de recencia.                |
| `UnitPrice`    | Float64       | Precio unitario del producto en libras (£). | Validado para asegurar valores positivos mayores a cero.                        |
| `CustomerID`   | Float64       | ID único del cliente.                       | **Atributo Privado (`__`)** ; eliminación estricta de registros nulos. |
| `Country`      | Object        | País de residencia del cliente.             | Utilizado como clave para operaciones de**Join**geográfico.              |

### C.2. Variables Generadas (Capa de Ingeniería)

Estas variables no existen en el dataset original y son el resultado de la lógica de programación aplicada en los módulos `transformations.py` y `models.py`.

* **`Revenue` (Monetario)** :
* **Cálculo** : `Quantity` * `UnitPrice`.
* **Propósito** : Representa el ingreso bruto por línea de factura.
* **`Recency` (Recencia)** :
* **Cálculo** : Días transcurridos entre la fecha actual del sistema y la última compra del cliente.
* **Propósito** : Medir la vigencia del cliente en el ecosistema de la startup.
* **`Frequency` (Frecuencia)** :
* **Cálculo** : Conteo único (`nunique`) de `InvoiceNo` por cada `CustomerID`.
* **Propósito** : Determinar el hábito de consumo y lealtad.

---

### C.3. Resumen de Calidad del Dato Post-Procesamiento

Tras la ejecución del pipeline en `app.py`, el dataset alcanza los siguientes estándares de calidad:

* **Integridad** : 0% de valores nulos en los campos críticos de segmentación.
* **Veracidad** : Todas las facturas cumplen con el patrón técnico definido en el motor de  **RegEx** .
* **Consistencia** : Formatos de fecha y moneda estandarizados para su representación en la Sección 5 (Análisis Visual).
