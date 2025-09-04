import os
from pathlib import Path


class ImageModel:
    def __init__(self):
        self.image_path = None
        self.image_data = None
        self.is_loaded = False

    def set_image(self, path):
        """Establece la ruta de la imagen"""
        self.image_path = path
        self.is_loaded = False
        self.image_data = None

    def get_image_path(self):
        """Obtiene la ruta de la imagen"""
        return self.image_path
    
    def load_image_data(self):
        """Carga los datos de la imagen para visualización"""
        if not self.image_path:
            return False
            
        try:
            # Verificar que el archivo existe
            if not os.path.exists(self.image_path):
                raise FileNotFoundError(f"Archivo no encontrado: {self.image_path}")
            
            # Verificar que es un archivo válido
            path_obj = Path(self.image_path)
            if not path_obj.is_file():
                raise ValueError(f"La ruta no es un archivo válido: {self.image_path}")
            
            # Para Toga, la imagen se carga directamente desde la ruta
            self.image_data = self.image_path
            self.is_loaded = True
            return True
            
        except Exception as e:
            self.is_loaded = False
            self.image_data = None
            raise e
    
    def get_image_data(self):
        """Obtiene los datos de imagen listos para mostrar"""
        return self.image_data if self.is_loaded else None
    
    def is_image_loaded(self):
        """Verifica si la imagen está cargada"""
        return self.is_loaded
    
    def clear_image(self):
        """Limpia los datos de imagen"""
        self.image_path = None
        self.image_data = None
        self.is_loaded = False