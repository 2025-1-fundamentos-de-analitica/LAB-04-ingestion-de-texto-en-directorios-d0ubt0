# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import zipfile
import pandas as pd

def listar_carpetas(ruta):
    carpetas = [nombre for nombre in os.listdir(ruta)
                if os.path.isdir(os.path.join(ruta, nombre))]   
    return carpetas

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    with zipfile.ZipFile('files/input.zip' , 'r') as zip:
        zip.extractall()

    train_df = pd.DataFrame(columns=['phrase', 'target'])
    test_df = pd.DataFrame(columns=['phrase', 'target'])

    for primera_carpeta in listar_carpetas('input'):
        for segunda_carpeta in listar_carpetas(f'input/{primera_carpeta}'):
            for archivo in os.listdir(f'input/{primera_carpeta}/{segunda_carpeta}'):
                with open(f'input/{primera_carpeta}/{segunda_carpeta}/{archivo}', 'r') as txt:
                        for line in txt:
                            line = line.strip()
                            aux_df = pd.DataFrame([{'phrase': line,'target': segunda_carpeta}])
                            if primera_carpeta == 'train':
                                train_df = pd.concat([train_df, aux_df], ignore_index=True)
                            else:    
                                test_df = pd.concat([test_df, aux_df], ignore_index=True)
                    
    if not os.path.exists('files/output'):
        os.mkdir('files/output')         

    train_df.to_csv('files/output/train_dataset.csv')
    test_df.to_csv('files/output/test_dataset.csv')

pregunta_01()