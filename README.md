# Proyecto de Interfaces Gráficas en Python (Tkinter)

Este repositorio contiene dos aplicaciones de escritorio desarrolladas en Python utilizando la biblioteca estándar `tkinter`:
1. **Calculadora Interactiva**: Una calculadora matemática con interfaz de botones.
2. **Formulario de Registro**: Una interfaz de captura de datos de usuario con validación estricta.

A continuación, se detallan las decisiones de diseño y los principios de programación de software aplicados en la construcción de ambos programas.

---

## 🏛️ Principios de Programación Aplicados

### 1. Programación Orientada a Objetos (POO)
Ambas aplicaciones (`Calculadora` y `FormularioRegistro`) están construidas utilizando clases. 
* **Encapsulamiento:** Toda la configuración de la ventana, las variables y las funciones de cada aplicación viven dentro de su propia clase. Esto evita que las variables se mezclen (variables globales) y hace que el código sea modular y reutilizable.

### 2. Separación de Responsabilidades (Separation of Concerns)
El código está dividido lógicamente para separar la **Vista** (lo que el usuario ve) de la **Lógica** (lo que el programa hace):
* En el formulario, la función `crear_widgets()` se encarga exclusivamente de dibujar la interfaz, mientras que `validar()` y `limpiar()` manejan la lógica de negocio y validación de datos.

### 3. Manejo Defensivo de Errores
Se implementaron bloques `try-except` para evitar que las aplicaciones se cierren de forma inesperada (crashes):
* En la **Calculadora**: Se envuelve la función `eval()` en un `try-except`. Si el usuario ingresa una operación matemática sin sentido (ej. `5++*2`), el programa lo atrapa y muestra un error amigable.
* En el **Formulario**: Se usa `try-except` al convertir la edad (`int()`) para atrapar el error si el usuario ingresa letras en lugar de números.

---

## 🎨 Decisiones de Diseño (UI/UX)

### 1. Sistema de Disposición (Layout Managers)
Se utilizaron los gestores de geometría de Tkinter de forma estratégica:
* **Grid (Cuadrícula):** Utilizado para estructurar los botones de la calculadora y los campos del formulario. Garantiza una alineación perfecta entre las etiquetas (Labels) y las cajas de texto (Entries).
* **Pack (Bloques):** Utilizado para agrupar elementos secundarios, como los botones de "Masculino/Femenino" o los botones finales de "Registrar" y "Limpiar", permitiendo que fluyan de manera natural y centrada.

### 2. Usabilidad y Seguridad de la Interfaz
* **Ventana de tamaño fijo en la calculadora:** Se utilizó `resizable(False, False)` para bloquear el tamaño de la ventana, garantizando que los botones no se deformen ni pierdan su simetría si el usuario intenta estirar la pantalla.
* **Ocultamiento de Contraseñas:** Se aplicó la propiedad `show="*"` en los campos de contraseña del formulario. Esto es un estándar de seguridad básico para proteger la privacidad del usuario mientras escribe.
* **Uso de variables de control (`StringVar`, `BooleanVar`):** Permiten que la interfaz gráfica y la lógica del programa se comuniquen en tiempo real, facilitando la limpieza del formulario con un solo clic.

### 3. Retroalimentación Inmediata (Feedback)
* **Validación exhaustiva:** El formulario no confía en la entrada del usuario. Verifica campos vacíos, longitud mínima de contraseñas y uso de expresiones regulares (`re`) para garantizar que el correo tenga un formato válido.
* **Alertas visuales (`messagebox`):** Se priorizó informar al usuario sobre lo que ocurre. Si hay múltiples errores en el formulario, se agrupan en una lista y se muestran todos juntos en una sola ventana de error, mejorando la experiencia del usuario (UX) al evitar mostrar múltiples alertas molestas.

---

## 🚀 Requisitos y Ejecución

* **Requisitos:** Python 3.x instalado. (La librería `tkinter` y `re` vienen incluidas por defecto en Python, por lo que no se requiere instalar paquetes externos).
* **Cómo ejecutar:**
  Abre una terminal o consola de comandos y ejecuta:
  ```bash
  python nombre_del_archivo.py