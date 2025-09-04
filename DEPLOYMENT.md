# 🚀 Guía de Despliegue - BoardyJam

## 📋 **Índice**

- [🎯 Introducción](#-introducción)
- [🛠️ Preparación del Entorno](#️-preparación-del-entorno)
- [💻 Despliegue Local](#-despliegue-local)
- [📦 Empaquetado Multiplataforma](#-empaquetado-multiplataforma)
- [🌐 Distribución](#-distribución)
- [🔧 Configuración Avanzada](#-configuración-avanzada)
- [🐛 Solución de Problemas](#-solución-de-problemas)

---

## 🎯 **Introducción**

BoardyJam utiliza **BeeWare/Briefcase** para crear aplicaciones nativas multiplataforma desde un único código base Python. Esta guía te ayudará a desplegar la aplicación en diferentes plataformas.

### **Plataformas Soportadas**

- 🖥️ **Desktop**: Windows, macOS, Linux
- 📱 **Mobile**: iOS, Android
- 🌐 **Web**: Progressive Web App (PWA)

---

## 🛠️ **Preparación del Entorno**

### **Requisitos Generales**

- **Python 3.13+**
- **Git**
- **Briefcase** (incluido en BeeWare)

### **Instalación de Dependencias**

```bash
# Clonar repositorio
git clone <repository-url>
cd boardyjam

# Crear entorno virtual
python -m venv beeware-venv

# Activar entorno virtual
# Windows:
beeware-venv\Scripts\activate
# macOS/Linux:
source beeware-venv/bin/activate

# Instalar Briefcase
python -m pip install briefcase
```

---

## 💻 **Despliegue Local**

### **Modo Desarrollo**

```bash
cd boardyjam
briefcase dev
```

**Características**:
- Ejecución directa desde código fuente
- Recarga automática en cambios
- Ideal para desarrollo y testing

### **Verificar Configuración**

```bash
# Verificar configuración del proyecto
briefcase dev --help

# Ver información del proyecto
briefcase --version
```

---

## 📦 **Empaquetado Multiplataforma**

### **🖥️ Windows**

#### **Preparación**

```bash
# Instalar dependencias específicas de Windows
python -m pip install briefcase[windows]
```

#### **Construcción**

```bash
# Crear aplicación
briefcase create windows

# Construir aplicación
briefcase build windows

# Empaquetar para distribución
briefcase package windows
```

**Salida**: Archivo `.msi` en `dist/`

#### **Ejecución**

```bash
# Ejecutar aplicación construida
briefcase run windows
```

### **🍎 macOS**

#### **Preparación**

```bash
# Instalar Xcode Command Line Tools
xcode-select --install

# Instalar dependencias específicas de macOS
python -m pip install briefcase[macOS]
```

#### **Construcción**

```bash
# Crear aplicación
briefcase create macOS

# Construir aplicación
briefcase build macOS

# Empaquetar para distribución
briefcase package macOS
```

**Salida**: Archivo `.dmg` en `dist/`

#### **Firma de Código (Opcional)**

```bash
# Configurar certificado de desarrollador
export CODESIGN_IDENTITY="Developer ID Application: Your Name"

# Empaquetar con firma
briefcase package macOS --adhoc-sign
```

### **🐧 Linux**

#### **Preparación**

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-dev python3-venv

# Instalar dependencias específicas de Linux
python -m pip install briefcase[linux]
```

#### **Construcción**

```bash
# Crear aplicación
briefcase create linux

# Construir aplicación
briefcase build linux

# Empaquetar para distribución
briefcase package linux
```

**Formatos disponibles**:
- **AppImage**: Portable
- **Flatpak**: Distribución moderna
- **Snap**: Ubuntu Store

#### **AppImage**

```bash
briefcase package linux appimage
```

#### **Flatpak**

```bash
briefcase package linux flatpak
```

### **📱 Android**

#### **Preparación**

```bash
# Instalar Android SDK
# Descargar desde: https://developer.android.com/studio

# Configurar variables de entorno
export ANDROID_HOME=/path/to/android-sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# Instalar dependencias
python -m pip install briefcase[android]
```

#### **Construcción**

```bash
# Crear aplicación
briefcase create android

# Construir aplicación
briefcase build android

# Empaquetar APK
briefcase package android
```

**Salida**: Archivo `.apk` en `dist/`

### **📱 iOS**

#### **Preparación**

```bash
# Requiere macOS y Xcode
# Instalar Xcode desde App Store

# Instalar dependencias
python -m pip install briefcase[iOS]
```

#### **Construcción**

```bash
# Crear aplicación
briefcase create iOS

# Construir aplicación
briefcase build iOS

# Empaquetar para distribución
briefcase package iOS
```

**Nota**: Requiere cuenta de desarrollador de Apple para distribución.

### **🌐 Web**

#### **Preparación**

```bash
# Instalar dependencias web
python -m pip install briefcase[web]
```

#### **Construcción**

```bash
# Crear aplicación web
briefcase create web

# Construir aplicación
briefcase build web

# Servir localmente
briefcase run web
```

**Salida**: Aplicación web estática en `dist/`

---

## 🌐 **Distribución**

### **📦 Distribución Desktop**

#### **Windows**

```bash
# Crear instalador MSI
briefcase package windows

# Ubicación: dist/windows/BoardyJam-0.0.1.msi
```

**Distribución**:
- Microsoft Store
- Sitio web propio
- GitHub Releases

#### **macOS**

```bash
# Crear imagen de disco DMG
briefcase package macOS

# Ubicación: dist/macOS/BoardyJam-0.0.1.dmg
```

**Distribución**:
- Mac App Store
- Sitio web propio
- GitHub Releases

#### **Linux**

```bash
# Crear AppImage
briefcase package linux appimage

# Crear Flatpak
briefcase package linux flatpak
```

**Distribución**:
- Flathub
- Snap Store
- Distribuciones de Linux

### **📱 Distribución Mobile**

#### **Android**

```bash
# Crear APK para testing
briefcase package android

# Para Google Play Store, crear AAB
briefcase package android --target aab
```

#### **iOS**

```bash
# Crear IPA para App Store
briefcase package iOS
```

### **🌐 Distribución Web**

```bash
# Construir para producción
briefcase build web

# Desplegar en servidor web
# Los archivos están en: dist/web/
```

**Opciones de hosting**:
- GitHub Pages
- Netlify
- Vercel
- Servidor propio

---

## 🔧 **Configuración Avanzada**

### **Personalización de `pyproject.toml`**

```toml
[tool.briefcase.app.boardyjam]
formal_name = "BoardyJam"
description = "Aplicación de gestión de imágenes"
version = "0.0.1"
bundle = "com.tudominio"
url = "https://tudominio.com/boardyjam"
author = "Tu Nombre"
author_email = "tu@email.com"

# Icono de la aplicación
icon = "resources/icon"

# Splash screen
splash = "resources/splash"

# Permisos específicos por plataforma
[tool.briefcase.app.boardyjam.android]
permission.READ_EXTERNAL_STORAGE = "Leer archivos de imagen"
permission.WRITE_EXTERNAL_STORAGE = "Guardar imágenes procesadas"

[tool.briefcase.app.boardyjam.iOS]
info.NSPhotoLibraryUsageDescription = "Acceso a galería de fotos"
```

### **Recursos de la Aplicación**

```
resources/
├── icon.png          # Icono principal (512x512)
├── icon.ico          # Icono Windows
├── icon.icns         # Icono macOS
├── splash.png        # Splash screen
└── README            # Información adicional
```

### **Scripts de Construcción**

#### **`build.py`** (Automatización)

```python
#!/usr/bin/env python3
import subprocess
import sys
import os

def build_for_platform(platform):
    """Construye la aplicación para una plataforma específica."""
    commands = [
        f"briefcase create {platform}",
        f"briefcase build {platform}",
        f"briefcase package {platform}"
    ]
    
    for cmd in commands:
        print(f"Ejecutando: {cmd}")
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return False
    return True

if __name__ == "__main__":
    platform = sys.argv[1] if len(sys.argv) > 1 else "windows"
    success = build_for_platform(platform)
    sys.exit(0 if success else 1)
```

#### **Uso del script**

```bash
# Construir para Windows
python build.py windows

# Construir para macOS
python build.py macOS

# Construir para Linux
python build.py linux
```

---

## 🐛 **Solución de Problemas**

### **Problemas Comunes**

#### **Error: "No module named 'toga'"**

```bash
# Solución: Reinstalar dependencias
pip uninstall briefcase
pip install briefcase
```

#### **Error de permisos en macOS**

```bash
# Solución: Configurar permisos
sudo xattr -rd com.apple.quarantine /path/to/app
```

#### **Error de construcción en Android**

```bash
# Verificar Android SDK
echo $ANDROID_HOME
ls $ANDROID_HOME/platforms

# Instalar plataforma necesaria
sdkmanager "platforms;android-30"
```

#### **Error de memoria en construcción**

```bash
# Aumentar memoria para Java (Android)
export GRADLE_OPTS="-Xmx4g -XX:MaxPermSize=512m"
```

### **Logs de Depuración**

```bash
# Ejecutar con logs detallados
briefcase build windows --log

# Ver logs específicos
briefcase run windows --log-level DEBUG
```

### **Limpieza de Construcción**

```bash
# Limpiar archivos de construcción
rm -rf build/
rm -rf dist/

# Reconstruir desde cero
briefcase create
briefcase build
briefcase package
```

### **Verificación de Dependencias**

```bash
# Verificar instalación de Briefcase
briefcase --version

# Verificar configuración del proyecto
briefcase dev --help

# Verificar dependencias del sistema
python -c "import toga; print('Toga OK')"
```

---

## 📊 **Checklist de Despliegue**

### **Pre-despliegue**

- [ ] Código testeado y funcionando
- [ ] Versión actualizada en `pyproject.toml`
- [ ] Iconos y recursos preparados
- [ ] Documentación actualizada
- [ ] Tests pasando

### **Construcción**

- [ ] Entorno virtual activado
- [ ] Dependencias instaladas
- [ ] `briefcase create` exitoso
- [ ] `briefcase build` exitoso
- [ ] `briefcase package` exitoso

### **Testing**

- [ ] Aplicación ejecuta correctamente
- [ ] Funcionalidades principales funcionan
- [ ] Interfaz se ve correctamente
- [ ] Manejo de errores apropiado

### **Distribución**

- [ ] Archivos de distribución generados
- [ ] Tamaño de archivos razonable
- [ ] Metadatos correctos
- [ ] Firma de código (si aplica)

---

## 🔗 **Referencias Útiles**

- [📖 Documentación de Briefcase](https://briefcase.readthedocs.io/)
- [🐍 BeeWare Project](https://beeware.org/)
- [📱 Toga Framework](https://toga.readthedocs.io/)
- [🔧 Configuración de pyproject.toml](https://briefcase.readthedocs.io/en/latest/reference/configuration.html)

---

*Esta guía de despliegue te permite distribuir BoardyJam en todas las plataformas soportadas. Para más detalles técnicos, consulta la [Documentación Técnica](TECHNICAL.md).*
