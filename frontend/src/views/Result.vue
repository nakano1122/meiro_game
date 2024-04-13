<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';

interface Props {
    level: String;
}
const props = defineProps<Props>();

interface Result {
    result_id: number;
    username: string;
    level: number;
    clear_time: number;
    collected_coins: number;
    timestamp: Date;
}
const results = ref<Result[]>([]);

const getRanking = async () => {
    try {
        const response = await axios.get(`/api/result/${props.level}`);
        console.log(response.data.results);
        results.value = response.data.results.map((item: any) => ({
            result_id: item.result_id,
            username: item.username,
            clear_time: item.clear_time,
            collected_coins: item.collected_coins,
            timestamp: new Date(item.timestamp)
        }));
    } catch (error) {
        console.error('データの取得に失敗しました。', error);
    }
}

onMounted(() => {
    getRanking();
});

function formatTime(seconds: number) {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;
  return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
}
</script>

<template>
    <h1>結果発表</h1>
    <table>
        <tr>
            <th></th>
            <th>ユーザー名</th>
            <th>獲得コイン数</th>
            <th>クリアタイム</th>
        </tr>
        <tr v-for="(result, resultIndex) in results">
            <td>[[ resultIndex+1 ]]位</td>
            <td>[[ result.username ]]</td>
            <td class="coins-collected">[[ result.collected_coins ]]枚</td>
            <td>[[ formatTime(result.clear_time) ]]</td>
        </tr>
    </table>
    <RouterLink v-bind:to="{ name: 'Start' }">スタート画面に戻る</RouterLink>
</template>

<style scoped>
.results-container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  background-color: #34495e;
  color: #ecf0f1;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
}

h1 {
  color: #e74c3c;
  margin-bottom: 20px;
}

table {
  width: 100%;
  margin: 20px 0;
  border-collapse: collapse;
  background-color: #2c3e50;
  color: #ecf0f1;
}

th, td {
  padding: 10px;
  border: 1px solid #34495e;
  text-align: center;
}

th {
  background-color: #3c6e71;
}

td {
  background-color: #35524a;
}

.coins-collected {
  font-weight: bold;
  font-size: 1.2em;
  color: #f1c40f;
  background-color: #2a2f36;
  box-shadow: inset 0 0 10px #f39c12;
  text-align: center;
}


.router-link {
  padding: 10px 20px;
  margin-top: 20px;
  background-color: #2c3e50;
  color: #ecf0f1;
  text-decoration: none;
  border-radius: 4px;
  display: inline-block;
  transition: background-color 0.3s;
}

.router-link:hover {
  background-color: #2a80b9;
}

h1, h2, th, td, .router-link {
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
}

@media (max-width: 600px) {
  .coins-collected {
    font-size: 1em;
  }
}
</style>