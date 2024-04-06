import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";
import AppTop from "@/views/AppTop.vue";
import Maze from "@/views/Maze.vue";
import { routes } from "vue-router/auto-routes";

const routeSettings: RouteRecordRaw[] = [
  {
    path: "/",
    name: "AppTop",
    component: AppTop
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
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routeSettings
});

export default router;