"""
Unified Color Schemes Library
==============================

This module provides a comprehensive collection of color schemes that can be
used across multiple production contexts:
- Manim video animations
- Custom SVG graphics
- HTML/JavaScript interactive applets

All color values are provided in multiple formats for maximum compatibility:
- Hex codes (for web/SVG)
- RGB tuples (for programmatic use)
- Named constants (for Manim)

Author: Generated from manim libraries
Version: 1.0
"""

from typing import Dict, Tuple, List, Any


def hex_to_rgb(hex_str: str) -> Tuple[float, float, float]:
    """Convert hex color to RGB tuple (0-1)"""
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) / 255.0 for i in (0, 2, 4))


class ColorScheme:
    """Base class for color scheme definitions"""
    
    def __init__(self, name: str, colors: Dict[str, str]):
        self.name = name
        self._hex_colors = colors
        self._rgb_colors = {}
        self._rgba_colors = {}
        
        # Pre-compute all color formats
        for key, hex_value in colors.items():
            try:
                rgb = hex_to_rgb(hex_value)
                self._rgb_colors[key] = rgb
                self._rgba_colors[key] = (*rgb, 1.0)
            except:
                # Fallback for invalid colors
                self._rgb_colors[key] = (0, 0, 0)
                self._rgba_colors[key] = (0, 0, 0, 1.0)
    
    def hex(self, key: str) -> str:
        """Get color as hex string (e.g., '#FFFFFF')"""
        return self._hex_colors.get(key, "#000000")
    
    def rgb(self, key: str) -> Tuple[float, float, float]:
        """Get color as RGB tuple (values 0-1)"""
        return self._rgb_colors.get(key, (0, 0, 0))
    
    def rgba(self, key: str, alpha: float = 1.0) -> Tuple[float, float, float, float]:
        """Get color as RGBA tuple (values 0-1)"""
        r, g, b = self.rgb(key)
        return (r, g, b, alpha)
    
    def rgb255(self, key: str) -> Tuple[int, int, int]:
        """Get color as RGB tuple (values 0-255)"""
        r, g, b = self.rgb(key)
        return (int(r * 255), int(g * 255), int(b * 255))
    
    def rgba255(self, key: str, alpha: int = 255) -> Tuple[int, int, int, int]:
        """Get color as RGBA tuple (values 0-255)"""
        r, g, b = self.rgb255(key)
        return (r, g, b, alpha)
    
    def css_rgb(self, key: str) -> str:
        """Get color as CSS rgb string"""
        r, g, b = self.rgb255(key)
        return f"rgb({r}, {g}, {b})"
    
    def css_rgba(self, key: str, alpha: float = 1.0) -> str:
        """Get color as CSS rgba string"""
        r, g, b = self.rgb255(key)
        return f"rgba({r}, {g}, {b}, {alpha})"
    
    def to_dict(self) -> Dict[str, Any]:
        """Export scheme as dictionary with all formats"""
        return {
            "name": self.name,
            "hex": self._hex_colors,
            "rgb": {k: list(v) for k, v in self._rgb_colors.items()},
            "rgb255": {k: list(self.rgb255(k)) for k in self._hex_colors.keys()},
        }
    
    def to_css_variables(self, prefix: str = "") -> str:
        """Generate CSS custom properties (variables) for this scheme"""
        lines = [":root {"]
        for key, hex_value in self._hex_colors.items():
            var_name = f"--{prefix}{key.replace('_', '-')}" if prefix else f"--{key.replace('_', '-')}"
            lines.append(f"  {var_name}: {hex_value};")
        lines.append("}")
        return "\n".join(lines)
    
    def to_javascript_object(self, var_name: str = "colorScheme") -> str:
        """Generate JavaScript object definition"""
        lines = [f"const {var_name} = {{"]
        items = []
        for key, hex_value in self._hex_colors.items():
            items.append(f"  {key}: '{hex_value}'")
        lines.append(",\n".join(items))
        lines.append("};")
        return "\n".join(lines)
    
    def __getitem__(self, key: str) -> str:
        """Allow dict-like access to hex values"""
        return self.hex(key)
    
    def keys(self) -> List[str]:
        """Get all color keys"""
        return list(self._hex_colors.keys())


# ============================================================================
# PREDEFINED COLOR SCHEMES
# ============================================================================

COLOR_SCHEMES_DATA = {
    "default": {
        "text_background": "#000000",  # BLACK
        "text": "#FFFFFF",              # WHITE
        "text_surrounding": "#000000",  # BLACK
        "background": "#000000",        # BLACK
        "highlight": "#FFFF00",         # YELLOW
        "accent": "#58C4DD",            # BLUE_C
        "time": "#C55F73",              # PURPLE
        "displacement": "#83C167",      # GREEN
        "dot": "#FC6255",               # RED
        "contrast_1": "#FF8C00",        # Dark Orange
        "contrast_2": "#00CED1"         # Dark Turquoise
    },
    
    "dark_muted_pastels": {
        "text_background": "#2C2C2C",   # Dark Gray
        "text": "#E4E4E4",              # Light Gray
        "text_surrounding": "#2C2C2C",  # Dark Gray
        "background": "#2C2C2C",        # Dark Gray
        "highlight": "#ABDADC",         # Light Teal
        "accent": "#FFC1CC",            # Light Pink
        "time": "#B39CD0",              # Light Purple
        "displacement": "#B2DFDB",      # Light Cyan
        "dot": "#FF6B6B",               # Soft Red
        "contrast_1": "#FFB74D",        # Light Orange
        "contrast_2": "#81C784"         # Light Green
    },
    
    "deep_jewel_tones": {
        "text_background": "#1a1a1a",   # Very Dark Gray
        "text": "#f0f0f0",              # Very Light Gray
        "text_surrounding": "#1a1a1a",  # Very Dark Gray
        "background": "#1a1a1a",        # Very Dark Gray
        "highlight": "#004d61",         # Deep Teal
        "accent": "#822659",            # Deep Magenta
        "time": "#3e5641",              # Deep Olive Green
        "displacement": "#90EE90",      # Light Green
        "dot": "#FF6B6B",               # Soft Red
        "contrast_1": "#FFB74D",        # Light Orange
        "contrast_2": "#9C27B0",        # Deep Purple
    },
    
    "contrasting_vibrancy": {
        "text_background": "#181818",   # Very Dark Gray
        "text": "#f7f7f7",              # Very Light Gray
        "text_surrounding": "#181818",  # Very Dark Gray
        "background": "#181818",        # Very Dark Gray
        "highlight": "#ff5722",         # Vibrant Orange
        "accent": "#673ab7",            # Deep Purple
        "time": "#ffeb3b",              # Bright Yellow
        "displacement": "#009688",      # Teal
        "dot": "#e91e63",               # Pink
        "contrast_1": "#c2185b",        # Deep Pink
        "contrast_2": "#4caf50"         # Green
    },
    
    "erau": {
        "text_background": "#03539E",   # UNRIVALED_BLUE
        "text": "#FFFFFF",              # White
        "text_surrounding": "#FFCB06",  # SUNRISE_YELLOW
        "background": "#000000",        # Black
        "highlight": "#FFCB06",         # SUNRISE_YELLOW
        "accent": "#01B2E3",            # ALTITUDE_BLUE
        "time": "#FFE066",              # Bright light yellow
        "displacement": "#90EE90",      # Light green
        "dot": "#FF6B6B",               # ALTITUDE_RED
        "contrast_1": "#FF1493",        # Deep Pink
        "contrast_2": "#32CD32"         # Lime Green
    },
    
    "dark": {
        "text_background": "#000000",   # Black
        "text": "#E0E0E0",              # Light Gray
        "text_surrounding": "#000000",  # Black
        "background": "#000000",        # Black
        "highlight": "#FF6B6B",         # Soft Red
        "accent": "#4ECDC4",            # Turquoise
        "time": "#45B7D1",              # Sky Blue
        "displacement": "#96CEB4",      # Mint
        "dot": "#FECA57",               # Golden Yellow
        "contrast_1": "#FF69B4",        # Hot Pink
        "contrast_2": "#00FA9A"         # Medium Spring Green
    },
    
    "high_contrast": {
        "text_background": "#000000",   # Black
        "text": "#FFFFFF",              # White
        "text_surrounding": "#000000",  # Black
        "background": "#000000",        # Black
        "highlight": "#FFFF00",         # Yellow
        "accent": "#00FFFF",            # Cyan
        "time": "#FF00FF",              # Magenta
        "displacement": "#00FF00",      # Lime
        "dot": "#FF0000",               # Red
        "contrast_1": "#FFA500",        # Orange
        "contrast_2": "#8A2BE2"         # Blue Violet
    },
    
    # Additional schemes for variety
    "warm_sunset": {
        "text_background": "#1a0f0a",   # Deep Brown
        "text": "#fff8f0",              # Warm White
        "text_surrounding": "#2a1810",  # Brown
        "background": "#1a0f0a",        # Deep Brown
        "highlight": "#ff6b35",         # Coral
        "accent": "#f7931e",            # Orange
        "time": "#fdc500",              # Golden
        "displacement": "#c1666b",      # Dusty Rose
        "dot": "#d62828",               # Red
        "contrast_1": "#fcbf49",        # Yellow
        "contrast_2": "#8b4513"         # Saddle Brown
    },
    
    "cool_ocean": {
        "text_background": "#0a1f2e",   # Deep Navy
        "text": "#e8f4f8",              # Ice Blue
        "text_surrounding": "#0a1f2e",  # Deep Navy
        "background": "#0a1f2e",        # Deep Navy
        "highlight": "#00d9ff",         # Bright Cyan
        "accent": "#1e90ff",            # Dodger Blue
        "time": "#40e0d0",              # Turquoise
        "displacement": "#7fffd4",      # Aquamarine
        "dot": "#ff6b9d",               # Pink
        "contrast_1": "#ff1493",        # Deep Pink
        "contrast_2": "#00fa9a"         # Medium Spring Green
    },
    
    "forest_earth": {
        "text_background": "#1a2e1a",   # Deep Forest
        "text": "#f0f8f0",              # Mint White
        "text_surrounding": "#1a2e1a",  # Deep Forest
        "background": "#1a2e1a",        # Deep Forest
        "highlight": "#90ee90",         # Light Green
        "accent": "#8fbc8f",            # Dark Sea Green
        "time": "#daa520",              # Goldenrod
        "displacement": "#9acd32",      # Yellow Green
        "dot": "#dc143c",               # Crimson
        "contrast_1": "#ff8c00",        # Dark Orange
        "contrast_2": "#4682b4"         # Steel Blue
    },
}


# Create ColorScheme objects for each predefined scheme
COLOR_SCHEMES = {
    name: ColorScheme(name, colors)
    for name, colors in COLOR_SCHEMES_DATA.items()
}


def get_scheme(name: str = "default") -> ColorScheme:
    """
    Get a color scheme by name
    
    Args:
        name: Name of the color scheme
        
    Returns:
        ColorScheme object
        
    Example:
        >>> scheme = get_scheme("dark_muted_pastels")
        >>> print(scheme.hex("highlight"))
        '#ABDADC'
    """
    return COLOR_SCHEMES.get(name, COLOR_SCHEMES["default"])


def list_schemes() -> List[str]:
    """Get list of all available color scheme names"""
    return list(COLOR_SCHEMES.keys())


def export_all_schemes_to_css(filename: str = "color_schemes.css", prefix: str = ""):
    """
    Export all color schemes to a CSS file
    
    Args:
        filename: Output CSS filename
        prefix: Optional prefix for CSS variable names (e.g., "scheme-name-")
    """
    with open(filename, 'w') as f:
        f.write("/* Auto-generated color schemes for web use */\n")
        f.write("/* Generated from unified_color_schemes.py */\n\n")
        
        for scheme_name, scheme in COLOR_SCHEMES.items():
            f.write(f"/* {scheme_name} color scheme */\n")
            f.write(f"[data-color-scheme='{scheme_name}'] {{\n")
            for key in scheme.keys():
                var_name = f"--{prefix}{key.replace('_', '-')}"
                f.write(f"  {var_name}: {scheme.hex(key)};\n")
            f.write("}\n\n")


def export_all_schemes_to_js(filename: str = "color_schemes.js"):
    """
    Export all color schemes to a JavaScript file
    
    Args:
        filename: Output JavaScript filename
    """
    with open(filename, 'w') as f:
        f.write("// Auto-generated color schemes for JavaScript use\n")
        f.write("// Generated from unified_color_schemes.py\n\n")
        
        f.write("const COLOR_SCHEMES = {\n")
        scheme_lines = []
        for scheme_name, scheme in COLOR_SCHEMES.items():
            colors_obj = "{\n"
            color_lines = []
            for key in scheme.keys():
                color_lines.append(f"    {key}: '{scheme.hex(key)}'")
            colors_obj += ",\n".join(color_lines)
            colors_obj += "\n  }"
            scheme_lines.append(f"  {scheme_name}: {colors_obj}")
        f.write(",\n\n".join(scheme_lines))
        f.write("\n};\n\n")
        
        # Add helper functions
        f.write("""
// Helper function to get a color from a scheme
function getColor(schemeName, colorKey) {
  return COLOR_SCHEMES[schemeName]?.[colorKey] || '#000000';
}

// Helper function to convert hex to RGB
function hexToRgb(hex) {
  const result = /^#?([a-f\\d]{2})([a-f\\d]{2})([a-f\\d]{2})$/i.exec(hex);
  return result ? {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  } : null;
}

// Helper function to convert hex to RGBA string
function hexToRgba(hex, alpha = 1.0) {
  const rgb = hexToRgb(hex);
  return rgb ? `rgba(${rgb.r}, ${rgb.g}, ${rgb.b}, ${alpha})` : 'rgba(0, 0, 0, 1)';
}

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { COLOR_SCHEMES, getColor, hexToRgb, hexToRgba };
}
""")


# Manim-specific exports (for backward compatibility)
def get_manim_color_dict(scheme_name: str = "default") -> Dict[str, str]:
    """
    Get color scheme in Manim-compatible format
    
    Args:
        scheme_name: Name of the color scheme
        
    Returns:
        Dictionary mapping color keys to hex strings
    """
    scheme = get_scheme(scheme_name)
    return {key: scheme.hex(key) for key in scheme.keys()}


if __name__ == "__main__":
    # Example usage and testing
    print("Available Color Schemes:")
    print("========================")
    for name in list_schemes():
        print(f"  - {name}")
    
    print("\n\nExample: 'default' scheme colors:")
    print("==================================")
    default = get_scheme("default")
    for key in default.keys():
        print(f"  {key:20} -> {default.hex(key):10} | RGB: {default.rgb255(key)}")
    
    print("\n\nExporting to CSS and JavaScript...")
    export_all_schemes_to_css("color_schemes.css")
    export_all_schemes_to_js("color_schemes.js")
    print("Done! Files created: color_schemes.css, color_schemes.js")
