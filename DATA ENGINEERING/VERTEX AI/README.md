# APUNTES CLASE VERTEX AI (21/01/2023)

- Es una plataforma que reúne dos productos de Google Cloud Platform (GCP)
    - Auto ML
    - AI Platform 

- Además nos proporciona herramientas que cubren todo el flujo de trabajo. 
    - Notebooks
    - Datasets
        - Datos tabulados
        - Imágenes/Video
        - Texto
    - Models
        - Mediante AutoML o AI Platform
    - Deploy  



## DATASET DE DATOS TABULADOS

- Para poder entrenar un modelo, debemos tener un mínimo de datos. Al menos 1000 filas para Tabular Data. 100 imágenes por clase para Vision AI. 

- Para poder entrenar el modelo hay que dividir el dataset. Una parte de entrenamiento y otra parte con datos de test. Si utilizamos todo el dataset para entrenar, cuando hagamos el test, el modelo habrá memorizado el dato. 


