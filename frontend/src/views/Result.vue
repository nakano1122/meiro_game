<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';

interface Props {
    mode: String;
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
        const response = await axios.get('/api/result');
        results.value = response.data.results.map((item: any) => ({
            result_id: item.result_id,
            username: item.username,
            level: item.level,
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
</script>

<template>
    <h1>結果発表</h1>
    <table>
        <tr v-for="(result, resultIndex) in results">
            <td>[[ resultIndex+1 ]]位</td>
            <td>[[ result.username ]]</td>
            <td>[[ result.clear_time ]]</td>
            <td>[[ result.collected_coins ]]</td>
            <td>[[ result.timestamp ]]</td>
        </tr>
    </table>
    <RouterLink v-bind:to="{ name: 'Start' }">スタート画面に戻る</RouterLink>
</template>