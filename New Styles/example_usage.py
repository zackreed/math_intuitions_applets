"""
Example: Using the Unified Style Library
========================================

This file demonstrates how to use the unified color schemes and animation
timing functions in a Manim scene.
"""

from manimlib import *
from unified_color_schemes import get_scheme
from unified_animation_timing import (
    smooth, rush_into, rush_from, there_and_back,
    ease_in_back, ease_out_back
)


class UnifiedStyleExample(Scene):
    """
    Example scene demonstrating the unified style library.
    Shows how to use color schemes and timing functions consistently.
    """
    
    def construct(self):
        # Choose a color scheme for this scene
        scheme = get_scheme("deep_jewel_tones")
        
        # Add background with scheme color
        background = Rectangle(
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT,
            color=scheme.hex("background"),
            fill_opacity=1,
            stroke_width=0
        )
        self.add(background)
        
        # Create title with scheme colors
        title = Text(
            "Unified Style Library Demo",
            font_size=60,
            color=scheme.hex("text")
        ).to_edge(UP)
        
        # Animate title appearing with smooth easing
        self.play(
            FadeIn(title),
            rate_func=smooth,
            run_time=1.0
        )
        self.wait(0.5)
        
        # Create geometric objects with scheme colors
        circle = Circle(
            radius=1.5,
            stroke_color=scheme.hex("highlight"),
            stroke_width=4,
            fill_color=scheme.hex("highlight"),
            fill_opacity=0.3
        )
        
        square = Square(
            side_length=2.5,
            stroke_color=scheme.hex("accent"),
            stroke_width=4,
            fill_color=scheme.hex("accent"),
            fill_opacity=0.3
        )
        
        # Position them
        circle.shift(LEFT * 3)
        square.shift(RIGHT * 3)
        
        # Animate circle appearing with rush_into
        self.play(
            FadeIn(circle),
            rate_func=rush_into,
            run_time=0.8
        )
        
        # Animate square appearing with ease_in_back (bouncy)
        self.play(
            FadeIn(square),
            rate_func=ease_in_back,
            run_time=1.0
        )
        
        self.wait(0.5)
        
        # Create a dot that will move
        dot = Dot(
            point=circle.get_center(),
            color=scheme.hex("dot"),
            radius=0.15
        )
        
        self.play(
            FadeIn(dot),
            rate_func=smooth,
            run_time=0.5
        )
        
        # Animate dot moving from circle to square with smooth easing
        self.play(
            dot.animate.move_to(square.get_center()),
            rate_func=smooth,
            run_time=2.0
        )
        
        self.wait(0.5)
        
        # Create equation with color-coded parts
        equation = Tex(
            "f", "(", "x", ")", "=", "x", "^2",
            font_size=72
        )
        equation.move_to(ORIGIN + DOWN * 2)
        
        # Color different parts
        equation[0].set_color(scheme.hex("accent"))      # f
        equation[2].set_color(scheme.hex("time"))        # x
        equation[5:].set_color(scheme.hex("displacement"))  # x^2
        
        # Write equation
        self.play(
            Write(equation),
            rate_func=smooth,
            run_time=2.0
        )
        
        self.wait(0.5)
        
        # Emphasize the equation with there_and_back
        self.play(
            Indicate(equation),
            rate_func=there_and_back,
            run_time=1.0
        )
        
        self.wait(0.5)
        
        # Transform circle to match square's color
        self.play(
            circle.animate.set_stroke(color=scheme.hex("accent")),
            circle.animate.set_fill(
                color=scheme.hex("accent"),
                opacity=0.3
            ),
            rate_func=smooth,
            run_time=1.5
        )
        
        self.wait(0.5)
        
        # Fade everything out smoothly
        self.play(
            FadeOut(VGroup(circle, square, dot, equation, title)),
            rate_func=rush_from,
            run_time=1.2
        )
        
        self.wait(0.5)


class ColorSchemeShowcase(Scene):
    """
    Display all available color schemes in a grid.
    Useful for choosing which scheme to use for a project.
    """
    
    def construct(self):
        from unified_color_schemes import list_schemes
        
        title = Text(
            "Available Color Schemes",
            font_size=48
        ).to_edge(UP)
        
        self.add(title)
        
        # Get all scheme names
        scheme_names = list_schemes()
        
        # Create a grid of color swatches
        grid = VGroup()
        
        for i, name in enumerate(scheme_names[:6]):  # Show first 6
            scheme = get_scheme(name)
            
            # Create label
            label = Text(name, font_size=24)
            
            # Create color swatches
            colors = ['highlight', 'accent', 'time', 'displacement', 'dot']
            swatches = VGroup()
            
            for color_key in colors:
                swatch = Square(
                    side_length=0.4,
                    fill_color=scheme.hex(color_key),
                    fill_opacity=1,
                    stroke_width=2,
                    stroke_color=WHITE
                )
                swatches.add(swatch)
            
            swatches.arrange(RIGHT, buff=0.1)
            
            # Combine label and swatches
            item = VGroup(label, swatches).arrange(DOWN, buff=0.3)
            grid.add(item)
        
        # Arrange grid
        grid.arrange_in_grid(rows=2, cols=3, buff=1.0)
        grid.next_to(title, DOWN, buff=0.8)
        
        # Animate appearance
        self.play(
            *[FadeIn(item, shift=UP) for item in grid],
            rate_func=smooth,
            run_time=2.0,
            lag_ratio=0.1
        )
        
        self.wait(2)


class EasingFunctionDemo(Scene):
    """
    Demonstrate different easing functions visually.
    Shows how different timing functions affect motion.
    """
    
    def construct(self):
        scheme = get_scheme("contrasting_vibrancy")
        
        # Background
        bg = Rectangle(
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT,
            color=scheme.hex("background"),
            fill_opacity=1,
            stroke_width=0
        )
        self.add(bg)
        
        # Title
        title = Text(
            "Easing Functions Comparison",
            font_size=48,
            color=scheme.hex("text")
        ).to_edge(UP)
        self.add(title)
        
        # List of functions to demonstrate
        functions_to_demo = [
            ("linear", linear),
            ("smooth", smooth),
            ("rush_into", rush_into),
            ("ease_out_back", ease_out_back)
        ]
        
        start_x = -5
        end_x = 5
        
        for i, (name, func) in enumerate(functions_to_demo):
            # Create label
            label = Text(
                name,
                font_size=24,
                color=scheme.hex("text")
            )
            
            # Create dot
            dot = Dot(
                color=scheme.hex("highlight"),
                radius=0.2
            )
            
            # Create path line
            line = Line(
                start=LEFT * 5,
                end=RIGHT * 5,
                stroke_color=scheme.hex("accent"),
                stroke_width=2
            )
            
            # Position elements
            y_pos = 2 - i * 1.5
            label.move_to(LEFT * 6 + UP * y_pos)
            line.move_to(UP * y_pos)
            dot.move_to(line.get_start())
            
            # Add elements
            self.add(label, line)
            
            # Animate dot along path with the easing function
            self.play(
                dot.animate.move_to(line.get_end()),
                rate_func=func,
                run_time=2.0
            )
            
            # Keep dot visible briefly
            self.wait(0.3)
            
            # Remove dot
            self.remove(dot)
        
        self.wait(1)


if __name__ == "__main__":
    # To run these scenes:
    # manimgl example_usage.py UnifiedStyleExample
    # manimgl example_usage.py ColorSchemeShowcase
    # manimgl example_usage.py EasingFunctionDemo
    pass
