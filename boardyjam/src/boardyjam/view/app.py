import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from boardyjam.model.image_model import ImageModel


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

        self.image_model = ImageModel()
        self.name_input = toga.TextInput(flex=1)

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

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def select_image(self, widget):
        file_path = self.main_window.open_file_dialog(
            title="Selecciona una imagen",
            initial_directory=".",
            file_types=[("Imagen", "*.png;*.jpg;*.jpeg;*.bmp")],
        )
        if file_path:
            self.image_model.set_image(file_path)
            print(f"Imagen seleccionada:{file_path}")        

def main():
    return boardyjam()
