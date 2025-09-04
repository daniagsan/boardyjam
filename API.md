# 📚 API Reference - BoardyJam

## 📋 **Índice**

- [🎨 View Layer](#-view-layer)
- [🎮 Controller Layer](#-controller-layer)
- [📦 Model Layer](#-model-layer)
- [🔧 Widgets](#-widgets)
- [📊 Tipos de Datos](#-tipos-de-datos)
- [⚡ Eventos](#-eventos)
- [🔍 Ejemplos de Uso](#-ejemplos-de-uso)

---

## 🎨 **View Layer**

### **`boardyjam` (Clase Principal)**

**Ubicación**: `src/boardyjam/view/app.py`

**Hereda de**: `toga.App`

**Descripción**: Clase principal de la aplicación que maneja la interfaz de usuario y coordina las interacciones del usuario.

#### **Métodos**

##### `startup()`
```python
def startup(self) -> None
```
**Descripción**: Inicializa y configura la interfaz de usuario principal.

**Funcionalidad**:
- Crea el layout principal de la aplicación
- Inicializa componentes UI (labels, botones, image view)
- Configura el controlador de imágenes
- Establece la ventana principal

**Componentes creados**:
- `name_label`: Etiqueta de identificación
- `name_input`: Campo de entrada de texto
- `status_label`: Indicador de estado
- `image_view`: Visualizador de imágenes
- `button`: Botón de selección de imagen

##### `select_image(widget)`
```python
async def select_image(self, widget: toga.Widget) -> None
```
**Descripción**: Maneja el evento de selección de imagen desde la interfaz.

**Parámetros**:
- `widget` (toga.Widget): El widget que disparó el evento

**Funcionalidad**:
- Abre diálogo de selección de archivo
- Filtra por tipos de archivo soportados
- Delega procesamiento al controlador
- Maneja errores de diálogo

**Formatos soportados**: PNG, JPG, JPEG, BMP, GIF

##### `on_image_event(event_type, data)`
```python
def on_image_event(self, event_type: str, data: Any = None) -> None
```
**Descripción**: Observador que recibe eventos del controlador de imágenes.

**Parámetros**:
- `event_type` (str): Tipo de evento recibido
- `data` (Any, opcional): Datos asociados al evento

**Eventos manejados**:
- `'image_selected'`: Imagen seleccionada exitosamente
- `'image_display_ready'`: Imagen lista para mostrar
- `'image_error'`: Error en procesamiento

#### **Atributos**

| Atributo | Tipo | Descripción |
|----------|------|-------------|
| `image_controller` | `ImageController` | Controlador de lógica de imágenes |
| `name_input` | `toga.TextInput` | Campo de entrada de texto |
| `status_label` | `toga.Label` | Etiqueta de estado |
| `image_view` | `toga.ImageView` | Componente de visualización |
| `main_window` | `toga.MainWindow` | Ventana principal |

---

## 🎮 **Controller Layer**

### **`ImageController`**

**Ubicación**: `src/boardyjam/controller/image_controller.py`

**Descripción**: Controlador que gestiona la lógica de negocio relacionada con imágenes, implementando el patrón Observer.

#### **Métodos**

##### `__init__()`
```python
def __init__(self) -> None
```
**Descripción**: Inicializa el controlador con un modelo de imagen y lista de observadores.

**Inicializa**:
- `image_model`: Instancia de `ImageModel`
- `_observers`: Lista vacía de observadores

##### `add_observer(observer)`
```python
def add_observer(self, observer: Any) -> None
```
**Descripción**: Registra un observador para recibir notificaciones de eventos.

**Parámetros**:
- `observer` (Any): Objeto que implementa `on_image_event()`

**Requisitos del observador**:
- Debe tener método `on_image_event(event_type, data)`

##### `remove_observer(observer)`
```python
def remove_observer(self, observer: Any) -> None
```
**Descripción**: Remueve un observador de la lista de notificaciones.

**Parámetros**:
- `observer` (Any): Observador a remover

##### `select_image(file_path)`
```python
def select_image(self, file_path: str) -> bool
```
**Descripción**: Procesa la selección de una imagen con validación y carga.

**Parámetros**:
- `file_path` (str): Ruta completa al archivo de imagen

**Retorna**:
- `bool`: `True` si la selección fue exitosa, `False` en caso contrario

**Flujo de procesamiento**:
1. Validación de formato de archivo
2. Establecimiento en el modelo
3. Notificación de selección exitosa
4. Carga de datos para visualización

**Eventos emitidos**:
- `'image_selected'`: En selección exitosa
- `'image_error'`: En caso de error

##### `load_image_for_display()`
```python
def load_image_for_display(self) -> None
```
**Descripción**: Carga los datos de imagen para visualización en la interfaz.

**Funcionalidad**:
- Solicita carga de datos al modelo
- Notifica disponibilidad de imagen
- Maneja errores de carga

**Eventos emitidos**:
- `'image_display_ready'`: Imagen lista para mostrar
- `'image_error'`: Error en carga

##### `get_current_image()`
```python
def get_current_image(self) -> Optional[str]
```
**Descripción**: Obtiene la ruta de la imagen actualmente seleccionada.

**Retorna**:
- `Optional[str]`: Ruta de la imagen o `None` si no hay imagen

##### `validate_image_file(file_path)`
```python
def validate_image_file(self, file_path: str) -> bool
```
**Descripción**: Valida si un archivo tiene un formato de imagen soportado.

**Parámetros**:
- `file_path` (str): Ruta al archivo a validar

**Retorna**:
- `bool`: `True` si el formato es válido, `False` en caso contrario

**Formatos válidos**: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`

#### **Métodos Privados**

##### `_notify_observers(event_type, data)`
```python
def _notify_observers(self, event_type: str, data: Any = None) -> None
```
**Descripción**: Notifica a todos los observadores registrados sobre un evento.

**Parámetros**:
- `event_type` (str): Tipo de evento
- `data` (Any, opcional): Datos del evento

#### **Atributos**

| Atributo | Tipo | Descripción |
|----------|------|-------------|
| `image_model` | `ImageModel` | Modelo de datos de imagen |
| `_observers` | `List[Any]` | Lista de observadores registrados |

---

## 📦 **Model Layer**

### **`ImageModel`**

**Ubicación**: `src/boardyjam/model/image_model.py`

**Descripción**: Modelo que gestiona el estado y datos de las imágenes, incluyendo validación y carga de archivos.

#### **Métodos**

##### `__init__()`
```python
def __init__(self) -> None
```
**Descripción**: Inicializa el modelo con estado limpio.

**Estado inicial**:
- `image_path`: `None`
- `image_data`: `None`
- `is_loaded`: `False`

##### `set_image(path)`
```python
def set_image(self, path: str) -> None
```
**Descripción**: Establece la ruta de una nueva imagen y resetea el estado.

**Parámetros**:
- `path` (str): Ruta completa al archivo de imagen

**Efectos**:
- Establece `image_path`
- Resetea `is_loaded` a `False`
- Limpia `image_data`

##### `get_image_path()`
```python
def get_image_path(self) -> Optional[str]
```
**Descripción**: Obtiene la ruta de la imagen actual.

**Retorna**:
- `Optional[str]`: Ruta de la imagen o `None`

##### `load_image_data()`
```python
def load_image_data(self) -> bool
```
**Descripción**: Carga y valida los datos de la imagen desde el archivo.

**Retorna**:
- `bool`: `True` si la carga fue exitosa, `False` en caso contrario

**Validaciones realizadas**:
- Verificación de existencia del archivo
- Validación de que es un archivo válido
- Preparación de datos para Toga

**Excepciones**:
- `FileNotFoundError`: Si el archivo no existe
- `ValueError`: Si la ruta no es un archivo válido

##### `get_image_data()`
```python
def get_image_data(self) -> Optional[str]
```
**Descripción**: Obtiene los datos de imagen listos para visualización.

**Retorna**:
- `Optional[str]`: Datos de imagen si está cargada, `None` en caso contrario

##### `is_image_loaded()`
```python
def is_image_loaded(self) -> bool
```
**Descripción**: Verifica si la imagen está cargada y lista.

**Retorna**:
- `bool`: Estado de carga de la imagen

##### `clear_image()`
```python
def clear_image(self) -> None
```
**Descripción**: Limpia todos los datos de imagen y resetea el estado.

**Efectos**:
- `image_path` = `None`
- `image_data` = `None`
- `is_loaded` = `False`

#### **Atributos**

| Atributo | Tipo | Descripción |
|----------|------|-------------|
| `image_path` | `Optional[str]` | Ruta al archivo de imagen |
| `image_data` | `Optional[str]` | Datos procesados de la imagen |
| `is_loaded` | `bool` | Estado de carga de la imagen |

---

## 🔧 **Widgets**

### **Estructura de Widgets**

**Ubicación**: `src/boardyjam/widgets/`

**Estado**: Módulo preparado para componentes personalizados

**Uso futuro**:
- Componentes UI reutilizables
- Widgets especializados para imágenes
- Controles personalizados

---

## 📊 **Tipos de Datos**

### **Formatos de Imagen Soportados**

```python
SUPPORTED_FORMATS = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
```

### **Estados de Carga**

```python
class LoadState:
    NOT_LOADED = False
    LOADED = True
```

### **Tipos de Archivo en Diálogo**

```python
FILE_TYPES = ["png", "jpg", "jpeg", "bmp", "gif"]
```

---

## ⚡ **Eventos**

### **Sistema de Eventos Observer**

#### **Eventos Disponibles**

| Evento | Descripción | Datos |
|--------|-------------|-------|
| `'image_selected'` | Imagen seleccionada exitosamente | `str`: Ruta del archivo |
| `'image_display_ready'` | Imagen cargada y lista para mostrar | `str`: Datos de imagen |
| `'image_error'` | Error en cualquier operación | `str`: Mensaje de error |

#### **Implementación de Observador**

```python
class MyObserver:
    def on_image_event(self, event_type: str, data: Any = None) -> None:
        """Maneja eventos del sistema de imágenes."""
        if event_type == 'image_selected':
            print(f"Imagen seleccionada: {data}")
        elif event_type == 'image_display_ready':
            print("Imagen lista para mostrar")
        elif event_type == 'image_error':
            print(f"Error: {data}")
```

---

## 🔍 **Ejemplos de Uso**

### **Uso Básico del Controlador**

```python
from boardyjam.controller.image_controller import ImageController

# Crear controlador
controller = ImageController()

# Agregar observador
class SimpleObserver:
    def on_image_event(self, event_type, data=None):
        print(f"Evento: {event_type}, Datos: {data}")

observer = SimpleObserver()
controller.add_observer(observer)

# Seleccionar imagen
success = controller.select_image("/path/to/image.png")
if success:
    print("Imagen seleccionada exitosamente")
```

### **Uso del Modelo Directamente**

```python
from boardyjam.model.image_model import ImageModel

# Crear modelo
model = ImageModel()

# Establecer imagen
model.set_image("/path/to/image.jpg")

# Cargar datos
if model.load_image_data():
    print("Imagen cargada")
    data = model.get_image_data()
    print(f"Datos: {data}")
else:
    print("Error al cargar imagen")
```

### **Validación de Archivos**

```python
from boardyjam.controller.image_controller import ImageController

controller = ImageController()

# Validar diferentes formatos
files = [
    "image.png",    # ✅ Válido
    "image.jpg",    # ✅ Válido
    "document.pdf", # ❌ Inválido
    "image.gif"     # ✅ Válido
]

for file in files:
    is_valid = controller.validate_image_file(file)
    print(f"{file}: {'✅' if is_valid else '❌'}")
```

### **Implementación de Observador Personalizado**

```python
class CustomImageObserver:
    def __init__(self):
        self.images_processed = 0
        self.errors_count = 0
    
    def on_image_event(self, event_type, data=None):
        if event_type == 'image_selected':
            self.images_processed += 1
            print(f"Imagen #{self.images_processed}: {data}")
        
        elif event_type == 'image_display_ready':
            print("✅ Imagen lista para visualizar")
        
        elif event_type == 'image_error':
            self.errors_count += 1
            print(f"❌ Error #{self.errors_count}: {data}")
    
    def get_stats(self):
        return {
            'processed': self.images_processed,
            'errors': self.errors_count
        }

# Uso
observer = CustomImageObserver()
controller.add_observer(observer)

# Después de procesar imágenes
stats = observer.get_stats()
print(f"Procesadas: {stats['processed']}, Errores: {stats['errors']}")
```

---

## 🔧 **Extensión de la API**

### **Agregar Nuevos Formatos**

```python
# En ImageController.validate_image_file()
def validate_image_file(self, file_path):
    valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp']  # Agregar .webp
    return any(file_path.lower().endswith(ext) for ext in valid_extensions)
```

### **Nuevos Tipos de Eventos**

```python
# En ImageController
def process_image_filters(self, filter_type):
    """Ejemplo de nueva funcionalidad"""
    try:
        # Lógica de filtros
        self._notify_observers('filter_applied', filter_type)
    except Exception as e:
        self._notify_observers('filter_error', str(e))
```

### **Métodos de Utilidad**

```python
# Extensiones útiles para ImageModel
def get_image_size(self):
    """Obtiene el tamaño de la imagen."""
    if self.is_loaded and self.image_path:
        # Implementar lógica de tamaño
        pass

def get_image_format(self):
    """Obtiene el formato de la imagen."""
    if self.image_path:
        return self.image_path.split('.')[-1].upper()
    return None
```

---

*Esta documentación de API proporciona una referencia completa para desarrolladores que trabajen con BoardyJam. Para ejemplos más avanzados, consulta la [Documentación Técnica](TECHNICAL.md).*
