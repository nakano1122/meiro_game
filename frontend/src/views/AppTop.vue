<script setup lang="ts">
import { inject } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserStore } from '@/stores/userStore';

const userStore = useUserStore();
const username = userStore.username;
</script>

<template>
  <div class="game-intro-container">
    <h1>迷路ゲーム！！</h1>
    <h2>[[ username ]]の挑戦</h2>
    <el-button type="success" plain>
      <RouterLink v-bind:to="{name: 'MazeStart', params: {mode: 'novice'}}">初級</RouterLink>
    </el-button>
    <el-button type="success" plain>
      <RouterLink v-bind:to="{name: 'MazeStart', params: {mode: 'intermediate'}}">中級</RouterLink>
    </el-button>
    <el-button type="success" plain>
      <RouterLink v-bind:to="{name: 'MazeStart', params: {mode: 'advance'}}">上級</RouterLink>
    </el-button>
  </div>
</template>

<style scoped>
.game-intro-container {
  text-align: center;
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  background-color: #34495e;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  color: #ecf0f1;
}

h1 {
  color: #e74c3c;
  margin-bottom: 20px;
}

h2 {
  color: #f39c12;
  margin-bottom: 40px;
}

.el-button {
  margin: 10px;
  border-color: #e74c3c;
  color: #ecf0f1;
  font-weight: bold;
}

.router-link-active {
  color: #e74c3c;
}
</style>
