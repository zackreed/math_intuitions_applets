/**
 * Global Color Scheme Configuration
 * ===================================
 * 
 * Use this file to set project-wide color scheme defaults.
 * Include this file AFTER style-config.js to override the default scheme.
 * 
 * Usage:
 * ------
 * 1. Uncomment one of the preset configurations below, or
 * 2. Create your own custom configuration
 * 3. Include in your HTML: <script src="../js/global-scheme-config.js"></script>
 */

// =============================================================================
// PRESET CONFIGURATIONS
// =============================================================================

// Option 1: Use default (classic 3Blue1Brown style)
// No configuration needed - this is the default

// Option 2: Modern soft pastels (recommended for general use)
styleConfig.setGlobalScheme('dark_muted_pastels', false);

// Option 3: ERAU branding (for university content)
// styleConfig.setGlobalScheme('erau', false);

// Option 4: High contrast (for accessibility)
// styleConfig.setGlobalScheme('high_contrast', false);

// Option 5: Cool ocean theme (calm, professional)
// styleConfig.setGlobalScheme('cool_ocean', false);

// =============================================================================
// ACTIVE CONFIGURATION
// =============================================================================

// Uncomment the line below to set your preferred default scheme
// Replace 'default' with any scheme name from COLOR_SCHEME_QUICK_REF.md

// styleConfig.setGlobalScheme('default', false);


// =============================================================================
// ADVANCED: Per-Context Configuration
// =============================================================================

/**
 * You can also set different schemes based on the current page/context:
 */

/*
// Detect page type and apply appropriate scheme
(function() {
    const path = window.location.pathname;
    
    if (path.includes('/applets/')) {
        // All applets use dark muted pastels
        styleConfig.setGlobalScheme('dark_muted_pastels', false);
    } else if (path.includes('/pages/')) {
        // Walkthrough pages use default scheme
        styleConfig.setGlobalScheme('default', false);
    } else if (path.includes('index.html')) {
        // Home page uses cool ocean
        styleConfig.setGlobalScheme('cool_ocean', false);
    }
    // If none match, use whatever was saved in localStorage
})();
*/


// =============================================================================
// NOTES
// =============================================================================

/**
 * The second parameter (false) prevents saving to localStorage.
 * This means:
 * - The scheme is set on page load
 * - User selections are still saved and respected
 * - Next time user visits, their saved preference will be used
 * 
 * If you want to FORCE a scheme (ignore user preferences):
 * styleConfig.setGlobalScheme('my_scheme', true);
 * 
 * Then remove the scheme selector from your pages to prevent users from changing it.
 */
