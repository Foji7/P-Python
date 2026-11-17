"""Algoritmo 2.4. Devuelve (p, historia), con historia = [p0, p1, p2, ..., p]."""
def secante(f, p0, p1, TOL=1e-6, N0=50):
    historia = [p0, p1]
    i = 2
    q0, q1 = f(p0), f(p1)
    while i <= N0:
        if q1 == q0:
            raise ZeroDivisionError(f"q1 = q0 en p0 = {p0}: La secante es horizontal")
        p = p1 - q1 * ((p1 - p0) / (q1 - q0))
        historia.append(p)
        if abs(p - p1) < TOL:
            return p, historia
        i += 1
        p0, q0 = p1, q1
        p1, q1 = p, f(p) 
    raise RuntimeError(f"El método fracasó después de {N0} iteraciones")

llamadas = []            # cada evaluación de f agrega aquí su x

def f(x):
    llamadas.append(x)
    return x ** 3 + 4 * x ** 2 - 10

llamadas.clear()         # vacíe la lista antes de cada prueba
p, historia = secante(f, 1.0, 2.0, TOL=1e-6)
print(p, len(historia) - 2, len(llamadas))
print(historia)