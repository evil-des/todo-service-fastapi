import type { PrettyRouteRecord } from '@/app/router/types.ts';

export const userRegisterRoute: PrettyRouteRecord = {
  path: 'register',
  name: 'register',
  component: () => import('@/pages/user/UserRegisterPage.vue'),
};

export const userLoginRoute: PrettyRouteRecord = {
  path: 'login',
  name: 'login',
  component: () => import('@/pages/user/UserLoginPage.vue'),
};

export const userRoute: PrettyRouteRecord = {
  path: '',
  name: 'user',
  children: [userRegisterRoute, userLoginRoute]
};
