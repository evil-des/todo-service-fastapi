import type { PrettyRouteRecord } from '@/app/router/types.ts';

export const tasksListRoute: PrettyRouteRecord = {
  path: 'tasks-list',
  name: 'tasks-list',
  meta: {
    requiresAuth: true,
  },
  component: () => import('@/pages/task/TaskListPage.vue'),
};

export const taskRoute: PrettyRouteRecord = {
  path: '',
  name: 'tasks',
  children: [tasksListRoute]
};
