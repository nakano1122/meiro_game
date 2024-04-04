<script setup lang="ts">
import { onMounted, ref } from 'vue';
import axios from 'axios';

const sampleText = ref('');

const getMaze = async () => {
  const response = await axios.get('/api/start/novice');
  console.log(response.data);
  sampleText.value = response.data;
};

onMounted(() => {
  getMaze();
});
</script>

<template>
  <h1>初級の画面です。</h1>
  <div>[[ sampleText ]]</div>
</template>

<style>

</style>