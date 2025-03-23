<template>
  <div
      class="rounded-xl py-3 px-6 bg-amber-100
      hover:bg-amber-200 text-gray-800 font-medium cursor-pointer"
  >
    <p>{{label}}</p>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  label: string;
}>();
</script>
