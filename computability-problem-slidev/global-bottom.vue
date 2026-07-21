<!-- Persistent footer on every slide but the title. Slidev's equivalent of
     Marp's `footer:` frontmatter — see @slidev/cli skills/references/layout-global-layers.md -->
<template>
  <footer
    v-if="$nav.currentPage > 1"
    class="absolute bottom-0 left-0 right-0 p-3 text-xs opacity-50 text-center"
  >
    felipe@felipevr.com ― github.com/fbidu
  </footer>
</template>
