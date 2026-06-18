# Marp talk template

A starter for text-based slide decks built with [Marp](https://marp.app/).
Write Markdown in `slides.md`, then build a single self-contained `index.html`
that drops straight onto GitHub Pages — no submodule, no runtime dependencies.

## Create a new talk from this template

```sh
cp -r template my-new-talk
cd my-new-talk
$EDITOR slides.md
```

## Preview while writing

```sh
npx -y @marp-team/marp-cli@latest -s .
# then open http://localhost:8080
```

Or use the "Marp for VS Code" extension for live preview.

## Build for publishing

```sh
npx -y @marp-team/marp-cli@latest slides.md -o index.html --html
```

The output is one self-contained `index.html` (theme CSS inlined). Export to
other formats from the same source:

```sh
npx -y @marp-team/marp-cli@latest slides.md -o slides.pdf
npx -y @marp-team/marp-cli@latest slides.md -o slides.pptx
```

## Markdown cheatsheet

- `---` alone on a line = new slide
- Front-matter at the top of the file sets `theme`, `paginate`, `footer`, …
- `<!-- _class: lead -->` centers a slide (great for title / closing)
- `<!-- a comment -->` becomes a presenter note
- Per-slide directives start with `_` (e.g. `<!-- _paginate: false -->`)

More in the [Marpit Markdown docs](https://marpit.marp.app/markdown).
