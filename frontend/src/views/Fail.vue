<script setup lang="ts">
import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="sorry-container">
      <h1>残念...</h1>
      <p>また挑戦してね！</p>
      <RouterLink v-bind:to="{name: 'Start'}" class="router-link">気を取り直して挑戦！！</RouterLink>
    </div>
  </template> 

<style scoped>
.sorry-container {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  background-color: #2c3e50;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
  color: #ecf0f1;
}

h1 {
  color: #c0392b;
  margin-bottom: 15px;
}

p {
  margin-bottom: 30px;
}

.router-link {
  padding: 10px 20px;
  background-color: #34495e;
  color: #ecf0f1;
  border: none;
  border-radius: 4px;
  text-decoration: none;
  font-size: 1rem;
  transition: background-color 0.3s;
}

.router-link:hover {
  background-color: #4a69bd;
}
</style>