from manim import *

class test(Scene):
    def construct(self):
        #create
        circle = Circle()
        square = Square()
        
        text = Text("Meow Meow Meow", font_size=73)
        text.to_edge(UP)
        
        self.add(circle)

        self.play(
            Write(text),
            Transform(circle, square)
        )