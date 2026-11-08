import numpy as np

def calculate(list):
    # Validar que la lista tenga exactamente 9 elementos
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertir la lista en una matriz de 3x3
    matrix = np.array(list).reshape(3, 3)
    
    # Calcular las métricas convirtiendo los resultados de NumPy a listas nativas de Python (.tolist())
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), # a lo largo del eje 0 (columnas)
            matrix.mean(axis=1).tolist(), # a lo largo del eje 1 (filas)
            matrix.mean().tolist()        # matriz aplanada
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }

    return calculations
