# Unified Style and Animation Library

A comprehensive collection of color schemes, animation timing functions, and style guides for creating consistent visual experiences across **Manim animations**, **custom SVGs**, and **HTML/JavaScript interactive applets**.

## 📁 Library Structure

```
unified_style_library/
├── unified_color_schemes.py      # Color scheme definitions and exports
├── unified_animation_timing.py   # Easing/timing functions and exports  
├── unified_style_guide.py        # Complete documentation and guides
├── README.md                      # This file
└── Generated files (after running scripts):
    ├── color_schemes.css         # CSS custom properties
    ├── color_schemes.js          # JavaScript color constants
    ├── easing_functions.json     # Sampled easing curves
    ├── easing_functions.js       # JavaScript easing functions
    └── STYLE_GUIDE.md            # Markdown documentation
```

## 🎨 Color Schemes

### Available Schemes

1. **default** - Classic black background with vibrant colors
2. **dark_muted_pastels** - Soft pastels on dark gray
3. **deep_jewel_tones** - Rich, saturated jewel colors
4. **contrasting_vibrancy** - Bright, bold, maximum energy
5. **erau** - ERAU university branding
6. **dark** - Modern sophisticated dark theme
7. **high_contrast** - Maximum accessibility
8. **warm_sunset** - Warm oranges and browns
9. **cool_ocean** - Blues and cyans
10. **forest_earth** - Greens and earth tones

### Color Keys

Each scheme provides:
- `text_background` - Background for text elements
- `text` - Primary text color
- `text_surrounding` - Text borders/surroundings
- `background` - Main background
- `highlight` - Emphasis color
- `accent` - Secondary accent
- `time` - Time-related elements
- `displacement` - Position/movement
- `dot` - Points and markers
- `contrast_1`, `contrast_2` - Contrasting colors

## ⏱️ Animation Timing

### Core Functions

**Manim Standard:**
- `smooth` - Most used, professional smooth ease-in-out
- `rush_into` - Fast start, slow end
- `rush_from` - Slow start, fast end
- `there_and_back` - Temporary highlight effect
- `wiggle` - Oscillating motion

**CSS-Compatible:**
- `ease_in_sine/quad/cubic/quart/expo/back`
- `ease_out_sine/quad/cubic/quart/expo/back`
- `ease_in_out_sine/quad/cubic/quart/expo/back`
- `linear` - Constant speed

### Recommended Durations

- Quick: 0.5s
- Default: 1.0s
- Slow: 2.0s
- Complex: 3.0s+

## 🚀 Quick Start

### Python (Manim)

```python
from unified_color_schemes import get_scheme
from unified_animation_timing import smooth, rush_into

# Get a color scheme
scheme = get_scheme("dark_muted_pastels")

# Use colors
highlight = scheme.hex("highlight")  # '#ABDADC'
text_rgb = scheme.rgb("text")        # (0.894, 0.894, 0.894)

# Animate
self.play(
    FadeIn(obj),
    rate_func=smooth,
    run_time=1.0
)
```

### JavaScript

```javascript
import { COLOR_SCHEMES, getColor } from './color_schemes.js';
import { applyEasing } from './easing_functions.js';

// Get color
const highlight = getColor('dark_muted_pastels', 'highlight');

// Apply easing
const easedValue = applyEasing(0, 100, 0.5, 'smooth');
```

### CSS

```css
[data-color-scheme='dark_muted_pastels'] {
  --highlight: #ABDADC;
  --text: #E4E4E4;
}

.animated {
  animation: fadeIn 1s cubic-bezier(0.37, 0, 0.63, 1); /* smooth */
}
```

## 📦 Installation and Setup

### Step 1: Copy Files

Copy the three main Python files to your project:
- `unified_color_schemes.py`
- `unified_animation_timing.py`
- `unified_style_guide.py`

### Step 2: Generate Web Assets

Run the Python files to generate web-compatible assets:

```bash
# Generate color scheme files
python unified_color_schemes.py

# Generate easing function files
python unified_animation_timing.py

# Generate documentation
python unified_style_guide.py
```

This creates:
- `color_schemes.css` - Ready-to-use CSS variables
- `color_schemes.js` - JavaScript constants
- `easing_functions.json` - Data for visualization
- `easing_functions.js` - JavaScript easing functions
- `STYLE_GUIDE.md` - Complete documentation

### Step 3: Use in Your Projects

**Manim:** Import directly from Python files

**Web:** Include generated CSS/JS files:
```html
<link rel="stylesheet" href="color_schemes.css">
<script type="module" src="color_schemes.js"></script>
<script type="module" src="easing_functions.js"></script>
```

## 📖 Usage Examples

### Complete Manim Scene

```python
from manimlib import *
from unified_color_schemes import get_scheme
from unified_animation_timing import smooth, there_and_back

class StyledScene(Scene):
    def construct(self):
        # Get color scheme
        scheme = get_scheme("dark_muted_pastels")
        
        # Create styled objects
        circle = Circle(
            color=scheme.hex("highlight"),
            fill_opacity=0.5
        )
        text = Text(
            "Hello",
            color=scheme.hex("text")
        )
        
        # Animate with standard timing
        self.play(
            FadeIn(circle),
            rate_func=smooth,
            run_time=1.0
        )
        
        # Emphasize
        self.play(
            Indicate(text),
            rate_func=there_and_back,
            run_time=0.8
        )
```

### Complete Web Animation

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="color_schemes.css">
  <style>
    [data-color-scheme='dark_muted_pastels'] {
      background: var(--background);
      color: var(--text);
    }
    
    .animated-circle {
      fill: var(--highlight);
      animation: fadeIn 1s cubic-bezier(0.37, 0, 0.63, 1);
    }
  </style>
</head>
<body data-color-scheme='dark_muted_pastels'>
  <svg width="200" height="200">
    <circle class="animated-circle" cx="100" cy="100" r="50" />
  </svg>
  
  <script type="module">
    import { applyEasing } from './easing_functions.js';
    
    // Animate programmatically
    const startTime = Date.now();
    const duration = 1000;
    
    function animate() {
      const elapsed = Date.now() - startTime;
      const t = Math.min(elapsed / duration, 1);
      const easedT = applyEasing(0, 1, t, 'smooth');
      
      // Use easedT for your animation
      
      if (t < 1) requestAnimationFrame(animate);
    }
    
    animate();
  </script>
</body>
</html>
```

## 🎯 Design Philosophy

### Consistency Across Platforms

The library ensures visual consistency by:
1. **Identical color values** across all platforms
2. **Equivalent timing functions** (Python ↔ JavaScript ↔ CSS)
3. **Proportional spacing** that scales appropriately
4. **Semantic naming** that maintains meaning

### Best Practices

1. **Use `smooth` as default** - Most professional looking
2. **Match colors to meaning** - Blue for primary, red for important, etc.
3. **Keep timing proportional** - Complex animations take longer
4. **Test on all platforms** - Ensure consistency

## 📚 API Reference

### ColorScheme Class Methods

```python
scheme = get_scheme("dark_muted_pastels")

scheme.hex(key)           # Get hex string: '#ABDADC'
scheme.rgb(key)           # Get RGB tuple (0-1): (0.671, 0.855, 0.863)
scheme.rgba(key, alpha)   # Get RGBA tuple (0-1)
scheme.rgb255(key)        # Get RGB tuple (0-255): (171, 218, 220)
scheme.css_rgb(key)       # Get CSS string: 'rgb(171, 218, 220)'
scheme.css_rgba(key, a)   # Get CSS string with alpha
scheme.to_css_variables() # Generate CSS custom properties
scheme.to_javascript_object() # Generate JS object
```

### Easing Functions

```python
# Get function by name
func = get_easing_function("smooth")

# Apply to value
t = 0.5  # Halfway through animation
eased_t = func(t)  # Returns eased value

# Sample for visualization
samples = sample_easing_function(smooth, num_samples=50)

# Get CSS equivalent
css_timing = get_css_timing_function("smooth")
# Returns: 'cubic-bezier(0.37, 0, 0.63, 1)'
```

### Export Functions

```python
# Export color schemes
export_all_schemes_to_css("colors.css")
export_all_schemes_to_js("colors.js")

# Export easing functions
export_easing_to_json("easing.json")
export_easing_to_javascript("easing.js")

# Export documentation
export_guide_to_markdown("GUIDE.md")
```

## 🔧 Customization

### Adding Custom Color Schemes

```python
# In unified_color_schemes.py, add to COLOR_SCHEMES_DATA:

COLOR_SCHEMES_DATA["my_custom_scheme"] = {
    "text_background": "#1a1a1a",
    "text": "#ffffff",
    "text_surrounding": "#1a1a1a",
    "background": "#0a0a0a",
    "highlight": "#ff6b6b",
    "accent": "#4ecdc4",
    "time": "#45b7d1",
    "displacement": "#96ceb4",
    "dot": "#feca57",
    "contrast_1": "#ff69b4",
    "contrast_2": "#00fa9a"
}
```

### Adding Custom Easing Functions

```python
# In unified_animation_timing.py:

def my_custom_ease(t: float) -> float:
    """My custom easing function"""
    return t * t * (3 - 2 * t)

# Add to registry
EASING_FUNCTIONS["my_custom_ease"] = my_custom_ease
```

## 🤝 Integration with Existing Code

### With Manim's scene_decorators

```python
from unified_color_schemes import get_manim_color_dict

# Get in scene_decorators format
colors = get_manim_color_dict("dark_muted_pastels")

# Use with existing decorators
@with_branding(scheme_name="dark_muted_pastels")
class MyScene(Scene):
    def construct(self):
        # Your scene code
        pass
```

### With D3.js

```javascript
import { COLOR_SCHEMES } from './color_schemes.js';

const colorScale = d3.scaleOrdinal()
  .domain(['highlight', 'accent', 'time'])
  .range([
    COLOR_SCHEMES.dark_muted_pastels.highlight,
    COLOR_SCHEMES.dark_muted_pastels.accent,
    COLOR_SCHEMES.dark_muted_pastels.time
  ]);
```

### With Three.js

```javascript
import { hexToRgb } from './color_schemes.js';

const color = hexToRgb(COLOR_SCHEMES.dark_muted_pastels.highlight);
const material = new THREE.MeshBasicMaterial({
  color: new THREE.Color(color.r / 255, color.g / 255, color.b / 255)
});
```

## 📋 Requirements

### Python
- Python 3.7+
- NumPy
- colour (pip install colour)

### JavaScript/Web
- Modern browser with ES6 module support
- No additional dependencies

## 🐛 Troubleshooting

**Colors look different across platforms:**
- Ensure you're using the same color space (sRGB)
- Check monitor calibration
- Verify gamma correction settings

**Animations feel different:**
- Check frame rates match (60 FPS recommended)
- Verify timing precision (milliseconds)
- Test on target devices

**Export functions fail:**
- Check write permissions
- Verify Python packages installed
- Ensure colour package version is compatible

## 📄 License

Use freely in your projects. Based on Manim's animation library and extended
for cross-platform consistency.

## 🙏 Acknowledgments

- Built from [ManimGL](https://github.com/3b1b/manim) animation library
- Inspired by 3Blue1Brown's visual style
- CSS easing functions from [easings.net](https://easings.net)

## 📞 Support

For issues or questions:
1. Check the generated STYLE_GUIDE.md for detailed documentation
2. Review the example code in this README
3. Test with the provided Python files to ensure proper setup

---

**Version:** 1.0  
**Last Updated:** January 2026  
**Compatibility:** Manim, CSS3, ES6+ JavaScript
