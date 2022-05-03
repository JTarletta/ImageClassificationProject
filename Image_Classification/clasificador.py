from email.mime import image
import torch
from torchvision import models, transforms #Modelos, y Transformaciones para ajustal la imagen 
from PIL import Image

#Cargamos el diccionario de Etiquetas de ImageNet
with open("resources\imageNet_index.txt") as f:
    idx2label = eval(f.read())
#print(idx2label, idx2label.get(916))

#Imagen a clasificar
imagen = Image.open("static\img\prueba.jpeg")
#imagen.show()

def clasificador(image_path=imagen):
    # print(dir(models)) #Modelos de clasificación de imágenes

    imagen = Image.open(image_path)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    #print(device) #Computo utilizado

    #Seleccionamos el modelo a utilizar
    alexnet = models.alexnet(pretrained=True)
    #print(alexnet)


    #Transformador para ajustar la imagen al número de neuronas de la red
    preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )])
    #print(preprocess)

    
    img_t = preprocess(imagen)                # preprocesar imagen
    batch_t = torch.unsqueeze(img_t, 0)    # convertir a tensor de 1-dimension
    alexnet.eval()          # entrar en modo evaluación
    out = alexnet(batch_t)  # pasar la imagen ya preprocesada y ajustada

    _, indices = torch.sort(out, descending=True)
    
    #print(indices[0][:3]) #3 Clasificaciones de la red según los Indices de ImageNet
    clave = indices[0][:1].item()

    clasification = idx2label.get(clave)

    return clasification