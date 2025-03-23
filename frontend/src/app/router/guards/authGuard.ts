import {ACCESS_TOKEN_SESSION_STORAGE_KEY} from '@/shared/api/utils.ts';
import {userLoginRoute, userRegisterRoute} from "@/pages/user/routes.ts";
import type {PrettyRouteRecord} from "@/app/router/types.ts";
import {tasksListRoute} from "@/pages/task/routes.ts";

const authGuard = async (
    to: PrettyRouteRecord,
): Promise<boolean | PrettyRouteRecord> => {
  const isAuthenticated = !!sessionStorage.getItem(ACCESS_TOKEN_SESSION_STORAGE_KEY);
  if (to.path === "/" + userLoginRoute.path || to.path === "/" + userRegisterRoute.path) return true;

  if (to.meta?.requiresAuth && !isAuthenticated) {
    return userLoginRoute;
  } else if (to.path === "/" + userLoginRoute.path && isAuthenticated) {
    return tasksListRoute;
  }

  return true;
}

export default authGuard;
