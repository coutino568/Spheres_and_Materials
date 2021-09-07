


class RayTracer(object):
    def __init__(self,width , height):
        self.black = color(0,0,0)
        self.bgColor = color(0,0,0)
        self.viewportBgColor = color(1,1,1)
        self.mainColor = color(0,0,0)
        self.glCreateWindow( width, height)
        self.glViewPort(0,0,self.width,self.height)
        self.path =[]