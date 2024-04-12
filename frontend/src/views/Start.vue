<script setup lang="ts">
import router from '@/router';
import axios from 'axios';
import { ref } from 'vue';
const username = ref('');

const onFormSubmit = async (): Promise<void> => {
  try {
    const response = await axios.post('/api/addUser', {
      name: username.value
    });
    router.push({ name: 'AppTop', query: { username: username.value } });
  } catch (error) {
    console.error('データ登録に失敗しました。', error);
  }
};

</script>

<template>
    <div class="form-container">
        <p class="title">ボーナスステージにようこそ！</p>
        <form action="#" v-on:submit.prevent="onFormSubmit">
            <input type="text" name="name" v-model="username" placeholder="あなたの名前" required>
            <button type="submit">挑戦する</button>
        </form>
        <p>挑戦者: [[ username ]]</p>
    </div>
</template>

<style scoped>
.form-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  background-color: #2c3e50;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  color: #ecf0f1;
}

form {
  display: flex;
  flex-direction: column;
}

input[type="text"] {
  padding: 10px;
  margin-bottom: 20px;
  border-radius: 4px;
  border: none;
  outline: none;
  font-size: 16px;
}

button[type="submit"] {
  padding: 10px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

button[type="submit"]:hover {
  background-color: #2980b9;
}

p {
  text-align: center;
  margin-top: 20px;
  font-size: 18px;
}

.title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 24px;
  color: #f39c12;
}
</style>
