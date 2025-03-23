import type { RouteRecordRaw } from 'vue-router';

interface PrettyMeta {
  requiresAuth: boolean;
}

export interface PrettyRouteRecord
  extends Omit<RouteRecordRaw, 'meta' | 'children'> {
  name: string;
  meta?: PrettyMeta;
  children?: PrettyRouteRecord[];
}
