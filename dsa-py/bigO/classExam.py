class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color



cookie1 = Cookie("green")
cookie2 = Cookie("blue")

print('Cookie one is', cookie1.get_color())
print('Cookie two is', cookie2.get_color())

print('-----------------------------------------------------')

cookie2.set_color('yellow')

print('Cookie one is still', cookie1.get_color())
print('Cookie two now is', cookie2.get_color())
