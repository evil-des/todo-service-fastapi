<template>
  <input
      :type="type"
      :placeholder="placeholder"
      class="rounded-xl p-3"
      v-model="model"
  >
</template>

<script setup lang="ts">
defineProps<{
  type: string;
  placeholder: string;
}>();

const model = defineModel<string>();
</script>
