import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";
import AppTop from "@/views/AppTop.vue";
import Maze from "@/views/Maze.vue";
import Result from "@/views/Result.vue";
import Start from "@/views/Start.vue";
import Fail from "@/views/Fail.vue";

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
  },
  {
    path: "/maze/:level",
    name: "MazeStart",
    component: Maze,
    props: (routes) => {
      return {
        level: routes.params.level
      };
    },
  },
  {
    path: "/result/:level",
    name: "Result",
    component: Result,
    props: (routes) => {
      return {
        level: routes.params.level
      }
    }
  },
  {
    path: "/fail",
    name: "Fail",
    component: Fail
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routeSettings
});

export default router;