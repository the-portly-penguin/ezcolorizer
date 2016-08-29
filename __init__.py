__author__ = 'The Portly Penguin'
__version__ = '2.0'
__date__ = '08/29/2016'

class Colorizer():
    '''
    Provides a simple way to color scripts and output that would otherwise be plain and boring. 
    Uses ANSI escape characters.
    '''

    def __init__(self):
        # Colors and the corresponding number to append.
        self.colors = {
            'red':'31',
            'green':'32',
            'yellow':'33',
            'blue':'34',
            'magenta':'35',
            'cyan':'36',
            'white':'37'
        }
        # Styles and the corresponding number to append.
        self.styles = {
            'normal': '0',
            'bold':'1',
            'underline': '4'
        }

    def ColorString(self, string, color='white', style='normal'):
        '''
        Appends the escape characters and colors and styles the string.
        '''
        try:
            attrs = []
            attrs.append(self.colors[color])
            attrs.append(self.styles[style])
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attrs), string)
        except:
            print('Did you provide a valid color or style name?')

    def RedBold(self, string):
        return self.ColorString(string, "red", "bold" )

    def RedUnderline(self, string):
        return self.ColorString(string, "red", "underline")

    def Red(self, string):
        return self.ColorString(string, "red", "normal")

    def GreenBold(self, string):
        return self.ColorString(string, "green", "bold")

    def GreenUnderline(self, string):
        return self.ColorString(string, "green", "underline")

    def Green(self, string):
        return self.ColorString(string, "green", "normal")

    def YellowBold(self, string):
        return self.ColorString(string, "yellow", "bold")

    def YellowUnderline(self, string):
        return self.ColorString(string, "yellow", "underline")

    def Yellow(self, string):
        return self.ColorString(string, "yellow", "normal")

    def BlueBold(self, string):
        return self.ColorString(string, "blue", "bold")

    def BlueUnderline(self, string):
        return self.ColorString(string, "blue", "underline")

    def Blue(self, string):
        return self.ColorString(string, "blue", "normal")

    def MagentaBold(self, string):
        return self.ColorString(string, "magenta", "bold")

    def MagentaUnderline(self, string):
        return self.ColorString(string, "magenta", "underline")

    def Magenta(self, string):
        return self.ColorString(string, "magenta", "normal")

    def CyanBold(self, string):
        return self.ColorString(string, "cyan", "bold")

    def CyanUnderline(self, string):
        return self.ColorString(string, "cyan", "underline")

    def Cyan(self, string):
        return self.ColorString(string, "cyan", "normal")

    def WhiteBold(self, string):
        return self.ColorString(string, "white", "bold")

    def WhiteUnderline(self, string):
        return self.ColorString(string, "white", "underline")