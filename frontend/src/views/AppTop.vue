<script setup lang="ts">
import { RouterLink } from 'vue-router';
</script>

<template>
  <h1>迷路ゲーム！！</h1>
  <h2>（挑戦者の名前）の挑戦</h2>
  <el-button type="success" plain>
    <RouterLink v-bind:to="{name: 'MazeStart', params: {mode: 'novice'}}">初級</RouterLink>
  </el-button>
  <el-button type="success" plain>
    <RouterLink v-bind:to="{name: 'MazeStart', params: {mode: 'intermediate'}}">中級</RouterLink>
  </el-button>
  <el-button type="success" plain>
    <RouterLink v-bind:to="{name: 'MazeStart', params: {mode: 'advance'}}">上級</RouterLink>
  </el-button>
</template>