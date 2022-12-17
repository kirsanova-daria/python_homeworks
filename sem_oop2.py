class Color:
    def __init__(self, c1, c2, c3) -> None:
        self.red = c1
        self.green = c2
        self.blue = c3
        self.colors = (c1, c2, c3)

    def __repr__(self) -> str:
        END = '\033[0'
        START = '\033[1;38;2'
        MOD = 'm'
        return f'{START};{self.red};{self.green};{self.blue}{MOD}●{END}{MOD}'

    def __eq__(self, other):
        return self.colors == other.colors

    def __add__(self, other):
        colors_sum = []
        for i, color in enumerate(self.colors):
            colors_sum.append(min(color+other.colors[i], 255))
        return type(self)(*colors_sum)

    def __hash__(self):
        return hash(self.colors)

    def __mul__(self, other):
        colors_new = []
        cl = -256*(1-other)
        f = 259*(cl+255)/(255*(259-cl))
        for color in self.colors:
            colors_new.append(int(f*(color-128)+128))
        return Color(*colors_new)

    def __rmul__(self, other):
        return self * other


if __name__ == '__main__':
    red = Color(255, 0, 0)
    print(red)
    print(red * 0.5)
    print(0.5 * red)
    red1 = 0.8 * red
    print(red1.colors)
