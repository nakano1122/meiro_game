<script setup lang="ts">

import type AppTop from './AppTop.vue';
</script>

<template>
    <h1>結果発表</h1>
    <RouterLink v-bind:to="{ name: 'AppTop' }">TOPに戻る</RouterLink>
</template>