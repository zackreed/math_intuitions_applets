#!/usr/bin/env python3
"""
Fix hardcoded colors in applets to use styleConfig color scheme system
"""
import os
import re

APPLETS_DIR = "/workspaces/math_intuitions_applets/applets"

# Color mapping from hardcoded hex to styleConfig keys
COLOR_MAPPINGS = {
    # Common colors
    '#1a1a2e': 'background',
    '#16213e': 'text-background', 
    '#0f1925': 'text-background',
    '#0f3460': 'text-background',
    '#e8e8e8': 'text',
    '#fff': 'text',
    '#ffffff': 'text',
    
    # Highlights and accents
    '#00d9ff': 'highlight',
    '#4ecca3': 'accent',
    '#77e4c8': 'accent',
    '#4ecdc4': 'accent',
    
    # Special colors
    '#ffe66d': 'time',
    '#ff6b6b': 'dot',
    '#e94560': 'dot',
    '#f9d423': 'time',
    
    # Borders and grays
    '#4a5568': 'border-color',
    '#2d3748': 'border-color',
    '#6c757d': 'border-color',
    '#aaa': 'border-color',
    
    # Hover states
    '#c93952': 'dot',  # darker red
    '#3db894': 'accent',  # darker green
    '#1e3a5f': 'text-background',
}

def fix_css_hardcoded_colors(content):
    """Replace hardcoded hex colors in <style> tags with CSS variables"""
    modified = content
    
    for hex_color, var_name in COLOR_MAPPINGS.items():
        # Match in CSS rules
        pattern = re.compile(r':\s*' + re.escape(hex_color) + r'\s*;', re.IGNORECASE)
        replacement = f': var(--{var_name});'
        modified = pattern.sub(replacement, modified)
    
    return modified

def fix_js_hardcoded_colors(content):
    """Replace hardcoded hex colors in JavaScript with styleConfig.getColor() calls"""
    modified = content
    
    for hex_color, var_name in COLOR_MAPPINGS.items():
        # Match in JavaScript (ctx.fillStyle = '#color', strokeStyle, etc.)
        patterns = [
            # fillStyle, strokeStyle assignments
            (r"(fillStyle|strokeStyle)\s*=\s*['\"]" + re.escape(hex_color) + r"['\"]", 
             r"\1 = styleConfig.getColor('" + var_name + "')"),
            
            # background, color in inline styles
            (r"(background|color):\s*" + re.escape(hex_color),
             r"\1: var(--" + var_name + ")"),
        ]
        
        for pattern, replacement in patterns:
            modified = re.sub(pattern, replacement, modified, flags=re.IGNORECASE)
    
    return modified

def ensure_color_scheme_loaded(content, filepath):
    """Ensure color scheme scripts are included"""
    filename = os.path.basename(filepath)
    
    # Check if already has color-schemes.css
    if 'color-schemes.css' in content:
        has_css = True
    else:
        has_css = False
        
    # Check if already has color scheme JS
    if 'color-schemes.js' in content:
        has_js = True
    else:
        has_js = False
    
    modified = content
    
    # Add CSS if missing
    if not has_css:
        # Add after first <link> or before </head>
        if '<link rel="stylesheet"' in modified:
            modified = modified.replace(
                '<link rel="stylesheet"',
                '<link rel="stylesheet" href="../css/color-schemes.css">\n    <link rel="stylesheet"',
                1
            )
        elif '</head>' in modified:
            modified = modified.replace(
                '</head>',
                '    <link rel="stylesheet" href="../css/color-schemes.css">\n</head>'
            )
    
    # Add JS if missing (before </body>)
    if not has_js and '</body>' in modified:
        # Find the last script before </body>
        body_close_pos = modified.rfind('</body>')
        if body_close_pos > 0:
            # Insert scripts before </body>
            scripts = '''    <script src="../js/color-schemes.js"></script>
    <script src="../js/style-config.js"></script>
    <script src="../js/global-scheme-config.js"></script>
'''
            modified = modified[:body_close_pos] + scripts + modified[body_close_pos:]
    
    return modified, (not has_css or not has_js)

def add_redraw_listener(content):
    """Add event listener to redraw when color scheme changes"""
    # Check if already has listener
    if 'colorSchemeChanged' in content:
        return content, False
    
    # Find the main draw/render function name
    draw_functions = re.findall(r'function\s+(draw|render|drawCanvas|update)\s*\(', content)
    if not draw_functions:
        return content, False
    
    main_draw = draw_functions[0]
    
    # Add listener before </script> tag at end
    listener_code = f'''
        // Redraw when color scheme changes
        window.addEventListener('colorSchemeChanged', {main_draw});
'''
    
    # Find last </script> before </body>
    last_script_pos = content.rfind('</script>')
    if last_script_pos > 0:
        content = content[:last_script_pos] + listener_code + content[last_script_pos:]
        return content, True
    
    return content, False

def fix_applet(filepath):
    """Fix a single applet file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Fix CSS hardcoded colors
    content = fix_css_hardcoded_colors(content)
    
    # 2. Fix JavaScript hardcoded colors
    content = fix_js_hardcoded_colors(content)
    
    # 3. Ensure color scheme files are loaded
    content, added_includes = ensure_color_scheme_loaded(content, filepath)
    
    # 4. Add redraw listener
    content, added_listener = add_redraw_listener(content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, added_includes, added_listener
    
    return False, False, False

def main():
    print("=" * 70)
    print("Fixing Hardcoded Colors in Applets")
    print("=" * 70)
    print()
    
    applet_files = [f for f in os.listdir(APPLETS_DIR) if f.endswith('.html')]
    applet_files.sort()
    
    total_fixed = 0
    
    for filename in applet_files:
        filepath = os.path.join(APPLETS_DIR, filename)
        print(f"Processing {filename}...", end=' ')
        
        try:
            was_modified, added_includes, added_listener = fix_applet(filepath)
            
            if was_modified:
                notes = []
                if added_includes:
                    notes.append("added color scheme files")
                if added_listener:
                    notes.append("added redraw listener")
                if notes:
                    print(f"✓ FIXED ({', '.join(notes)})")
                else:
                    print("✓ FIXED (color replacements)")
                total_fixed += 1
            else:
                print("→ No changes needed")
        except Exception as e:
            print(f"✗ ERROR: {e}")
    
    print()
    print("=" * 70)
    print(f"Summary: Fixed {total_fixed}/{len(applet_files)} applets")
    print("=" * 70)
    print()
    print("Next steps:")
    print("1. Hard refresh your browser (Ctrl+F5 / Cmd+Shift+R)")
    print("2. Test changing schemes in global-scheme-config.js")
    print("3. Verify all applets and quiz questions use new colors")

if __name__ == '__main__':
    main()
