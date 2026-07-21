<!-- Persistent footer on every slide but the title. Slidev's equivalent of
     Marp's `footer:` frontmatter.

     Deliberately slide-bottom rather than global-bottom: global layers render
     once, outside the transition group, so they sit still while slides move
     past them. A per-slide layer renders inside each slide and travels with it.

     $page is this slide's own number, not the deck's current page — during a
     transition both slides are mounted, and the global page counter has
     already advanced, which would flash the footer onto the outgoing title. -->
<script setup>
import { useSlideContext } from "@slidev/client";

const { $page: page } = useSlideContext();
</script>

<template>
  <footer
    v-if="page > 1"
    class="absolute bottom-0 left-0 right-0 p-3 text-xs opacity-50 text-center"
  >
    felipe@felipevr.com ― github.com/fbidu
  </footer>
</template>
