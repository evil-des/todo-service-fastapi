import type { NavigationGuardWithThis, RouteRecordRaw } from 'vue-router';
import { createRouter, createWebHistory } from 'vue-router';
import mainLayoutRoute from '@layouts/main/routes';
import userGuard from "@/app/router/guards/userGuard.ts";
import authGuard from "@/app/router/guards/authGuard.ts";

const router = createRouter({
  // @ts-ignore
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [mainLayoutRoute as RouteRecordRaw],
});

// !ORDER IS IMPORTANT!
router.beforeEach(authGuard as NavigationGuardWithThis<undefined>);
router.beforeEach(userGuard);

export default router;
