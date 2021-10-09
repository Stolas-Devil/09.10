class Soda:
    """Газировка"""
    # а это добавка
    def __init__(self, a):
        if isinstance(a, str):
            self.a = a
        else:
            self.a = None    
 
    def show_my_drink():
        if self.a:
            print("обычная газировка ,{A}")
        else:
            print("обычная газировка")



