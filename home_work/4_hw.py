# ----------- Задача 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width;
        self.height = height;

    def perimeterRectangle(self):
        print((self.width*self.height)*2)

    def areaRectangle(self):
        print(self.width*self.height)

numOne = 3
numTwo = 6

formulaPerimeter = Rectangle(numOne,numTwo)
formulaPerimeter.perimeterRectangle()

formulaArea = Rectangle(numOne,numTwo)
formulaArea.areaRectangle()

# ----------- Задача 2
class Math:

    def __init__(self, a, b):
        self.a = a;
        self.b = b;

    def subtraction(self):
        print(self.a - self.b)

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)


numOne = 13
numTwo = 7

mathematical = Math(numOne, numTwo)
mathematical.subtraction()
mathematical.addition()
mathematical.multiplication()
mathematical.division()

# ----------- Задача 3

class Button:
    def __init__(self, text, typ, lok=None):
        self.text = text;
        self.typ = typ;
        self.lok = lok

    def click(self):
        print("Нажал на кнопку", self.text)

TextBox = Button("Text Box", "Button")
print(TextBox.text)
TextBox.click()

CheckBox = Button("Check Box", "Button")
print(CheckBox.text)
CheckBox.click()

RadioButton = Button("Radio Button","Button")
print(RadioButton.text)
RadioButton.click()

WebTables = Button("Web Tables", "Button")
print(WebTables.text)
WebTables.click()

Buttons = Button("Buttons", "Button")
print(Buttons.text)
Buttons.click()

Links = Button("Links", "Button")
print(Links.text)
Links.click()

BrokenLinkImages = Button( "Broken link - image", "Button")
print(BrokenLinkImages.text)
BrokenLinkImages.click()

UploadAndDownload = Button("Upload and download", "Button")
print(UploadAndDownload.text)
UploadAndDownload.click()