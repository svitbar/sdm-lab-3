from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/product')
def culc_product() -> dict:
    import numpy as np

    matrix_a = np.random.rand(10,10)
    matrix_b = np.random.rand(10,10)

    product = np.matmul(matrix_a, matrix_b)

    return {
        'matrix_a': matrix_a.tolist(),
        'matrix_b': matrix_b.tolist(),
        'product': product.tolist()
    }
