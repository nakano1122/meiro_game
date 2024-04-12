import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";
import AppTop from "@/views/AppTop.vue";
import Maze from "@/views/Maze.vue";
import Result from "@/views/Result.vue";
import Start from "@/views/Start.vue";

const routeSettings: RouteRecordRaw[] = [
  {
    path: "/",
    name: "Start",
    component: Start
  },
  {
    path: "/TOP",
    name: "AppTop",
    component: AppTop,
    props: (routes) => {
      return {
        username: routes.params.username
      };
    },
  },
  {
    path: "/maze/:mode",
    name: "MazeStart",
    component: Maze,
    props: (routes) => {
      return {
        mode: routes.params.mode
      };
    },
  },
  {
    path: "/result",
    name: "Result",
    component: Result
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routeSettings
});

export default router;