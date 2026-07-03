# Clasificación de lesiones cutáneas mediante deep learning: análisis del transfer learning y de la robustez del modelo en escenarios con datos limitados

Repositorio asociado a mi Trabajo Fin de Máster (TFM), centrado en el estudio del impacto del **Transfer Learning** en la clasificación automática de imágenes de lesiones cutáneas mediante técnicas de Deep Learning.

El proyecto compara diferentes estrategias de entrenamiento, desde una CNN diseñada desde cero hasta modelos preentrenados basados en EfficientNet-B0, analizando su rendimiento, capacidad de generalización e interpretabilidad.

---

## Objetivos

Los principales objetivos del proyecto son:

- Desarrollar un modelo baseline de clasificación de lesiones cutáneas.
- Evaluar el efecto del Transfer Learning frente al entrenamiento desde cero.
- Comparar distintas estrategias de fine-tuning sobre EfficientNet-B0.
- Analizar el comportamiento del modelo en diferentes tonos de piel.
- Analizar el impacto del tamaño del conjunto de entrenamiento.
- Estudiar la interpretabilidad de los modelos mediante Grad-CAM.

---

## Dataset

El proyecto utiliza el dataset SCIN, disponible en Hugging Face.

El notebook descarga automáticamente el dataset, por lo que no es necesario descargarlo manualmente.

---

## Estructura del repositorio

```text
.
├── models/                    # Checkpoints de los modelos entrenados
├── results/                   # Resultados de los experimentos
├── scripts/
│   └── download_models.py     # Descarga automática de los modelos
├── requirements.txt
├── notebook.ipynb
└── README.md
```

---

## Ejecución

El notebook puede ejecutarse de principio a fin sin necesidad de volver a entrenar los modelos, y está diseñado para su uso en Google Colab.

Se incluyen en las primeras celdas las siguientes instalaciones: 

Clonar el repositorio:

```bash
git clone https://github.com/rainbownash/transfer-learning-skin-lesion-classification.git
cd transfer-learning-skin-lesion-classification
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Descargar los modelos (se almacenarán en la carpeta `models/`):

```bash
python scripts/download_models.py
```
Los modelos entrenados no se incluyen directamente en el repositorio debido a su tamaño.

Las celdas de entrenamiento se conservan comentadas para documentar la configuración experimental utilizada en el TFM.

---

## Experimentos incluidos

- CNN baseline con 3 bloques convolucionales + class weights
- CNN baseline con 3 bloques convolucionales sin class weights
- CNN baseline con 4 bloques convolucionales + class weights
- EfficientNet-B0 con Feature Extraction
- EfficientNet-B0 con Fine-Tuning parcial
- EfficientNet-B0 con Fine-Tuning completo
- Análisis por tono de piel según la escala Fitzpatrick
- Análisis del tamaño del conjunto de entrenamiento
- Análisis de interpretabilidad mediante Grad-CAM

---

## Reproducibilidad

Con el objetivo de facilitar la reproducción de los resultados, el repositorio incluye:

- Configuración determinista mediante semillas.
- Checkpoints de todos los modelos entrenados.
- Historiales completos de entrenamiento.
- Resultados agregados de los experimentos.

Esto permite reproducir todos los análisis del notebook sin necesidad de reentrenar los modelos.

---

## Autora

Estudio realizado por Anastasie Wagenheim en su Trabajo Fin de Máster (Máster en Deep Learning, Universidad Politécnica de Madrid, 2026).

---

## Licencia

Repositorio publicado con fines académicos y de investigación.
