<script setup lang="ts">
import { onMounted, ref, onUnmounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();

interface Props {
  mode: String;
}
const props = defineProps<Props>();

const maze = ref<boolean[][]>([]);
const stepLimit = ref(0);
const collectedCoins = ref(0);
const elapsedTime = ref(0);
const timerId = ref();
const characterPosition = ref({ x: 7, y: 3 });
const collectedCoinsPositions = ref<Array<{ x: number, y: number }>>([]);

const getMaze = async () => {
  try {
    const response = await axios.get(`/api/start/${props.mode}`);
    maze.value = response.data.maze as boolean[][];
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

const moveCharacter = (direction: string): void => {
  const maxX = maze.value.length - 1;
  const maxY = maze.value[0].length - 1;
  switch (direction) {
    case 'ArrowUp':
      characterPosition.value.x = Math.max(characterPosition.value.x - 1, 0);
      break;
    case 'ArrowDown':
      characterPosition.value.x = Math.min(characterPosition.value.x + 1, maxX);
      break;
    case 'ArrowLeft':
      characterPosition.value.y = Math.max(characterPosition.value.y - 1, 0);
      break;
    case 'ArrowRight':
      characterPosition.value.y = Math.min(characterPosition.value.y + 1, maxY);
      break;
  }

  if (maze.value[characterPosition.value.x][characterPosition.value.y] === true) {
    collectedCoins.value++;
    collectedCoinsPositions.value.push({ x: characterPosition.value.x, y: characterPosition.value.y });
  }
};

const isCharacterCell = (rowIndex: number, cellIndex: number) => {
  return characterPosition.value.x === rowIndex && characterPosition.value.y === cellIndex;
}

const onAnimationEnd = (x: number, y: number) => {
  maze.value[x][y] = false;
  collectedCoinsPositions.value = collectedCoinsPositions.value.filter(pos => pos.x !== x || pos.y !== y);
};

const handleKeyDown = (event: KeyboardEvent): void => {
  if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(event.key)) {
    moveCharacter(event.key);
    stepLimit.value--;
    if ((characterPosition.value.x === 0 && characterPosition.value.y === 3 || stepLimit.value === 0)) {
      router.push({ name: 'Result' });
    }
  }
};

onMounted(() => {
  startTimer();
  getMaze();
  window.addEventListener('keydown', handleKeyDown);
});

onUnmounted(() => {
  if (timerId.value) {
    clearInterval(timerId.value);
  }
  window.removeEventListener('keydown', handleKeyDown);
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
      <div class="status-card step-limit">
        <dt>獲得コイン数</dt>
        <dd>[[ collectedCoins ]]</dd>
      </div>
      <div class="status-card elapsed-time">
        <dt>経過時間</dt>
        <dd>[[ formatTime(elapsedTime) ]]</dd>
      </div>
    </div>
    <div class="maze-container">
      <table>
        <tr v-for="(row, rowIndex) in maze" v-bind:key="rowIndex">
          <td v-for="(cell, cellIndex) in row" v-bind:key="cellIndex" class="maze-cell"
            v-bind:class="{ 'character-cell': isCharacterCell(rowIndex, cellIndex) }">
            <div class="start" v-if="rowIndex === 7 && cellIndex === 3">スタート</div>
            <div class="goal" v-else-if="rowIndex === 0 && cellIndex === 3">ゴール</div>
            <img v-else-if="cell" src="/images/coin_image.png" alt="コイン" class="coin"
              v-bind:class="{ 'get-coin': collectedCoinsPositions.some(pos => pos.x === rowIndex && pos.y === cellIndex) }"
              v-on:animationend="onAnimationEnd(rowIndex, cellIndex)">
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

.character-cell {
  background-image: url('/images/stop_man.png');
  background-size: cover;
  position: relative;
  z-index: 100;
}

.start,
.goal {
  color: #ffffff;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8em;
  overflow: hidden;
  white-space: nowrap;
  position: relative;
  z-index: 80;
}

.start {
  background-color: #4CAF50;
}

.goal {
  background-color: #FF6347;
}

.coin {
  position: relative;
  z-index: 50;
}

@keyframes bounce {
  0% {
    transform: translateY(0);
    opacity: 1;
  }

  50% {
    transform: translateY(-20px);
    opacity: 1;
  }

  100% {
    transform: translateY(0);
    opacity: 0;
  }
}

.get-coin {
  animation: bounce 0.5s ease-out;
}

img {
  width: 40px;
  height: auto;
}
</style>