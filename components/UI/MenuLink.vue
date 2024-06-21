<template>
    <NuxtLink :to="link" class="md:mr-6 max-md:justify-center flex items-center gap-2 border border p-2 rounded-xl hover:bg-slate-200"><Icon size="24px" :name="icon"/><span class="max-md:hidden">{{ title }}</span></NuxtLink>
</template>
<script setup>
defineProps({
    title:'',
    icon:'',
    link:''
})
</script>