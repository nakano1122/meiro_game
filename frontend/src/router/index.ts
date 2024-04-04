import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";
import AppTop from "@/views/AppTop.vue";
import NoviceMode from "@/views/NoviceMode.vue";
import IntermediateMode from "@/views/IntermediateMode.vue";
import AdvancedMode from "@/views/AdvancedMode.vue";

const routeSettings: RouteRecordRaw[] = [
  {
    path: "/",
    name: "AppTop",
    component: AppTop
  },
  {
    path: "/novice",
    name: "NoviceMode",
    component: NoviceMode
  },
  {
    path: "/intermediate",
    name: "IntermediateMode",
    component: IntermediateMode
  },
  {
    path: "/advance",
    name: "AdvanceMode",
    component: AdvancedMode
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routeSettings
});

export default router;