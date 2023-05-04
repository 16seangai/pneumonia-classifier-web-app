import io

from model_loader import load_model
import torchvision.transforms as transforms
from PIL import Image

model = load_model()

def transform_image(image_bytes):
    resize_and_normalize = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize((256, 256)),
        transforms.ToTensor()
        ])
    image = Image.open(io.BytesIO(image_bytes))
    return resize_and_normalize(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes)
    output = model(tensor)
    class_name = 'normal' if output.item() <= 0.5 else 'pneumonia'
    confidence = output.item() if class_name == 'pneumonia' else 1.0 - output.item()
    return class_name, confidence