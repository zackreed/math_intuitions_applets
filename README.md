# Math Intuitions Applets

A collection of interactive applets for learning mathematical concepts.

## Structure

- `index.html`: Landing page listing all available walkthroughs.
- `pages/`: Contains the walkthrough pages (e.g., `svd-walkthrough.html`).
- `applets/`: Contains the standalone interactive applets (e.g., `vector-projection-applet.html`).
- `css/`: Shared stylesheets (`styles.css`).
- `js/`: Shared JavaScript utilities and logic (`quiz.js`, `utils.js`).

## Available Applets

### Singular Value Decomposition (SVD)
- **Walkthrough**: [SVD Walkthrough](pages/svd-walkthrough.html)
- **Applet**: [Vector Projection Applet](applets/vector-projection-applet.html)

## Contributing

To add a new applet:
1. Create the applet HTML file in `applets/`.
2. Create a walkthrough page in `pages/` linking to the applet.
3. Add a link to the walkthrough in `index.html`.
