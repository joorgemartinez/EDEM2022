# Apuntes APACHE SPARK
Clase 09/12/2022

## BEFORE SPARK

Antes de la computación en paralelo, el objetivo era tener un a máquina más potente. Tenía sus limitaciones:

- Escalabilidad
- Costes

### HDFS

Hadoop Distributed File System. Es el encargado de almacenar los datos en el cluster. 

### MapReduce

---

## APACHE SPARK

### RDD 
- Son inmutables. No se pueden cambiar. Cualquier transformación en un RDD dará lugar a otro RDD nuevo. (Resilientes)
- Facilita dos tipos de operaciones:
    - Transformación
    - Acción