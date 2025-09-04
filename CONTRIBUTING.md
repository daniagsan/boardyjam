# 🤝 Guía de Contribución - BoardyJam

¡Gracias por tu interés en contribuir a BoardyJam! Esta guía te ayudará a entender cómo puedes participar en el desarrollo del proyecto.

## 📋 **Índice**

- [🚀 Primeros Pasos](#-primeros-pasos)
- [🔧 Configuración del Entorno](#-configuración-del-entorno)
- [📝 Estándares de Código](#-estándares-de-código)
- [🌿 Flujo de Trabajo con Git](#-flujo-de-trabajo-con-git)
- [🧪 Testing](#-testing)
- [📖 Documentación](#-documentación)
- [🐛 Reporte de Bugs](#-reporte-de-bugs)
- [✨ Solicitud de Features](#-solicitud-de-features)
- [👥 Código de Conducta](#-código-de-conducta)

---

## 🚀 **Primeros Pasos**

### **Tipos de Contribuciones Bienvenidas**

- 🐛 **Corrección de bugs**
- ✨ **Nuevas funcionalidades**
- 📖 **Mejoras en documentación**
- 🧪 **Tests y cobertura**
- 🎨 **Mejoras en UI/UX**
- 🔧 **Optimizaciones de rendimiento**
- 🌐 **Soporte multiplataforma**

### **Antes de Contribuir**

1. **Revisa los issues existentes** para evitar trabajo duplicado
2. **Abre un issue** para discutir cambios grandes antes de implementarlos
3. **Lee esta guía completa** para entender nuestros estándares
4. **Configura tu entorno** siguiendo las instrucciones

---

## 🔧 **Configuración del Entorno**

### **1. Fork y Clone**

```bash
# Fork el repositorio en GitHub, luego:
git clone https://github.com/TU_USERNAME/boardyjam.git
cd boardyjam

# Agregar upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/boardyjam.git
```

### **2. Configurar Entorno Virtual**

```bash
# Crear entorno virtual
python -m venv beeware-venv

# Activar entorno virtual
# Windows:
beeware-venv\Scripts\activate
# macOS/Linux:
source beeware-venv/bin/activate

# Instalar dependencias
python -m pip install briefcase
python -m pip install pytest
python -m pip install black
python -m pip install flake8
```

### **3. Verificar Instalación**

```bash
cd boardyjam
briefcase dev
```

---

## 📝 **Estándares de Código**

### **Estilo de Código Python**

Seguimos **PEP 8** con algunas adaptaciones:

```python
# ✅ Correcto
class ImageController:
    """Controlador para gestión de imágenes."""
    
    def __init__(self):
        self.image_model = ImageModel()
        self._observers = []
    
    def select_image(self, file_path: str) -> bool:
        """Selecciona una imagen para procesar.
        
        Args:
            file_path: Ruta al archivo de imagen
            
        Returns:
            True si la selección fue exitosa, False en caso contrario
        """
        if not file_path:
            return False
        
        try:
            # Lógica de procesamiento
            return True
        except Exception as e:
            self._notify_observers('image_error', str(e))
            return False

# ❌ Incorrecto
class imagecontroller:
    def __init__(self):
        self.imageModel=ImageModel()
        self.observers=[]
    def selectImage(self,filePath):
        if not filePath:return False
        try:
            return True
        except:
            return False
```

### **Convenciones de Nomenclatura**

| Elemento | Convención | Ejemplo |
|----------|------------|---------|
| Clases | PascalCase | `ImageController` |
| Métodos/Funciones | snake_case | `select_image()` |
| Variables | snake_case | `file_path` |
| Constantes | UPPER_SNAKE_CASE | `MAX_FILE_SIZE` |
| Archivos | snake_case | `image_controller.py` |
| Métodos privados | _snake_case | `_notify_observers()` |

### **Documentación de Código**

```python
def validate_image_file(self, file_path: str) -> bool:
    """Valida si el archivo es una imagen válida.
    
    Verifica que el archivo tenga una extensión soportada y que
    el archivo exista en el sistema.
    
    Args:
        file_path (str): Ruta completa al archivo de imagen
        
    Returns:
        bool: True si el archivo es válido, False en caso contrario
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        
    Example:
        >>> controller = ImageController()
        >>> controller.validate_image_file("/path/to/image.png")
        True
    """
```

### **Manejo de Errores**

```python
# ✅ Correcto - Específico y descriptivo
try:
    self.image_model.load_image_data()
except FileNotFoundError as e:
    self._notify_observers('image_error', f"Archivo no encontrado: {e}")
except PermissionError as e:
    self._notify_observers('image_error', f"Sin permisos para leer: {e}")
except Exception as e:
    self._notify_observers('image_error', f"Error inesperado: {e}")

# ❌ Incorrecto - Muy genérico
try:
    self.image_model.load_image_data()
except:
    pass
```

---

## 🌿 **Flujo de Trabajo con Git**

### **1. Crear Rama de Feature**

```bash
# Actualizar main
git checkout main
git pull upstream main

# Crear nueva rama
git checkout -b feature/nueva-funcionalidad
# o
git checkout -b fix/corregir-bug
# o
git checkout -b docs/actualizar-documentacion
```

### **2. Realizar Cambios**

```bash
# Hacer commits pequeños y descriptivos
git add .
git commit -m "feat: agregar validación de formatos de imagen

- Implementar validación para PNG, JPG, JPEG
- Agregar tests para nuevos formatos
- Actualizar documentación de formatos soportados"
```

### **3. Convenciones de Commit**

Usamos **Conventional Commits**:

```bash
# Tipos de commit
feat: nueva funcionalidad
fix: corrección de bug
docs: cambios en documentación
style: formateo, espacios, etc.
refactor: refactorización de código
test: agregar o modificar tests
chore: tareas de mantenimiento

# Ejemplos
git commit -m "feat: agregar soporte para formato WebP"
git commit -m "fix: corregir error al cargar imágenes grandes"
git commit -m "docs: actualizar guía de instalación"
git commit -m "test: agregar tests para ImageController"
```

### **4. Push y Pull Request**

```bash
# Push a tu fork
git push origin feature/nueva-funcionalidad

# Crear Pull Request en GitHub con:
# - Título descriptivo
# - Descripción detallada
# - Referencias a issues relacionados
# - Screenshots si aplica
```

---

## 🧪 **Testing**

### **Ejecutar Tests**

```bash
# Todos los tests
python -m pytest tests/

# Tests específicos
python -m pytest tests/test_image_controller.py

# Con cobertura
python -m pytest tests/ --cov=src/boardyjam
```

### **Escribir Tests**

```python
# tests/test_image_controller.py
import pytest
from unittest.mock import Mock, patch
from boardyjam.controller.image_controller import ImageController

class TestImageController:
    def setup_method(self):
        """Configuración antes de cada test."""
        self.controller = ImageController()
        self.mock_observer = Mock()
        self.controller.add_observer(self.mock_observer)
    
    def test_validate_image_file_valid_extension(self):
        """Test que valida extensiones correctas."""
        assert self.controller.validate_image_file("test.png") == True
        assert self.controller.validate_image_file("test.jpg") == True
        assert self.controller.validate_image_file("test.jpeg") == True
    
    def test_validate_image_file_invalid_extension(self):
        """Test que rechaza extensiones incorrectas."""
        assert self.controller.validate_image_file("test.txt") == False
        assert self.controller.validate_image_file("test.pdf") == False
    
    @patch('os.path.exists')
    def test_select_image_file_not_found(self, mock_exists):
        """Test manejo de archivo no encontrado."""
        mock_exists.return_value = False
        
        result = self.controller.select_image("nonexistent.png")
        
        assert result == False
        self.mock_observer.on_image_event.assert_called_with(
            'image_error', 
            'Archivo no encontrado: nonexistent.png'
        )
```

### **Cobertura de Tests**

- **Mínimo 80%** de cobertura para nuevas funcionalidades
- **Tests unitarios** para lógica de negocio
- **Tests de integración** para flujos completos
- **Tests de UI** para componentes críticos

---

## 📖 **Documentación**

### **Actualizar Documentación**

Cuando agregues nuevas funcionalidades:

1. **README.md**: Actualizar características y ejemplos
2. **TECHNICAL.md**: Documentar arquitectura y patrones
3. **API.md**: Documentar nuevas clases y métodos
4. **Docstrings**: Documentar código inline

### **Formato de Documentación**

```markdown
## 🆕 **Nueva Funcionalidad**

### **Descripción**
Breve descripción de la funcionalidad.

### **Uso**
```python
# Ejemplo de código
controller = ImageController()
result = controller.nueva_funcionalidad()
```

### **Parámetros**
- `param1` (str): Descripción del parámetro
- `param2` (bool, opcional): Descripción del parámetro opcional

### **Retorna**
- `bool`: Descripción del valor de retorno
```

---

## 🐛 **Reporte de Bugs**

### **Antes de Reportar**

1. **Busca issues existentes** para evitar duplicados
2. **Reproduce el bug** en la última versión
3. **Recopila información** del sistema y error

### **Template de Bug Report**

```markdown
## 🐛 **Descripción del Bug**
Descripción clara y concisa del problema.

## 🔄 **Pasos para Reproducir**
1. Ir a '...'
2. Hacer clic en '...'
3. Scroll down to '...'
4. Ver error

## ✅ **Comportamiento Esperado**
Descripción de lo que debería pasar.

## ❌ **Comportamiento Actual**
Descripción de lo que está pasando.

## 📱 **Entorno**
- OS: [e.g. Windows 11, macOS 14, Ubuntu 22.04]
- Python: [e.g. 3.13.0]
- BeeWare/Toga: [e.g. 0.5.0]
- Versión BoardyJam: [e.g. 0.0.1]

## 📎 **Información Adicional**
- Screenshots
- Logs de error
- Archivos de ejemplo (si aplica)
```

---

## ✨ **Solicitud de Features**

### **Template de Feature Request**

```markdown
## 🚀 **Descripción del Feature**
Descripción clara de la funcionalidad solicitada.

## 🎯 **Problema que Resuelve**
¿Qué problema resuelve esta funcionalidad?

## 💡 **Solución Propuesta**
Descripción de cómo te gustaría que funcione.

## 🔄 **Alternativas Consideradas**
Otras soluciones que has considerado.

## 📋 **Información Adicional**
- Mockups o wireframes
- Ejemplos de implementación
- Referencias a otras aplicaciones
```

---

## 👥 **Código de Conducta**

### **Nuestros Valores**

- **Respeto**: Tratamos a todos con respeto y dignidad
- **Inclusión**: Valoramos la diversidad y diferentes perspectivas
- **Colaboración**: Trabajamos juntos hacia objetivos comunes
- **Aprendizaje**: Fomentamos el crecimiento y aprendizaje continuo

### **Comportamiento Esperado**

- ✅ Usar lenguaje inclusivo y respetuoso
- ✅ Ser constructivo en feedback y críticas
- ✅ Aceptar críticas constructivas graciosamente
- ✅ Enfocarse en lo que es mejor para la comunidad
- ✅ Mostrar empatía hacia otros miembros

### **Comportamiento Inaceptable**

- ❌ Lenguaje o imágenes sexualizadas
- ❌ Trolling, comentarios insultantes o despectivos
- ❌ Acoso público o privado
- ❌ Publicar información privada de otros
- ❌ Cualquier conducta inapropiada en un entorno profesional

---

## 📞 **Contacto y Soporte**

### **Canales de Comunicación**

- **Issues**: Para bugs y feature requests
- **Discussions**: Para preguntas generales y discusiones
- **Email**: jdas_9920@hotmail.com (para asuntos urgentes)

### **Tiempo de Respuesta**

- **Issues críticos**: 24-48 horas
- **Feature requests**: 1-2 semanas
- **Pull requests**: 3-5 días laborales

---

## 🎉 **Reconocimientos**

¡Valoramos todas las contribuciones! Los contribuidores serán reconocidos en:

- **README.md**: Lista de contribuidores
- **CHANGELOG.md**: Créditos por versión
- **Releases**: Menciones en notas de versión

---

**¡Gracias por contribuir a BoardyJam! 🚀**

*Tu participación hace que este proyecto sea mejor para toda la comunidad.*
