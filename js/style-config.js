/**
 * Style Configuration System
 * ===========================
 * 
 * Developer-only color scheme management for applets and pages.
 * This is NOT a user-facing feature - schemes are set in code only.
 * 
 * Usage:
 * ------
 * 1. Include this file after color-schemes.js in your HTML
 * 2. Set scheme globally: In global-scheme-config.js or page script
 * 3. Get colors in JavaScript: styleConfig.getColor('highlight')
 * 
 * To change the global scheme:
 * - Edit js/global-scheme-config.js, OR
 * - Add to your page: <script>styleConfig.setScheme('dark_muted_pastels');</script>
 * 
 * Features:
 * ---------
 * - Global scheme selection (applies to entire page)
 * - Per-element scheme overrides
 * - Easy color access in JavaScript
 * - Fallback to default scheme
 */

class StyleConfig {
    constructor() {
        this.DEFAULT_SCHEME = 'default';
        this.currentScheme = this.DEFAULT_SCHEME;
    }
    
    /**
     * Get list of all available color schemes
     */
    getAvailableSchemes() {
        return Object.keys(COLOR_SCHEMES);
    }
    
    /**
     * Get the currently active global scheme name
     */
    getCurrentScheme() {
        return this.currentScheme;
    }
    
    /**
     * Set global color scheme for the entire page/applet
     * @param {string} schemeName - Name of the color scheme to apply
     */
    setScheme(schemeName) {
        if (!COLOR_SCHEMES[schemeName]) {
            console.warn(`Color scheme '${schemeName}' not found. Using '${this.DEFAULT_SCHEME}'.`);
            schemeName = this.DEFAULT_SCHEME;
        }
        
        this.currentScheme = schemeName;
        
        // Apply to document root
        document.documentElement.setAttribute('data-color-scheme', schemeName);
        
        // Also apply to body for backward compatibility
        document.body.setAttribute('data-color-scheme', schemeName);
        
        // Dispatch custom event for listeners (e.g., canvas redraw)
        window.dispatchEvent(new CustomEvent('colorSchemeChanged', {
            detail: { scheme: schemeName }
        }));
        
        console.log(`Color scheme set to: ${schemeName}`);
    }
    
    /**
     * Set color scheme for a specific element (advanced use)
     * @param {HTMLElement} element - The element to apply the scheme to
     * @param {string} schemeName - Name of the color scheme
     */
    setElementScheme(element, schemeName) {
        if (!COLOR_SCHEMES[schemeName]) {
            console.warn(`Color scheme '${schemeName}' not found.`);
            return;
        }
        
        element.setAttribute('data-color-scheme', schemeName);
    }
    
    /**
     * Get a color value from the current scheme
     * @param {string} colorKey - The color key (e.g., 'highlight', 'background')
     * @param {string} schemeName - Optional: use a specific scheme instead of current
     * @returns {string} The hex color value
     */
    getColor(colorKey, schemeName = null) {
        const scheme = schemeName || this.currentScheme;
        return COLOR_SCHEMES[scheme]?.[colorKey] || '#000000';
    }
    
    /**
     * Get all colors from the current scheme
     * @param {string} schemeName - Optional: use a specific scheme instead of current
     * @returns {object} Object containing all colors
     */
    getColors(schemeName = null) {
        const scheme = schemeName || this.currentScheme;
        return COLOR_SCHEMES[scheme] || COLOR_SCHEMES[this.DEFAULT_SCHEME];
    }
    
    /**
     * Convert hex color to RGB array [r, g, b] with values 0-255
     * @param {string} hex - Hex color string
     * @returns {array} RGB values
     */
    hexToRGB(hex) {
        const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? [
            parseInt(result[1], 16),
            parseInt(result[2], 16),
            parseInt(result[3], 16)
        ] : [0, 0, 0];
    }
    
    /**
     * Convert hex color to RGB array [r, g, b] with values 0-1 (for canvas)
     * @param {string} hex - Hex color string
     * @returns {array} Normalized RGB values
     */
    hexToRGBNormalized(hex) {
        const rgb = this.hexToRGB(hex);
        return rgb.map(v => v / 255);
    }
    
    /**
     * Get a CSS variable value
     * @param {string} varName - CSS variable name (with or without --)
     * @returns {string} The CSS variable value
     */
    getCSSVariable(varName) {
        if (!varName.startsWith('--')) {
            varName = '--' + varName;
        }
        return getComputedStyle(document.documentElement).getPropertyValue(varName).trim();
    }
    
    /**
     * Reset to default scheme
     */
    reset() {
        this.setScheme(this.DEFAULT_SCHEME);
    }
}

// Create global instance
const styleConfig = new StyleConfig();

// Export for use in modules or global scope
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { StyleConfig, styleConfig };
}
