# 🏗️ Documentación Técnica - BoardyJam

## 📋 **Índice**

- [🎯 Arquitectura General](#-arquitectura-general)
- [🏛️ Patrón MVC](#️-patrón-mvc)
- [🔄 Patrón Observer](#-patrón-observer)
- [📦 Componentes Detallados](#-componentes-detallados)
- [🔀 Flujo de Datos](#-flujo-de-datos)
- [🛠️ Tecnologías Utilizadas](#️-tecnologías-utilizadas)
- [📊 Diagramas](#-diagramas)

---

## 🎯 **Arquitectura General**

BoardyJam implementa una arquitectura **Model-View-Controller (MVC)** con **Observer Pattern** para crear una aplicación desktop multiplataforma robusta y mantenible.

### **Principios de Diseño**

- **Separación de Responsabilidades**: Cada capa tiene una responsabilidad específica
- **Bajo Acoplamiento**: Los componentes están débilmente acoplados
- **Alta Cohesión**: Cada módulo tiene una función bien definida
- **Extensibilidad**: Fácil agregar nuevas funcionalidades
- **Testabilidad**: Arquitectura que facilita las pruebas unitarias

---

## 🏛️ **Patrón MVC**

### **📱 Model (Modelo)**
**Ubicación**: `src/boardyjam/model/`

**Responsabilidades**:
- Gestión del estado de la aplicación
- Validación de datos
- Operaciones de archivo
- Lógica de negocio pura

```python
# image_model.py
class ImageModel:
    def __init__(self):
        self.image_path = None      # Ruta del archivo
        self.image_data = None      # Datos de la imagen
        self.is_loaded = False      # Estado de carga
```

### **🎨 View (Vista)**
**Ubicación**: `src/boardyjam/view/`

**Responsabilidades**:
- Interfaz de usuario
- Manejo de eventos de UI
- Presentación de datos
- Interacción con el usuario

```python
# app.py
class boardyjam(toga.App):
    def startup(self):
        # Configuración de la interfaz
        # Componentes UI (botones, labels, etc.)
        # Layout y estilos
```

### **🎮 Controller (Controlador)**
**Ubicación**: `src/boardyjam/controller/`

**Responsabilidades**:
- Coordinación entre Model y View
- Lógica de aplicación
- Manejo de eventos
- Implementación del patrón Observer

```python
# image_controller.py
class ImageController:
    def __init__(self):
        self.image_model = ImageModel()
        self._observers = []
```

---

## 🔄 **Patrón Observer**

### **Implementación**

El patrón Observer permite que la Vista se actualice automáticamente cuando cambia el estado del Modelo, sin crear dependencias directas.

```python
# En ImageController
def _notify_observers(self, event_type, data=None):
    """Notifica a todos los observadores sobre cambios"""
    for observer in self._observers:
        if hasattr(observer, 'on_image_event'):
            observer.on_image_event(event_type, data)

# En la Vista (app.py)
def on_image_event(self, event_type, data=None):
    """Observador para eventos del controlador"""
    if event_type == 'image_selected':
        # Actualizar UI
    elif event_type == 'image_display_ready':
        # Mostrar imagen
    elif event_type == 'image_error':
        # Mostrar error
```

### **Eventos Disponibles**

| Evento | Descripción | Datos |
|--------|-------------|-------|
| `image_selected` | Imagen seleccionada exitosamente | Ruta del archivo |
| `image_display_ready` | Imagen lista para mostrar | Datos de imagen |
| `image_error` | Error en operación | Mensaje de error |

---

## 📦 **Componentes Detallados**

### **1. Punto de Entrada (`__main__.py`)**

```python
from boardyjam.view.app import main

if __name__ == "__main__":
    main().main_loop()
```

**Función**: Inicializa y ejecuta la aplicación principal.

### **2. Aplicación Principal (`view/app.py`)**

**Clase**: `boardyjam(toga.App)`

**Métodos Principales**:
- `startup()`: Configura la interfaz inicial
- `select_image()`: Maneja la selección de imágenes
- `on_image_event()`: Observador de eventos del controlador

**Componentes UI**:
- `name_label`: Etiqueta de identificación
- `name_input`: Campo de texto
- `status_label`: Indicador de estado
- `image_view`: Visualizador de imágenes
- `button`: Botón de selección

### **3. Controlador de Imágenes (`controller/image_controller.py`)**

**Clase**: `ImageController`

**Métodos Principales**:
- `select_image(file_path)`: Procesa selección de imagen
- `load_image_for_display()`: Prepara imagen para visualización
- `validate_image_file(file_path)`: Valida formato de archivo
- `add_observer(observer)`: Registra observador
- `_notify_observers(event, data)`: Notifica cambios

**Flujo de Procesamiento**:
1. Validación de formato
2. Establecer imagen en modelo
3. Notificar selección
4. Cargar datos para visualización
5. Notificar disponibilidad

### **4. Modelo de Imagen (`model/image_model.py`)**

**Clase**: `ImageModel`

**Atributos**:
- `image_path`: Ruta del archivo de imagen
- `image_data`: Datos procesados de la imagen
- `is_loaded`: Estado de carga

**Métodos Principales**:
- `set_image(path)`: Establece nueva imagen
- `load_image_data()`: Carga datos del archivo
- `get_image_data()`: Obtiene datos cargados
- `clear_image()`: Limpia estado

---

## 🔀 **Flujo de Datos**

### **Selección de Imagen**

```mermaid
graph TD
    A[Usuario hace clic en botón] --> B[View: select_image()]
    B --> C[Diálogo de selección]
    C --> D[Controller: select_image()]
    D --> E[Validar formato]
    E --> F{¿Formato válido?}
    F -->|Sí| G[Model: set_image()]
    F -->|No| H[Notificar error]
    G --> I[Notificar selección]
    I --> J[Controller: load_image_for_display()]
    J --> K[Model: load_image_data()]
    K --> L[Notificar imagen lista]
    L --> M[View: actualizar UI]
    H --> M
```

### **Comunicación Entre Capas**

```
┌─────────────┐    eventos    ┌──────────────┐    métodos    ┌─────────────┐
│    View     │ ──────────→   │ Controller   │ ──────────→   │   Model     │
│   (UI)      │               │  (Lógica)    │               │  (Datos)    │
└─────────────┘               └──────────────┘               └─────────────┘
       ↑                             │                              │
       │          Observer           │                              │
       └─────────────────────────────┘                              │
                Pattern                                              │
                                                                     │
       ┌─────────────────────────────────────────────────────────────┘
       │                    Estado/Datos
       ↓
```

---

## 🛠️ **Tecnologías Utilizadas**

### **Framework Principal**
- **BeeWare/Toga**: Framework multiplataforma para Python
- **Briefcase**: Herramienta de empaquetado y distribución

### **Lenguaje y Versión**
- **Python 3.13**: Lenguaje de programación principal
- **Asyncio**: Para operaciones asíncronas (diálogos de archivo)

### **Patrones de Diseño**
- **MVC (Model-View-Controller)**: Arquitectura principal
- **Observer Pattern**: Comunicación reactiva
- **Singleton Pattern**: Para instancias únicas (implícito en App)

### **Formatos Soportados**
- **PNG**: Portable Network Graphics
- **JPG/JPEG**: Joint Photographic Experts Group
- **BMP**: Bitmap
- **GIF**: Graphics Interchange Format

---

## 📊 **Diagramas**

### **Diagrama de Clases**

```
┌─────────────────┐
│   boardyjam     │
│   (toga.App)    │
├─────────────────┤
│ + startup()     │
│ + select_image()│
│ + on_image_event│
└─────────────────┘
         │
         │ usa
         ↓
┌─────────────────┐
│ImageController  │
├─────────────────┤
│ - image_model   │
│ - _observers[]  │
├─────────────────┤
│ + select_image()│
│ + add_observer()│
│ + validate_file()│
└─────────────────┘
         │
         │ controla
         ↓
┌─────────────────┐
│   ImageModel    │
├─────────────────┤
│ - image_path    │
│ - image_data    │
│ - is_loaded     │
├─────────────────┤
│ + set_image()   │
│ + load_data()   │
│ + get_data()    │
└─────────────────┘
```

### **Diagrama de Secuencia - Selección de Imagen**

```
Usuario    View       Controller    Model
  │         │             │          │
  │ click   │             │          │
  ├────────→│             │          │
  │         │select_image │          │
  │         ├────────────→│          │
  │         │             │set_image │
  │         │             ├─────────→│
  │         │             │          │
  │         │on_image_event│         │
  │         │←────────────┤          │
  │         │             │load_data │
  │         │             ├─────────→│
  │         │             │          │
  │         │on_image_event│         │
  │         │←────────────┤          │
  │ update  │             │          │
  │←────────┤             │          │
```

---

## 🔧 **Configuración y Extensibilidad**

### **Agregar Nuevos Formatos de Imagen**

1. Modificar `validate_image_file()` en `ImageController`
2. Actualizar lista de extensiones válidas
3. Agregar soporte en el diálogo de selección

### **Agregar Nuevos Eventos**

1. Definir nuevo tipo de evento en `ImageController`
2. Implementar lógica de notificación
3. Manejar evento en `on_image_event()` de la Vista

### **Extensión de Funcionalidades**

- **Edición de Imágenes**: Agregar nuevo controlador `EditController`
- **Filtros**: Implementar `FilterModel` y `FilterController`
- **Galería**: Crear `GalleryView` y `GalleryController`

---

## 📝 **Notas de Implementación**

### **Manejo de Errores**

- Validación en múltiples capas
- Propagación controlada de excepciones
- Feedback visual al usuario

### **Rendimiento**

- Carga asíncrona de imágenes
- Validación temprana de formatos
- Gestión eficiente de memoria

### **Multiplataforma**

- Uso de rutas compatibles (`pathlib`)
- Diálogos nativos del sistema
- Estilos adaptativos

---

*Esta documentación técnica proporciona una visión completa de la arquitectura y implementación de BoardyJam. Para más detalles sobre el uso, consulta el [README.md](README.md).*
