<script setup lang="ts">
import { onMounted, ref } from 'vue';
import axios from 'axios';

const maze = ref([]);
const getMaze = async () => {
  try {
    const response = await axios.get('/api/start/novice');
    maze.value = response.data;
  } catch (error) {
    console.error('APIからの迷路データの取得に失敗しました。', error);
  }
};

onMounted(() => {
  getMaze();
});
</script>

<template>
  <h1>コインをなるべく多く集めてゴールにたどり着こう！！</h1>
  <table>
    <tr v-for="(row, rowIndex) in maze" v-bind:key="rowIndex">
      <td v-for="(cell, cellIndex) in row" v-bind:key="cellIndex">
        <div v-if="rowIndex == 7 && cellIndex == 3">スタート</div>
        <div v-else-if="rowIndex == 0 && cellIndex == 3">ゴール</div>
        <img v-else-if="cell" src="/images/coin_image.png" alt="コイン">
      </td>
    </tr>
  </table>
</template>

<style>
td {
  border: 1px solid #000;
  padding: 8px;
}
img {
  width: 50px;
  height: auto;
}
</style>