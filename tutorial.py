from manimlib import *

class HelloWorld(InteractiveScene):
    def construct(self):
        #add some simple geometry
        circle = Circle()
        square = Square()
        self.add(circle)
        self.add(square)
        
        square.to_edge(UP)
    
class OpenGLIntro(Scene):
    def construct(self):
        hello_world = Text("Hello, World!").scale(3)
        self.play(Write(hello_world))
        self.play(
            self.camera.animate.set_euler_angles(
                theta=-10 * DEGREES,
                phi=50 * DEGREES
            )
        )
        self.play(FadeOut(hello_world))

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()