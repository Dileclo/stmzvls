<script setup lang="ts">
import { MENU } from '~/data/menu';
</script>

<template>
    <div class="flex flex-col gap-2 max-md:mx-3  md:ml-6">
        <UIMenuLink v-for="i in MENU" :title="i.title" :link="i.link" :icon="i.icon"></UIMenuLink>
    </div>
</template>
<style scoped>
.router-link-active{
    @apply border-blue-400 border-2
}
</style>