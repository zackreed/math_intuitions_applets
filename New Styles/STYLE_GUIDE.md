# Unified Style Guide

Complete documentation for maintaining visual consistency across Manim, SVG, and web-based productions.

---


COLOR SCHEMES
=============

All color schemes follow a consistent naming pattern for semantic colors:
- text_background: Background color for text elements
- text: Primary text color
- text_surrounding: Color for text surroundings/borders
- background: Main background color
- highlight: Color for emphasis and highlighting
- accent: Secondary accent color
- time: Color for time-related elements
- displacement: Color for position/displacement
- dot: Color for points and markers
- contrast_1: First contrasting color
- contrast_2: Second contrasting color

Available Schemes:
-----------------

1. DEFAULT
   Classic black background with vibrant colors
   - Best for: Traditional educational math videos
   - Style: High contrast, clear visibility

2. DARK_MUTED_PASTELS
   Soft pastels on dark gray background
   - Best for: Gentle, modern aesthetic
   - Style: Low contrast, easy on eyes

3. DEEP_JEWEL_TONES
   Rich, saturated colors on very dark background
   - Best for: Professional, sophisticated look
   - Style: Medium contrast, elegant

4. CONTRASTING_VIBRANCY
   Bright, bold colors with maximum energy
   - Best for: Attention-grabbing content
   - Style: Very high contrast, energetic

5. ERAU (Embry-Riddle Aeronautical University)
   Official university branding colors
   - Best for: ERAU-specific content
   - Style: University brand compliance

6. DARK
   Sophisticated dark theme with modern colors
   - Best for: Contemporary presentations
   - Style: Balanced contrast

7. HIGH_CONTRAST
   Maximum contrast for accessibility
   - Best for: Visibility in all conditions
   - Style: Stark, clear

8. WARM_SUNSET
   Warm oranges and browns
   - Best for: Organic, warm feeling
   - Style: Cozy, inviting

9. COOL_OCEAN
   Blues and cyans for oceanic feel
   - Best for: Calm, flowing content
   - Style: Cool, tranquil

10. FOREST_EARTH
    Greens and earth tones
    - Best for: Natural, grounded aesthetic
    - Style: Organic, stable

Usage Examples:
--------------

Python (Manim):
```python
from unified_color_schemes import get_scheme

scheme = get_scheme("dark_muted_pastels")
highlight_color = scheme.hex("highlight")  # '#ABDADC'
text_rgb = scheme.rgb("text")  # (0.894, 0.894, 0.894)
```

JavaScript:
```javascript
import { COLOR_SCHEMES, getColor } from './color_schemes.js';

const highlightColor = getColor('dark_muted_pastels', 'highlight');
```

CSS:
```css
[data-color-scheme='dark_muted_pastels'] {
  --highlight: #ABDADC;
  --text: #E4E4E4;
}
```


---


ANIMATION TIMING AND EASING
============================

Standard Durations:
------------------
- Quick: 0.5 seconds (brief transitions)
- Default: 1.0 seconds (most animations)
- Slow: 2.0 seconds (detailed transformations)
- Very Slow: 3+ seconds (complex sequences)

Easing Functions by Use Case:
-----------------------------

APPEARING (Fade In, Grow):
- smooth: Best general purpose (recommended)
- rush_into: Fast appearance
- ease_in_cubic: Gradual acceleration
- ease_in_back: Playful overshoot

DISAPPEARING (Fade Out, Shrink):
- smooth: Best general purpose (recommended)
- rush_from: Fast disappearance
- ease_out_cubic: Gradual deceleration
- ease_out_back: Playful overshoot

MOVING/TRANSFORMING:
- smooth: Best general purpose (recommended)
- linear: Constant speed
- ease_in_out_cubic: Smooth start and end
- there_and_back: Temporary highlight

EMPHASIS:
- wiggle: Oscillating attention
- there_and_back: Brief highlight
- overshoot: Bouncy emphasis

MATHEMATICAL VISUALIZATION:
- smooth: Default for clarity
- linear: When showing constant rates
- exponential_decay: For decay processes
- ease_in_quad: For quadratic growth

Function Descriptions:
---------------------

SMOOTH (Manim Standard):
  Most used in Manim. Very smooth ease-in-out with zero derivatives
  at endpoints. Creates professional, polished look.

RUSH_INTO / RUSH_FROM:
  Asymmetric easing - fast start/end, slow end/start.
  Good for objects entering/leaving frame.

THERE_AND_BACK:
  Goes to target then returns. Perfect for temporary highlighting
  or showing "what if" scenarios.

WIGGLE:
  Oscillating motion. Great for drawing attention or showing
  uncertainty/variation.

CSS-Compatible Functions:
------------------------
All ease_in_*, ease_out_*, ease_in_out_* functions have direct CSS
equivalents using cubic-bezier() or predefined timing functions.

Usage Examples:
--------------

Python (Manim):
```python
from unified_animation_timing import smooth, rush_into

# Fade in with smooth easing
self.play(FadeIn(obj), rate_func=smooth)

# Quick appearance
self.play(FadeIn(obj), rate_func=rush_into, run_time=0.5)
```

JavaScript:
```javascript
import { applyEasing } from './easing_functions.js';

const easedValue = applyEasing(0, 100, 0.5, 'smooth');
```

CSS:
```css
.animated {
  animation: fadeIn 1s cubic-bezier(0.37, 0, 0.63, 1);
}
```


---


VISUAL AESTHETICS AND PATTERNS
===============================

Spacing and Layout:
------------------
Manim Constants (keep consistent across platforms):
- SMALL_BUFF: 0.1 units (tight spacing)
- MED_SMALL_BUFF: 0.25 units 
- MED_LARGE_BUFF: 0.5 units (comfortable spacing)
- LARGE_BUFF: 1.0 units (generous spacing)

In CSS/SVG, scale these appropriately:
- 1 Manim unit ~= 100 pixels (at 1080p)
- SMALL_BUFF ~= 10px
- MED_LARGE_BUFF ~= 50px

Stroke Widths:
-------------
- Fine detail: 1-2 pixels
- Standard: 3-4 pixels (default)
- Emphasis: 5-6 pixels
- Bold: 8+ pixels

Font Sizing:
-----------
- Small text: 24-28pt (annotations, labels)
- Body text: 36-48pt (main content)
- Headers: 60-72pt (titles)
- Large display: 96pt+ (key equations)

Animation Best Practices:
-------------------------

1. CONSISTENCY
   - Use same easing for similar actions
   - Keep timing proportional to complexity
   - Maintain color meanings (e.g., red = error/important)

2. HIERARCHY
   - Important elements: slower, smoother animations
   - Supporting elements: faster, simpler transitions
   - Background: minimal or no animation

3. READABILITY
   - Allow time for viewers to read text
   - About 1 second per line of text minimum
   - Pause on key results

4. SMOOTHNESS
   - Default to 'smooth' easing in Manim
   - Avoid jarring linear animations for visual elements
   - Use linear only for constant-velocity demonstrations

5. ANTICIPATION
   - Use running_start for dramatic reveals
   - Add slight delay before important transformations
   - Build suspense with slower initial timing

Recommended Animation Sequences:
-------------------------------

INTRODUCING EQUATION:
1. Write equation (Write animation, 2s)
2. Brief pause (0.5s)
3. Highlight key term (Indicate, 1s)

TRANSFORMING EQUATION:
1. Indicate what will change (0.5s)
2. Transform (ReplacementTransform, 1-2s, smooth)
3. Brief pause to show result (0.5s)

GRAPH ANIMATION:
1. Draw axes (Create, 1s)
2. Draw function curve (ShowCreation, 2s)
3. Add labels (FadeIn, 0.5s each)
4. Animate point along curve (MoveAlongPath, 3-5s, linear)

COLOR USAGE PATTERNS:
--------------------

Educational Math Videos:
- Blue family: Functions, curves, primary objects
- Green family: Positive values, solutions
- Red family: Important points, errors, warnings
- Yellow family: Highlights, emphasis
- Purple family: Time, animation progress

Consistent Semantic Meanings:
- Red dots: Important points, answers
- Blue: Primary mathematical objects
- Green: Secondary objects, comparisons
- Yellow: Temporary highlights
- White/Light: Text, labels
- Dark: Backgrounds, de-emphasis


---


CROSS-PLATFORM IMPLEMENTATION
==============================

This section provides equivalent code patterns across different platforms
to maintain visual consistency.

1. COLOR IMPLEMENTATION
-----------------------

Python (Manim):
```python
from unified_color_schemes import get_scheme

scheme = get_scheme("dark_muted_pastels")
circle = Circle(color=scheme.hex("highlight"))
```

JavaScript (Canvas):
```javascript
import { COLOR_SCHEMES } from './color_schemes.js';

ctx.fillStyle = COLOR_SCHEMES.dark_muted_pastels.highlight;
ctx.fill();
```

SVG:
```xml
<circle fill="#ABDADC" />
```

CSS:
```css
[data-scheme="dark_muted_pastels"] .highlight {
  background-color: var(--highlight);
}
```

2. ANIMATION TIMING
-------------------

Python (Manim):
```python
from unified_animation_timing import smooth

self.play(
    Transform(obj1, obj2),
    rate_func=smooth,
    run_time=1.0
)
```

JavaScript (requestAnimationFrame):
```javascript
import { applyEasing } from './easing_functions.js';

function animate(startTime) {
  const elapsed = (Date.now() - startTime) / 1000;
  const t = Math.min(elapsed / duration, 1);
  const easedT = EASING_FUNCTIONS.smooth(t);
  
  value = startValue + (endValue - startValue) * easedT;
  
  if (t < 1) requestAnimationFrame(() => animate(startTime));
}
```

CSS Animation:
```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.animated {
  animation: fadeIn 1s cubic-bezier(0.37, 0, 0.63, 1);
}
```

GSAP (JavaScript library):
```javascript
gsap.to(element, {
  duration: 1,
  x: 100,
  ease: "power3.inOut"  // Similar to smooth
});
```

3. RESPONSIVE SCALING
---------------------

Manim uses fixed coordinate system:
- Frame: 16:9 ratio
- Height: 8 units
- Width: 14.22 units (automatically calculated)

For web, scale proportionally:
```javascript
const scale = window.innerHeight / 800; // Base 800px height
const manimUnit = 100 * scale; // 1 Manim unit in pixels
```

4. TEXT RENDERING
-----------------

Manim:
```python
text = Text("Hello", font_size=48)
```

SVG:
```xml
<text font-size="48" font-family="sans-serif">Hello</text>
```

Canvas:
```javascript
ctx.font = "48px sans-serif";
ctx.fillText("Hello", x, y);
```

5. STROKE AND FILL
------------------

Manim:
```python
circle = Circle(
    stroke_color=BLUE,
    stroke_width=4,
    fill_color=RED,
    fill_opacity=0.5
)
```

SVG:
```xml
<circle
  stroke="#58C4DD"
  stroke-width="4"
  fill="#FC6255"
  fill-opacity="0.5"
/>
```

Canvas:
```javascript
ctx.strokeStyle = "#58C4DD";
ctx.lineWidth = 4;
ctx.fillStyle = "rgba(252, 98, 85, 0.5)";
ctx.stroke();
ctx.fill();
```


---


QUICK REFERENCE CARD
====================

Most Common Combinations:
------------------------

1. STANDARD FADE IN:
   - Easing: smooth
   - Duration: 1.0s
   - Color: From scheme

2. STANDARD FADE OUT:
   - Easing: smooth  
   - Duration: 0.8s
   - Final opacity: 0

3. TRANSFORM:
   - Easing: smooth
   - Duration: 1.5-2.0s
   - Path: Direct interpolation

4. EMPHASIS:
   - Easing: there_and_back
   - Duration: 0.8s
   - Scale: 1.2x

5. APPEAR WITH BOUNCE:
   - Easing: ease_out_back
   - Duration: 0.8s
   - Overshoot: About 20%

Default Values:
--------------
- Animation duration: 1.0s
- Fade in/out opacity: 0 to 1
- Default easing: smooth (Manim) / ease (CSS)
- Text display time: 2-3s minimum
- Pause between scenes: 0.5-1.0s

File Structure:
--------------
unified_color_schemes.py
  ├─ ColorScheme class
  ├─ COLOR_SCHEMES dict
  ├─ Export functions (CSS, JS)
  └─ Utility functions

unified_animation_timing.py
  ├─ Easing functions
  ├─ CSS equivalents
  ├─ Export functions
  └─ Sampling utilities

unified_style_guide.py
  └─ This documentation

Generated Files:
---------------
- color_schemes.css (CSS variables)
- color_schemes.js (JavaScript constants)
- easing_functions.json (Sampled curves)
- easing_functions.js (JavaScript functions)

Usage Workflow:
--------------
1. Choose color scheme for project
2. Import scheme in all contexts
3. Use consistent easing functions
4. Match timing across platforms
5. Test on all target platforms
