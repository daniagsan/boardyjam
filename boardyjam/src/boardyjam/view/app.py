import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from boardyjam.controller.image_controller import ImageController


class boardyjam(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(direction=COLUMN)

        name_label = toga.Label(
            "Your name: BoardyJam ",
            margin=(0, 5),
        )

        # Inicializar controlador
        self.image_controller = ImageController()
        self.image_controller.add_observer(self)
        
        self.name_input = toga.TextInput(flex=1)
        self.status_label = toga.Label(
            "No hay imagen seleccionada",
            margin=(5, 0)
        )
        
        # Componente para mostrar la imagen
        self.image_view = toga.ImageView(
            style=Pack(width=300, height=200, margin=10)
        )

        name_box = toga.Box(direction=ROW, margin=5)
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Elegir imagen",
            on_press=self.select_image,
            margin=5,
        )

        main_box.add(name_box)
        main_box.add(button)
        main_box.add(self.status_label)
        main_box.add(self.image_view)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def select_image(self, widget):
        """Maneja el evento de selección de imagen desde la UI"""
        try:
            file_path = await self.main_window.dialog(
                toga.OpenFileDialog(
                    title="Selecciona una imagen",
                    initial_directory=".",
                    file_types=["png", "jpg", "jpeg", "bmp", "gif"]
                )
            )
            
            # Delegar la lógica al controlador
            if file_path:
                self.image_controller.select_image(str(file_path))
        except Exception as e:
            self.status_label.text = f"Error al abrir diálogo: {str(e)}"
    
    def on_image_event(self, event_type, data=None):
        """Observador para eventos del controlador de imágenes"""
        if event_type == 'image_selected':
            filename = data.split('\\')[-1] if '\\' in data else data.split('/')[-1]
            self.status_label.text = f"Imagen seleccionada: {filename}"
            print(f"Imagen seleccionada: {data}")
        elif event_type == 'image_display_ready':
            # Mostrar la imagen en el ImageView
            try:
                self.image_view.image = data
                self.status_label.text = "Imagen cargada correctamente"
            except Exception as e:
                self.status_label.text = f"Error al mostrar imagen: {str(e)}"
        elif event_type == 'image_error':
            self.status_label.text = f"Error: {data}"
            self.image_view.image = None
            print(f"Error al seleccionar imagen: {data}")        

def main():
    return boardyjam()
