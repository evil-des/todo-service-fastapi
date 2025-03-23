<template>
  <div class="flex flex-col items-center gap-4 px-4 py-3 text-center">
    <h2 class="text-xl">Авторизация</h2>
    <auth-form button-label="Войти" auth-type="login" />
    <a
        href="#"
        @click="() => goTo(userRegisterRoute)"
        class="text-amber-600 text-opacity-60 hover:text-opacity-90 font-medium text-sm"
    >
      Нет аккаунта? Зарегистрируйтесь тут
    </a>
  </div>
</template>

<script setup lang="ts">
import AuthForm from "@/entities/user/ui/UserAuthForm.vue";
import {goTo} from "@utils/navigation.ts";
import {userRegisterRoute} from "@/pages/user/routes.ts";
</script>
