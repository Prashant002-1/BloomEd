# Five shapes at four corners and one at edge 
# Name transform into shape sequentially 
from manimlib.imports import *

class WriteName(Scene):
    def construct(self):
        SquareText = TextMobject(
            "Square",
            tex_to_color_map={"Square": RED}
        )
        RectangleText = TextMobject(
            "Rectangle",
            tex_to_color_map={"Rectablge": BLUE}
        )
        TriangleText = TextMobject(
            "Triangle",
            tex_to_color_map={"Triangle": YELLOW}
        )
        CircleText = TextMobject(
            "Circle",
            tex_to_color_map={"Circle": GREEN}
        )
        AnnulusText = TextMobject(
            "Annulus",
            tex_to_color_map={"Annulus": PURPLE}
        )
        SquareText.to_corner(UR)
        RectangleText.to_corner(DR)
        TriangleText.to_corner(DL)
        CircleText.to_corner(UL)
        AnnulusText.to_edge(UP)
        self.add(SquareText)
        self.add(RectangleText)
        self.add(TriangleText)
        self.add(CircleText)
        self.add(AnnulusText)
        self.wait(4)
        self.remove(CircleText)
        self.remove(RectangleText)
        self.remove(AnnulusText)
        self.remove(TriangleText)
        vector = np.array([0,0,0])
        SquareText.move_to(vector)
        self.play(GrowFromCenter(SquareText))
        self.wait(2)

class DrawSquare(Scene):
    def construct(self):
        square = Square()
        SqText = TextMobject("The formula and shape")
        self.add(SqText)
        self.wait(1)
        formulasq = TexMobject("Length^2")
        formulasq.shift(2*DOWN)
        self.play(Transform(SqText,formulasq))
        self.play(ShowCreation(square))
        self.wait(4)
        self.remove(formulasq)
        self.remove(square)

class DrawCircle(Scene):
    def construct(self):
        circle = Circle()
        Crtext = TextMobject("Now, the formula and shape for circle")
        self.play(Write(Crtext))
        self.wait(1)
        formulacr = TexMobject("\\pi *radius^2")
        formulacr.shift(2*DOWN)
        self.play(Transform(Crtext, formulacr))
        self.play(ShowCreation(circle))
        self.wait(4)
        self.remove(formulacr)
        self.remove(circle)

class DrawTriangle(Scene):
    def construct(self):
        triangle = Triangle()
        Trtext = TextMobject("Now, the formula and shape for triangle")
        self.play(Write(Trtext))
        self.wait(1)
        formulatr = TexMobject(
            "{1 \\over 2} base*height",
        )
        formulatr.shift(2*DOWN)
        self.play(Transform(Trtext, formulatr))
        self.play(ShowCreation(triangle))
        self.wait(4)
        self.remove(formulatr)
        self.remove(triangle)

class DrawReactangle(Scene):
    def construct(self):
        rectangle = Rectangle()
        Rttext = TextMobject("Now, the formula and shape for rectangle")
        self.play(Write(Rttext))
        self.wait(1)
        formulart = TexMobject(
            "Length * Width",
        )
        formulart.shift(2*DOWN)
        self.play(Transform(Rttext, formulart))
        self.play(ShowCreation(rectangle))
        self.wait(4)
        self.remove(formulart)
        self.remove(rectangle)

class DrawAnnulus(Scene):
    def construct(self):
        annulus = Annulus()
        Antext = TextMobject("Now, the formula and shape for annulus")
        self.play(Write(Antext))
        self.wait(1)
        formulaAn = TexMobject(
            "\\pi (R^2 - r^2)",
        )
        formulaAn.shift(3*DOWN)
        self.play(Transform(Antext, formulaAn))
        self.play(ShowCreation(annulus))
        self.wait(4)
        self.remove(formulaAn)
        self.remove(annulus)







        


    
        