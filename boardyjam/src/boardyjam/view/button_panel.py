import toga
from toga.style import Pack

class ButtonPanel(self, on_select_image):
    self.select_image_button = toga.Button(
        "Elegir imagen",
        on_press=on_select_image,
        style=Pack(padding=5)
    )