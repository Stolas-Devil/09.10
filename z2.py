class TriangleChecker:
    """правельный треугольник"""
    def __init__(self, a, b, c):
        if a > 0 and b > 0 and c > 0:
            self.z = a, b, c 
        else:
            self.z = None
        if a + b < c:
            self.z = self.x
        else:
            print("Жаль, но из этого треугольник не сделать.")     
    

    def is_triangle():
        if self.z:
            print("Ура, можно построить треугольник!")
        else:
            print("С отрицательными числами ничего не выйдет!")



