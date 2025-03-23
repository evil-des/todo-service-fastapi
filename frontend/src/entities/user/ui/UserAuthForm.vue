<template>
  <div class="flex flex-col gap-3">
    <pretty-input placeholder="username" type="text" v-model="authData.username" />
    <pretty-input placeholder="password" type="password" v-model="authData.password" />
  </div>
  <pretty-button :label="buttonLabel" @click="handleAuth" />
</template>

<script setup lang="ts">
import PrettyButton from "@/features/PrettyButton.vue";
import PrettyInput from "@/features/PrettyInput.vue";
import {useUserStore} from "@/entities/user/store.ts";
import type {UserAuth} from "@/entities/user/types.ts";
import {ref} from "vue";
import {goTo} from "@utils/navigation.ts";
import {tasksListRoute} from "@/pages/task/routes.ts";

const props = defineProps<{
  buttonLabel: string;
  authType: "login" | "register";
}>();

const userStore = useUserStore();
const authData = ref<UserAuth>({
  username: "",
  password: "",
});

const handleAuth = async () => {
  try {
    await userStore.auth(props.authType, authData.value);
    await goTo(tasksListRoute);
  } catch (error) {
    console.error("Error while authenticating:", error);
  }
};
</script>
