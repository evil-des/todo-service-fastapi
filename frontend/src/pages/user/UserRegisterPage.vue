<template>
  <div class="flex flex-col items-center gap-4 px-4 py-3 text-center">
    <h2 class="text-xl">Регистрация</h2>
    <auth-form button-label="Создать аккаунт" auth-type="register" />
    <a
        href="#"
        @click="() => goTo(userLoginRoute)"
        class="text-amber-600 text-opacity-60 hover:text-opacity-90 font-medium text-sm"
    >
      Есть аккаунт? Войдите тут
    </a>
  </div>
</template>

<script setup lang="ts">
import AuthForm from "@/entities/user/ui/UserAuthForm.vue";
import {goTo} from "@utils/navigation.ts";
import {userLoginRoute} from "@/pages/user/routes.ts";
</script>
