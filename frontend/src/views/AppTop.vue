<script setup lang="ts">
import { RouterLink } from 'vue-router';

</script>

<template>
  <h1>迷路ゲーム！！</h1>
  <h2>（挑戦者の名前）の挑戦</h2>
  <RouterLink v-bind:to="{name: 'NoviceMode'}">初級</RouterLink>
  <RouterLink v-bind:to="{name: 'IntermediateMode'}">中級</RouterLink>
  <RouterLink v-bind:to="{name: 'AdvanceMode'}">上級</RouterLink>
</template>