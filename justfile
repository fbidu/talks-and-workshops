# Talk tooling. Run `just` (no args) to list recipes.
# Talks are npm workspaces, so one `npm install` at the root covers all of them.

default:
    @just --list

# Scaffold a new talk from the Slidev template
new talk:
    @test ! -e {{talk}} || { echo "error: {{talk}} already exists"; exit 1; }
    cp -R .template-slidev {{talk}}
    cd {{talk}} && npm pkg set name={{talk}}
    npm install
    @echo "created {{talk}} -- run: just dev {{talk}}"

# Install dependencies for every talk
install:
    npm install

# Live-preview a talk with hot reload
dev talk:
    npm run dev -w {{talk}}

# Build a talk to <talk>/dist
build talk:
    npm run build -w {{talk}}

# Export a talk to PDF
pdf talk:
    npm run export -w {{talk}}

# Format everything Prettier is allowed to touch
format:
    npm run format

# Run every pre-commit hook against the whole repo
lint:
    prek run --all-files
