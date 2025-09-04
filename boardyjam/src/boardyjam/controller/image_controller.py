from boardyjam.model.image_model import ImageModel


class ImageController:
    def __init__(self):
        self.image_model = ImageModel()
        self._observers = []
    
    def add_observer(self, observer):
        """Añade un observador para notificar cambios"""
        self._observers.append(observer)
    
    def remove_observer(self, observer):
        """Remueve un observador"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def _notify_observers(self, event_type, data=None):
        """Notifica a todos los observadores sobre cambios"""
        for observer in self._observers:
            if hasattr(observer, 'on_image_event'):
                observer.on_image_event(event_type, data)
    
    def select_image(self, file_path):
        """Maneja la selección de una imagen"""
        if file_path:
            try:
                # Validar formato de archivo
                if not self.validate_image_file(file_path):
                    raise ValueError("Formato de archivo no soportado")
                
                # Establecer imagen en el modelo
                self.image_model.set_image(file_path)
                self._notify_observers('image_selected', file_path)
                
                # Cargar imagen para visualización
                self.load_image_for_display()
                return True
                
            except Exception as e:
                self._notify_observers('image_error', str(e))
                return False
        return False
    
    def load_image_for_display(self):
        """Carga la imagen para mostrar en la interfaz"""
        try:
            success = self.image_model.load_image_data()
            if success:
                image_data = self.image_model.get_image_data()
                self._notify_observers('image_display_ready', image_data)
            else:
                self._notify_observers('image_error', "No se pudo cargar la imagen")
        except Exception as e:
            self._notify_observers('image_error', f"Error al cargar imagen: {str(e)}")
    
    def get_current_image(self):
        """Obtiene la imagen actual"""
        return self.image_model.get_image()
    
    def validate_image_file(self, file_path):
        """Valida si el archivo es una imagen válida"""
        if not file_path:
            return False
        
        valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
        return any(file_path.lower().endswith(ext) for ext in valid_extensions)