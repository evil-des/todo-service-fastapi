import type { PrettyRouteRecord } from '@/app/router/types.ts';
import router from '@/app/router';

export const goTo = async (
  to: PrettyRouteRecord,
  params?: Record<string, string | number>
): Promise<boolean> => {
  if (!to.name) return false;
  await router.push({ name: to.name, params });
  return true;
};

export const goToExternal = async (url: string, newWindow: boolean = true) => {
  window.open(url, newWindow ? '_blank' : '_self');
};
