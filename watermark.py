from PIL import Image


class WaterMark:
    def __init__(self):
        self.image_path = None
        self.watermark_path = None

    def load_image(self, image_path):
        self.image_path = image_path
        image = Image.open(self.image_path)
        return image

    def load_watermark(self, watermark_path):
        self.watermark_path = watermark_path
        watermark = Image.open(self.watermark_path)
        return watermark

    def add_watermark_on_image(self, image_path, watermark_path):
        current_image = self.load_image(image_path)
        current_watermark = self.load_watermark(watermark_path)

        watermark_width = int(current_image.size[0] * 0.2)
        watermark_height = int(current_image.size[1] * 0.2)
        current_watermark = current_watermark.resize((watermark_width, watermark_height))

        position = (current_image.width - current_watermark.width - 10,
                    current_image.height - current_watermark.height - 10)

        current_image.paste(current_watermark, position, current_watermark)
        current_image.show()

        current_image.save(fp=f"./outputs/output-{image_path.name}")
