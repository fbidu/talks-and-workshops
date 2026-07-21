# Talk rendering tasks. Run `just` (no args) to list recipes.
# Usage: just <recipe> <talk-folder>   e.g.  just build computability-problem

default:
    @just --list

# --- Marp (text-first, self-contained single HTML) ---

# Build a Marp talk to a self-contained <talk>/index.html
build talk:
    npx -y @marp-team/marp-cli@latest {{talk}}/slides.md -o {{talk}}/index.html --html

# Live-preview a Marp talk with hot reload (http://localhost:8080)
preview talk:
    npx -y @marp-team/marp-cli@latest -s {{talk}}

# Export a Marp talk to PDF
pdf talk:
    npx -y @marp-team/marp-cli@latest {{talk}}/slides.md -o {{talk}}/slides.pdf --allow-local-files

# Render a Mermaid diagram (.mmd) to a self-contained SVG via Kroki (build-time only)
diagram src out:
    curl -sf -X POST https://kroki.io/mermaid/svg -H "Content-Type: text/plain" --data-binary @{{src}} -o {{out}}

# --- Slidev (Vue-based, richer: mermaid, layouts, animations) ---

# Install a Slidev talk's dependencies
slidev-install talk:
    cd {{talk}} && npm install

# Dev server for a Slidev talk
slidev-dev talk:
    cd {{talk}} && npm run dev

# Build a Slidev talk to <talk>/dist (static site)
slidev-build talk:
    cd {{talk}} && npm run build

# Export a Slidev talk to PDF
slidev-pdf talk:
    cd {{talk}} && npm run export
