<script setup lang="ts">
import { onMounted, ref, onUnmounted } from 'vue';
import axios from 'axios';

interface Props {
  mode: String;
}
const props = defineProps<Props>();

const maze = ref([]);
const stepLimit = ref(0);
const elapsedTime = ref(0);
const timerId = ref();

const getMaze = async () => {
  try {
    const response = await axios.get(`/api/start/${props.mode}`);
    console.log(response.data);
    maze.value = response.data.maze;
    stepLimit.value = response.data.stepLimit;
  } catch (error) {
    console.error('APIからの迷路データの取得に失敗しました。', error);
  }
};

const startTimer = () => {
  timerId.value = setInterval(() => {
    elapsedTime.value++;
  }, 1000);
};

onMounted(() => {
  startTimer();
  getMaze();
});

onUnmounted(() => {
  if(timerId.value) {
    clearInterval(timerId.value);
  }
});

function formatTime(seconds: number) {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;
  return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
}
</script>

<template>
  <h1>コインをなるべく多く集めてゴールにたどり着こう！！</h1>
  <dl>
    <dt>残り歩数</dt>
    <dd>[[ stepLimit ]]</dd>
    <dt>経過時間</dt>
    <dd>[[ formatTime(elapsedTime) ]]</dd>
  </dl>
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
  width: 80px;
  height: auto;
  padding: 8px;
}
img {
  width: 50px;
  height: auto;
}
</style>