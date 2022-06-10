import math

from fastapi import FastAPI
import uvicorn
import numpy

app = FastAPI()


@app.get("/solution")
def solution(a: int, b: int, c: int):
    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form))

    if a == 0:
        return "Incorrect quadratic equation, required: a != 0"

    if dis_form > 0:
        root1 = ((-b + sqrt_val) / (2 * a))
        root2 = ((-b - sqrt_val) / (2 * a))
        return {'root1': root1, 'root2': root2}
    elif dis_form == 0:
        root = -b / (2 * a)
        return root
    else:
        return f'Discriminant < 0, no real roots for a: {a}, b: {b}, c: {c}'


@app.get("/sample_colour")
def solution():
    colour = numpy.random.choice(['blue', 'green', 'red'], p=[0.7, 0.2, 0.1])
    return colour


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


