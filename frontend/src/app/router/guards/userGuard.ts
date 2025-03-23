import { useUserStore } from '@/entities/user/store.ts';

const userGuard = async () => {
  const store = useUserStore();
  if (store.isAuthenticated) await store.fetch();
};

export default userGuard;
