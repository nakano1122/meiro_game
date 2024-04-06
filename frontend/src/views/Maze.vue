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
  <div class="game-container">
    <h1 class="title">コインを集めてゴールを目指そう！！</h1>
    <div class="status-bar">
    <div class="status-card step-limit">
      <dt>残り歩数</dt>
      <dd>[[ stepLimit ]]</dd>
    </div>
    <div class="status-card elapsed-time">
      <dt>経過時間</dt>
      <dd>[[ formatTime(elapsedTime) ]]</dd>
    </div>
  </div>
    <div class="maze-container">
      <table>
        <tr v-for="(row, rowIndex) in maze" :key="rowIndex">
          <td v-for="(cell, cellIndex) in row" :key="cellIndex" class="maze-cell">
            <div class="start" v-if="rowIndex === 7 && cellIndex === 3">スタート</div>
            <div class="goal" v-else-if="rowIndex === 0 && cellIndex === 3">ゴール</div>
            <img v-else-if="cell" src="/images/coin_image.png" alt="コイン">
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<style scoped>
.game-container {
  background-color: #3D3D3D;
  color: #ffffff;
  font-family: 'Roboto', sans-serif;
  text-align: center;
  padding: 20px;
}

.title {
  margin-bottom: 20px;
  color: #FFD700;
}

.status-bar {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.status-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 10px;
  background-color: #424242;
  border-radius: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  color: #FFFFFF;
  font-size: 1.2em;
  width: 120px;
  height: 60px;
}

.status-card dt {
  font-size: 0.8em;
  opacity: 0.7;
}

.status-card dd {
  font-size: 1.5em;
  font-weight: bold;
}

.step-limit {
  background-color: #FF8F00;
}

.elapsed-time {
  background-color: #1565C0;
}

.maze-container {
  overflow-x: auto;
}

table {
  margin: 0 auto;
}

.maze-cell {
  border: 1px solid #FFFAFA;
  width: 50px;
  height: 50px;
  background-color: #FFFAFA;
}

.start, .goal {
  color: #ffffff; /* 白色のテキスト */
  font-weight: bold; /* 太字 */
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8em;
  overflow: hidden;
  white-space: nowrap; /* 改行をさせない */
}
.start {
  background-color: #4CAF50; /* 緑色 */
}

.goal {
  background-color: #FF6347; /* 赤色 */
}

img {
  width: 40px;
  height: auto;
}
</style>