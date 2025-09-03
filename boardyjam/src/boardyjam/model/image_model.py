class ImageModel:
    def __init__(self):
        self.image_path = None

    def set_image(self, path):
        self.image_path = path 

    def get_image(self):
        return self.image_path