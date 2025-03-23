import type { PrettyRouteRecord } from '@/app/router/types.ts';
import {userRoute} from "@/pages/user/routes.ts";
import {taskRoute} from "@/pages/task/routes.ts";

const mainLayoutRoute: PrettyRouteRecord = {
  name: 'main-layout',
  path: '/',
  component: () => import('@layouts/main/MainLayout.vue'),
  children: [userRoute, taskRoute],
};

export default mainLayoutRoute;
