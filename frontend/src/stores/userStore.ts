import { defineStore } from "pinia";

export const useUserStore = defineStore('user', {
  state: () => ({
    username: ''
  }),
  actions: {
    setUsername(newName: string) {
      this.username = newName;
    }
  }
});