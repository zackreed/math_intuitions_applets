/**
 * Global Color Scheme Configuration
 * ===================================
 * 
 * Set the default color scheme for your entire project here.
 * This is a DEVELOPER setting, not exposed to users.
 * 
 * Usage:
 * ------
 * 1. Uncomment ONE of the options below to set your default scheme
 * 2. Include this file in your HTML AFTER style-config.js
 * 3. The scheme will be applied automatically to all pages/applets that include it
 * 
 * To override on a specific page, add to that page's script:
 * <script>styleConfig.setScheme('different_scheme');</script>
 */

// =============================================================================
// CHOOSE YOUR DEFAULT SCHEME
// =============================================================================

// Uncomment ONE line below to set the global default:

// Wait for DOM to be ready before applying scheme
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyGlobalScheme);
} else {
    applyGlobalScheme();
}

function applyGlobalScheme() {
    //styleConfig.setScheme('default');                  // Classic 3Blue1Brown style
    //styleConfig.setScheme('dark_muted_pastels');       // Modern soft pastels (RECOMMENDED)
    // styleConfig.setScheme('deep_jewel_tones');         // Sophisticated elegance
    //styleConfig.setScheme('contrasting_vibrancy');     // High energy, bold
    // styleConfig.setScheme('erau');                     // ERAU university branding
    // styleConfig.setScheme('dark');                     // Contemporary dark theme
    // styleConfig.setScheme('high_contrast');            // Maximum accessibility
    styleConfig.setScheme('warm_sunset');              // Cozy, inviting
    // styleConfig.setScheme('cool_ocean');               // Calm, professional
    // styleConfig.setScheme('forest_earth');             // Natural, grounded
}


// =============================================================================
// ADVANCED: Per-Context Configuration (Optional)
// =============================================================================

/**
 * Uncomment the code below if you want different schemes for different sections
 */

/*
(function() {
    const path = window.location.pathname;
    
    if (path.includes('/applets/')) {
        styleConfig.setScheme('dark_muted_pastels');
    } else if (path.includes('/pages/')) {
        styleConfig.setScheme('default');
    } else if (path.includes('index.html')) {
        styleConfig.setScheme('cool_ocean');
    }
})();
*/
