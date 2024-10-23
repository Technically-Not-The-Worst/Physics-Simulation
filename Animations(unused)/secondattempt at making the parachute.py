from manim import *

class ParachuteWithTheHoles(Scene):
    def construct(self):
        # Create the parachute as an upside-down semi-circle (inflated state)
        parachute = Arc(radius=1, start_angle=0, angle=PI, color=BLUE)  # Flipped arc
        cut_out = Arc(radius=1, start_angle=PI/2, angle=-PI/3, color=BLACK)
        cut_out1 = Arc(radius=1, start_angle=PI/2, angle=PI/3, color=BLACK)
        cut_out_back = Arc(radius=1, start_angle=PI/6, angle=PI/3, color=BLUE)
        cut_out1_back = Arc(radius=1, start_angle=5*PI/6, angle=-PI/3, color=BLUE)
        cut_out2 = Arc(radius=1, start_angle=PI/2, angle=-PI/6, color=BLACK)
        cut_out3 = Arc(radius=1, start_angle=PI/2, angle=PI/6, color=BLACK)
        
        # Create suspension cords (lines connecting the parachute to the weight)
        cords = VGroup(
            Line(parachute.get_start(), DOWN * 1, color=WHITE),  # Connected from parachute to weight
            Line(parachute.get_end(), DOWN * 1, color=WHITE)
        )
        
        # Create the weight (a simple box or circle)
        weight = Square(side_length=0.5, color=RED).move_to(DOWN * 1.25)

        # Group parachute, cords, and weight together
        parachute_system = VGroup(parachute, cords, weight, cut_out, cut_out1, cut_out_back, cut_out1_back,cut_out2,cut_out3 )

        # Initial position of the parachute system (start from higher up in the frame)
        parachute_system.shift(UP * 1)

        # Add parachute system to the scene with the cords already connecting the weight
        self.play(Create(parachute), Create(cords), Create(weight), run_time=3)
        self.wait(0.5)
        self.play(Create(cut_out),  Create(cut_out1), run_time=1.5 )
        self.play(Create(cut_out_back), Create(cut_out1_back), run_time=1.5 )
        self.play(Create(cut_out3), Create(cut_out2), run_time=0.75 )
        



        # Wait at the end for a moment

