class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{0:02x}".format(self.red, self.green, self.green)
        else:
            raise AttributeError

    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.b = val[2]
        super().__setattr__(attr, val)

     # برای نمایش داراییهای یک کلا س به صورت رشته
    def __dir__(self):
        return ("red",  "green", "blue", "rgbcolor", "hexcolor")


def main():

    c1 = myColor()
    print(c1.rgbcolor)
    print(c1.hexcolor)

    c1.rgbcolor = (125, 200, 86)

    print(c1.rgbcolor)
    print(c1.hexcolor)

    print(c1.red)

    print(dir(c1))


if __name__ == '__main__':
    main()
