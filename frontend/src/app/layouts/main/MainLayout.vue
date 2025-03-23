<template>
  <div class="p-4 flex flex-col items-center justify-center">
    <h1 class="text-2xl font-semibold">TODO Service v1.0</h1>
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router';
import '@css/main.css';
</script>
