# 🎯 BoardyJam

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![BeeWare](https://img.shields.io/badge/BeeWare-Toga-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey.svg)

**Una aplicación de escritorio multiplataforma para gestión de imágenes construida con BeeWare/Toga**

[📖 Documentación](#-documentación) • [🚀 Instalación](#-instalación-rápida) • [💻 Uso](#-uso) • [🏗️ Arquitectura](#️-arquitectura) • [🤝 Contribuir](#-contribuir)

</div>

---

## 📋 **Descripción**

BoardyJam es una aplicación de escritorio multiplataforma desarrollada en Python que permite a los usuarios seleccionar, visualizar y gestionar imágenes de manera intuitiva. Construida con el framework BeeWare/Toga, la aplicación funciona nativamente en Windows, macOS, Linux, iOS, Android y Web.

### ✨ **Características Principales**

- 🖼️ **Selección de Imágenes**: Interfaz intuitiva para seleccionar archivos de imagen
- 🎨 **Visualización**: Vista previa de imágenes en tiempo real
- 📱 **Multiplataforma**: Funciona en todos los sistemas operativos principales
- 🏗️ **Arquitectura MVC**: Código bien estructurado y mantenible
- 🔍 **Validación**: Soporte para formatos PNG, JPG, JPEG, BMP, GIF
- ⚡ **Patrón Observer**: Actualizaciones reactivas de la interfaz

---

## 🚀 **Instalación Rápida**

### **Prerrequisitos**

- **Python 3.13+**: [Descargar aquí](https://www.python.org/downloads/)
- **Git**: [Descargar aquí](https://git-scm.com/downloads)

### **Pasos de Instalación**

1. **Clonar el repositorio**
   ```bash
   git clone <tu-repositorio-url>
   cd boardyjam
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv beeware-venv
   ```

3. **Activar entorno virtual**
   
   **Windows:**
   ```bash
   beeware-venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source beeware-venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   python -m pip install briefcase
   ```

5. **Ejecutar la aplicación**
   ```bash
   cd boardyjam
   briefcase dev
   ```

---

## 💻 **Uso**

### **Interfaz Principal**

1. **Seleccionar Imagen**: Haz clic en "Elegir imagen" para abrir el diálogo de selección
2. **Formatos Soportados**: PNG, JPG, JPEG, BMP, GIF
3. **Vista Previa**: La imagen seleccionada se mostrará automáticamente
4. **Estado**: El label inferior muestra el estado actual de la operación

### **Flujo de Trabajo**

```
Usuario selecciona imagen → Validación de formato → Carga en modelo → Actualización de vista
```

---

## 🏗️ **Arquitectura**

BoardyJam implementa el patrón **Model-View-Controller (MVC)** con **Observer Pattern**:

```
src/boardyjam/
├── __main__.py          # Punto de entrada
├── view/                # Capa de presentación
│   ├── app.py          # Interfaz principal
│   └── button_panel.py # Componentes UI
├── controller/          # Lógica de negocio
│   └── image_controller.py
├── model/              # Capa de datos
│   └── image_model.py
└── widgets/            # Componentes personalizados
```

### **Componentes Principales**

- **🎨 View Layer**: Interfaz de usuario con Toga
- **🎮 Controller Layer**: Lógica de negocio y coordinación
- **📦 Model Layer**: Gestión de datos y estado
- **🔄 Observer Pattern**: Comunicación reactiva entre capas

---

## 📖 **Documentación**

- **[📋 Documentación Técnica](TECHNICAL.md)**: Arquitectura detallada y patrones de diseño
- **[🤝 Guía de Contribución](CONTRIBUTING.md)**: Cómo contribuir al proyecto
- **[📚 API Reference](API.md)**: Documentación de clases y métodos
- **[🚀 Deployment Guide](DEPLOYMENT.md)**: Guía de despliegue multiplataforma

---

## 🛠️ **Desarrollo**

### **Estructura del Proyecto**

```
boardyjam/
├── src/boardyjam/       # Código fuente
├── tests/              # Pruebas unitarias
├── resources/          # Recursos de la aplicación
├── pyproject.toml      # Configuración del proyecto
└── README.md          # Este archivo
```

### **Comandos Útiles**

```bash
# Desarrollo
briefcase dev

# Construir para distribución
briefcase build

# Crear paquete
briefcase package

# Ejecutar tests
python -m pytest tests/
```

---

## 🤝 **Contribuir**

¡Las contribuciones son bienvenidas! Por favor lee nuestra [Guía de Contribución](CONTRIBUTING.md) para más detalles.

### **Proceso Rápido**

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 **Licencia**

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 👨‍💻 **Autor**

**Daniel Aguilera**
- 📧 Email: jdas_9920@hotmail.com
- 🌐 Proyecto: BoardyJam v0.0.1

---

## 🔗 **Enlaces Útiles**

- [📖 Documentación de BeeWare](https://docs.beeware.org/en/latest/index.html)
- [🐍 Python.org](https://www.python.org/)
- [📱 Toga Framework](https://toga.readthedocs.io/)

---

<div align="center">

**⭐ ¡Si te gusta este proyecto, dale una estrella! ⭐**

</div>
