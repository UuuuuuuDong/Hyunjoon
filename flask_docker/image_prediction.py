from torchvision import models
import json

model = models.densenet121(pretrained=True)

model.eval()

imagenet_class_index = json.load(open('../path/to/imagenet_class_index.json'))

def get_prediction(image_bytes):
	tensor = transform_image(image_bytes = image_bytes)
	outputs = model.forward(tensor)
	_, y_hat = outputs.max(1)
	predicted_idx = str(y_hat.item())

	return imagenet_class_index[predicted_idx]