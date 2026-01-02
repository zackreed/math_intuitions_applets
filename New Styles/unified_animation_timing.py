"""
Unified Animation Timing and Easing Library
============================================

This module provides a comprehensive collection of timing functions (rate functions),
easing functions, and interpolation utilities that can be used across multiple
production contexts:
- Manim video animations
- CSS animations and transitions
- JavaScript/Canvas animations
- SVG animations

All functions follow a standard interface: f(t) -> value, where t is normalized
time (0 to 1), and the output is the eased value (typically 0 to 1).

Based on manim's rate_functions.py and animation timing utilities.

Author: Generated from manim libraries
Version: 1.0
"""

import numpy as np
from typing import Callable, Tuple, List, Dict, Any
import json


# ============================================================================
# BASIC EASING FUNCTIONS
# ============================================================================

def linear(t: float) -> float:
    """
    Linear interpolation - no easing
    
    Args:
        t: Time parameter (0 to 1)
        
    Returns:
        Linearly interpolated value
    """
    return t


def smooth(t: float) -> float:
    """
    Smooth easing with zero first and second derivatives at t=0 and t=1
    Creates a very smooth "ease in-out" effect
    Equivalent to bezier([0, 0, 0, 1, 1, 1])
    
    This is one of the most commonly used easing functions in Manim
    
    Args:
        t: Time parameter (0 to 1)
        
    Returns:
        Smoothly interpolated value
    """
    s = 1 - t
    return (t**3) * (10 * s * s + 5 * s * t + t * t)


def rush_into(t: float) -> float:
    """
    Fast start, then slow down
    Eases in quickly, good for objects appearing
    
    Args:
        t: Time parameter (0 to 1)
        
    Returns:
        Eased value
    """
    return 2 * smooth(0.5 * t)


def rush_from(t: float) -> float:
    """
    Slow start, then speed up
    Eases out quickly, good for objects disappearing
    
    Args:
        t: Time parameter (0 to 1)
        
    Returns:
        Eased value
    """
    return 2 * smooth(0.5 * (t + 1)) - 1


def slow_into(t: float) -> float:
    """
    Gradually ease into motion
    Square root easing
    
    Args:
        t: Time parameter (0 to 1)
        
    Returns:
        Eased value
    """
    return np.sqrt(1 - (1 - t) * (1 - t))


def double_smooth(t: float) -> float:
    """
    Two smooth easing curves combined
    Very gradual acceleration and deceleration
    
    Args:
        t: Time parameter (0 to 1)
        
    Returns:
        Eased value
    """
    if t < 0.5:
        return 0.5 * smooth(2 * t)
    else:
        return 0.5 * (1 + smooth(2 * t - 1))


def there_and_back(t: float) -> float:
    """
    Motion that goes forward then returns to start
    Useful for emphasis or temporary highlighting
    
    Args:
        t: Time parameter (0 to 1)
        
    Returns:
        Eased value (goes to 1 at t=0.5, returns to 0 at t=1)
    """
    new_t = 2 * t if t < 0.5 else 2 * (1 - t)
    return smooth(new_t)


def there_and_back_with_pause(t: float, pause_ratio: float = 1.0 / 3) -> float:
    """
    Motion that goes forward, pauses, then returns
    
    Args:
        t: Time parameter (0 to 1)
        pause_ratio: Fraction of time spent at peak (default 1/3)
        
    Returns:
        Eased value
    """
    a = 2.0 / (1.0 - pause_ratio)
    if t < 0.5 - pause_ratio / 2:
        return smooth(a * t)
    elif t < 0.5 + pause_ratio / 2:
        return 1
    else:
        return smooth(a - a * t)


def running_start(t: float, pull_factor: float = -0.5) -> float:
    """
    Starts with a slight backward motion before moving forward
    Creates anticipation effect
    
    Args:
        t: Time parameter (0 to 1)
        pull_factor: How far to pull back (negative value)
        
    Returns:
        Eased value
    """
    # Simplified bezier implementation for this specific curve
    return bezier([0, 0, pull_factor, pull_factor, 1, 1, 1])(t)


def overshoot(t: float, pull_factor: float = 1.5) -> float:
    """
    Overshoots the target then settles back
    Creates a bouncy, elastic feel
    
    Args:
        t: Time parameter (0 to 1)
        pull_factor: How far to overshoot (>1)
        
    Returns:
        Eased value
    """
    return bezier([0, 0, pull_factor, pull_factor, 1, 1])(t)


def wiggle(t: float, wiggles: float = 2) -> float:
    """
    Oscillating motion - moves back and forth
    
    Args:
        t: Time parameter (0 to 1)
        wiggles: Number of complete oscillations
        
    Returns:
        Oscillating value
    """
    return there_and_back(t) * np.sin(wiggles * np.pi * t)


def lingering(t: float) -> float:
    """
    Stay at start for a while, then move
    Good for delayed effects
    
    Args:
        t: Time parameter (0 to 1)
        
    Returns:
        Eased value
    """
    return squish_rate_func(lambda t: t, 0, 0.8)(t)


def exponential_decay(t: float, half_life: float = 0.1) -> float:
    """
    Exponential decay curve
    Approaches 1 asymptotically
    
    Args:
        t: Time parameter (0 to 1)
        half_life: Rate of decay (smaller = faster)
        
    Returns:
        Eased value
    """
    return 1 - np.exp(-t / half_life)


# ============================================================================
# STANDARD CSS-COMPATIBLE EASING FUNCTIONS
# ============================================================================

def ease_in_sine(t: float) -> float:
    """CSS ease-in-sine equivalent"""
    return 1 - np.cos((t * np.pi) / 2)


def ease_out_sine(t: float) -> float:
    """CSS ease-out-sine equivalent"""
    return np.sin((t * np.pi) / 2)


def ease_in_out_sine(t: float) -> float:
    """CSS ease-in-out-sine equivalent"""
    return -(np.cos(np.pi * t) - 1) / 2


def ease_in_quad(t: float) -> float:
    """CSS ease-in-quad equivalent"""
    return t * t


def ease_out_quad(t: float) -> float:
    """CSS ease-out-quad equivalent"""
    return 1 - (1 - t) * (1 - t)


def ease_in_out_quad(t: float) -> float:
    """CSS ease-in-out-quad equivalent"""
    return 2 * t * t if t < 0.5 else 1 - (-2 * t + 2) ** 2 / 2


def ease_in_cubic(t: float) -> float:
    """CSS ease-in-cubic equivalent"""
    return t * t * t


def ease_out_cubic(t: float) -> float:
    """CSS ease-out-cubic equivalent"""
    return 1 - (1 - t) ** 3


def ease_in_out_cubic(t: float) -> float:
    """CSS ease-in-out-cubic equivalent"""
    return 4 * t * t * t if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2


def ease_in_quart(t: float) -> float:
    """CSS ease-in-quart equivalent"""
    return t * t * t * t


def ease_out_quart(t: float) -> float:
    """CSS ease-out-quart equivalent"""
    return 1 - (1 - t) ** 4


def ease_in_out_quart(t: float) -> float:
    """CSS ease-in-out-quart equivalent"""
    return 8 * t * t * t * t if t < 0.5 else 1 - (-2 * t + 2) ** 4 / 2


def ease_in_expo(t: float) -> float:
    """CSS ease-in-expo equivalent"""
    return 0 if t == 0 else 2 ** (10 * t - 10)


def ease_out_expo(t: float) -> float:
    """CSS ease-out-expo equivalent"""
    return 1 if t == 1 else 1 - 2 ** (-10 * t)


def ease_in_out_expo(t: float) -> float:
    """CSS ease-in-out-expo equivalent"""
    if t == 0:
        return 0
    elif t == 1:
        return 1
    elif t < 0.5:
        return 2 ** (20 * t - 10) / 2
    else:
        return (2 - 2 ** (-20 * t + 10)) / 2


def ease_in_back(t: float, s: float = 1.70158) -> float:
    """CSS ease-in-back equivalent with overshoot"""
    return t * t * ((s + 1) * t - s)


def ease_out_back(t: float, s: float = 1.70158) -> float:
    """CSS ease-out-back equivalent with overshoot"""
    return 1 + (t - 1) ** 2 * ((s + 1) * (t - 1) + s)


def ease_in_out_back(t: float, s: float = 1.70158) -> float:
    """CSS ease-in-out-back equivalent with overshoot"""
    c = s * 1.525
    if t < 0.5:
        return (2 * t) ** 2 * ((c + 1) * 2 * t - c) / 2
    else:
        return ((2 * t - 2) ** 2 * ((c + 1) * (2 * t - 2) + c) + 2) / 2


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def squish_rate_func(
    func: Callable[[float], float],
    a: float = 0.4,
    b: float = 0.6
) -> Callable[[float], float]:
    """
    Compress a rate function to a specific time window
    
    Args:
        func: The rate function to compress
        a: Start of the window (0 to 1)
        b: End of the window (0 to 1)
        
    Returns:
        Modified rate function
    """
    def result(t):
        if a == b:
            return a
        elif t < a:
            return func(0)
        elif t > b:
            return func(1)
        else:
            return func((t - a) / (b - a))
    return result


def not_quite_there(
    func: Callable[[float], float] = smooth,
    proportion: float = 0.7
) -> Callable[[float], float]:
    """
    Scale a rate function to only go partway
    
    Args:
        func: The rate function to scale
        proportion: How far to go (0 to 1)
        
    Returns:
        Modified rate function
    """
    def result(t):
        return proportion * func(t)
    return result


def bezier(points: List[float]) -> Callable[[float], float]:
    """
    Create a bezier curve rate function
    
    Args:
        points: Control points for the bezier curve
        
    Returns:
        Bezier curve function
    """
    if len(points) == 0:
        raise Exception("bezier cannot be called on an empty list")
    
    n = len(points) - 1
    
    def choose(n, k):
        """Binomial coefficient"""
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        result = 1
        for i in range(min(k, n - k)):
            result = result * (n - i) // (i + 1)
        return result
    
    def result(t: float) -> float:
        return sum(
            ((1 - t)**(n - k)) * (t**k) * choose(n, k) * point
            for k, point in enumerate(points)
        )
    
    return result


# ============================================================================
# EASING FUNCTION REGISTRY
# ============================================================================

EASING_FUNCTIONS = {
    # Manim-style functions
    "linear": linear,
    "smooth": smooth,
    "rush_into": rush_into,
    "rush_from": rush_from,
    "slow_into": slow_into,
    "double_smooth": double_smooth,
    "there_and_back": there_and_back,
    "wiggle": wiggle,
    "lingering": lingering,
    "exponential_decay": exponential_decay,
    
    # CSS-compatible functions
    "ease_in_sine": ease_in_sine,
    "ease_out_sine": ease_out_sine,
    "ease_in_out_sine": ease_in_out_sine,
    "ease_in_quad": ease_in_quad,
    "ease_out_quad": ease_out_quad,
    "ease_in_out_quad": ease_in_out_quad,
    "ease_in_cubic": ease_in_cubic,
    "ease_out_cubic": ease_out_cubic,
    "ease_in_out_cubic": ease_in_out_cubic,
    "ease_in_quart": ease_in_quart,
    "ease_out_quart": ease_out_quart,
    "ease_in_out_quart": ease_in_out_quart,
    "ease_in_expo": ease_in_expo,
    "ease_out_expo": ease_out_expo,
    "ease_in_out_expo": ease_in_out_expo,
    "ease_in_back": ease_in_back,
    "ease_out_back": ease_out_back,
    "ease_in_out_back": ease_in_out_back,
}


# CSS timing functions mapping
CSS_TIMING_FUNCTIONS = {
    "linear": "linear",
    "ease": "ease",
    "ease-in": "cubic-bezier(0.42, 0, 1.0, 1.0)",
    "ease-out": "cubic-bezier(0, 0, 0.58, 1.0)",
    "ease-in-out": "cubic-bezier(0.42, 0, 0.58, 1.0)",
    "smooth": "cubic-bezier(0.37, 0, 0.63, 1)",  # Manim smooth approximation
    "ease-in-sine": "cubic-bezier(0.12, 0, 0.39, 0)",
    "ease-out-sine": "cubic-bezier(0.61, 1, 0.88, 1)",
    "ease-in-out-sine": "cubic-bezier(0.37, 0, 0.63, 1)",
    "ease-in-quad": "cubic-bezier(0.11, 0, 0.5, 0)",
    "ease-out-quad": "cubic-bezier(0.5, 1, 0.89, 1)",
    "ease-in-out-quad": "cubic-bezier(0.45, 0, 0.55, 1)",
    "ease-in-cubic": "cubic-bezier(0.32, 0, 0.67, 0)",
    "ease-out-cubic": "cubic-bezier(0.33, 1, 0.68, 1)",
    "ease-in-out-cubic": "cubic-bezier(0.65, 0, 0.35, 1)",
    "ease-in-back": "cubic-bezier(0.36, 0, 0.66, -0.56)",
    "ease-out-back": "cubic-bezier(0.34, 1.56, 0.64, 1)",
    "ease-in-out-back": "cubic-bezier(0.68, -0.6, 0.32, 1.6)",
}


def get_easing_function(name: str) -> Callable[[float], float]:
    """
    Get an easing function by name
    
    Args:
        name: Name of the easing function
        
    Returns:
        Easing function
    """
    return EASING_FUNCTIONS.get(name, linear)


def list_easing_functions() -> List[str]:
    """Get list of all available easing function names"""
    return list(EASING_FUNCTIONS.keys())


def get_css_timing_function(name: str) -> str:
    """
    Get CSS timing function string
    
    Args:
        name: Name of the timing function
        
    Returns:
        CSS timing function string (e.g., "cubic-bezier(...)")
    """
    return CSS_TIMING_FUNCTIONS.get(name, "linear")


# ============================================================================
# EXPORT FUNCTIONS
# ============================================================================

def sample_easing_function(
    func: Callable[[float], float],
    num_samples: int = 50
) -> List[Tuple[float, float]]:
    """
    Sample an easing function for visualization or export
    
    Args:
        func: Easing function to sample
        num_samples: Number of sample points
        
    Returns:
        List of (t, value) tuples
    """
    return [(t, func(t)) for t in np.linspace(0, 1, num_samples)]


def export_easing_to_json(filename: str = "easing_functions.json"):
    """
    Export sampled easing functions to JSON for use in web applications
    
    Args:
        filename: Output JSON filename
    """
    data = {}
    for name, func in EASING_FUNCTIONS.items():
        try:
            samples = sample_easing_function(func, num_samples=50)
            data[name] = {
                "samples": [[float(t), float(v)] for t, v in samples],
                "css": CSS_TIMING_FUNCTIONS.get(name, "linear")
            }
        except Exception as e:
            print(f"Warning: Could not sample {name}: {e}")
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


def export_easing_to_javascript(filename: str = "easing_functions.js"):
    """
    Export easing functions as JavaScript code
    
    Args:
        filename: Output JavaScript filename
    """
    with open(filename, 'w') as f:
        f.write("// Auto-generated easing functions for JavaScript use\n")
        f.write("// Generated from unified_animation_timing.py\n\n")
        
        f.write("const EASING_FUNCTIONS = {\n")
        
        # Write each function
        functions = []
        functions.append("  linear: (t) => t")
        functions.append("  smooth: (t) => {\n    const s = 1 - t;\n    return (t**3) * (10 * s * s + 5 * s * t + t * t);\n  }")
        functions.append("  rushInto: (t) => 2 * EASING_FUNCTIONS.smooth(0.5 * t)")
        functions.append("  rushFrom: (t) => 2 * EASING_FUNCTIONS.smooth(0.5 * (t + 1)) - 1")
        functions.append("  slowInto: (t) => Math.sqrt(1 - (1 - t) * (1 - t))")
        functions.append("  easeInSine: (t) => 1 - Math.cos((t * Math.PI) / 2)")
        functions.append("  easeOutSine: (t) => Math.sin((t * Math.PI) / 2)")
        functions.append("  easeInOutSine: (t) => -(Math.cos(Math.PI * t) - 1) / 2")
        functions.append("  easeInQuad: (t) => t * t")
        functions.append("  easeOutQuad: (t) => 1 - (1 - t) * (1 - t)")
        functions.append("  easeInOutQuad: (t) => t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2")
        functions.append("  easeInCubic: (t) => t * t * t")
        functions.append("  easeOutCubic: (t) => 1 - Math.pow(1 - t, 3)")
        functions.append("  easeInOutCubic: (t) => t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2")
        functions.append("  easeInBack: (t) => {\n    const s = 1.70158;\n    return t * t * ((s + 1) * t - s);\n  }")
        functions.append("  easeOutBack: (t) => {\n    const s = 1.70158;\n    return 1 + Math.pow(t - 1, 2) * ((s + 1) * (t - 1) + s);\n  }")
        
        f.write(",\n\n".join(functions))
        f.write("\n};\n\n")
        
        # CSS timing functions
        f.write("const CSS_TIMING_FUNCTIONS = {\n")
        items = [f"  '{k}': '{v}'" for k, v in CSS_TIMING_FUNCTIONS.items()]
        f.write(",\n".join(items))
        f.write("\n};\n\n")
        
        # Helper functions
        f.write("""
// Get easing function by name
function getEasingFunction(name) {
  return EASING_FUNCTIONS[name] || EASING_FUNCTIONS.linear;
}

// Get CSS timing function string
function getCssTimingFunction(name) {
  return CSS_TIMING_FUNCTIONS[name] || 'linear';
}

// Apply easing to a value
function applyEasing(startValue, endValue, t, easingName = 'linear') {
  const easingFunc = getEasingFunction(easingName);
  const easedT = easingFunc(t);
  return startValue + (endValue - startValue) * easedT;
}

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    EASING_FUNCTIONS,
    CSS_TIMING_FUNCTIONS,
    getEasingFunction,
    getCssTimingFunction,
    applyEasing
  };
}
""")


if __name__ == "__main__":
    # Example usage and testing
    print("Available Easing Functions:")
    print("===========================")
    for name in list_easing_functions():
        print(f"  - {name}")
    
    print("\n\nExample: Sampling 'smooth' function:")
    print("=====================================")
    samples = sample_easing_function(smooth, num_samples=11)
    for t, value in samples:
        print(f"  t={t:.1f} -> {value:.4f}")
    
    print("\n\nExporting to JSON and JavaScript...")
    export_easing_to_json("easing_functions.json")
    export_easing_to_javascript("easing_functions.js")
    print("Done! Files created: easing_functions.json, easing_functions.js")
