<template>
  <div class="p-4 flex flex-col items-center justify-center">
    <div class="flex gap-6">
      <h1 class="text-2xl font-semibold">TODO Service v1.0</h1>
      <a
          href="#"
          v-if="isAuthenticated"
          class="text-sm font-medium"
          @click="onLogoutClick"
      >
        Выйти
      </a>
    </div>
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router';
import '@css/main.css';
import {useUserStore} from "@/entities/user/store.ts";
import {storeToRefs} from "pinia";
import {goTo} from "@utils/navigation.ts";
import {userLoginRoute} from "@/pages/user/routes.ts";

const userStore = useUserStore();
const { isAuthenticated } = storeToRefs(userStore);

const onLogoutClick = () => {
  userStore.logout();
  goTo(userLoginRoute);
}
</script>
