<template>
  <div class="flex flex-col items-center gap-4 px-4 py-3 text-center w-full md:w-1/2">
    <h2 class="text-xl">Список ваших задач</h2>
    <div class="flex flex-col gap-4 w-full">
      <p class="text-lg font-bold text-indigo-400 cursor-pointer" @click="() => taskStore.addEmptyTask()">Добавить задачу +</p>
      <task-card v-for="task in tasks" :key="task.id" :task="task" />
    </div>
  </div>
</template>

<script setup lang="ts">
import TaskCard from "@/entities/task/ui/TaskCard.vue";
import {useTaskStore} from "@/entities/task/store.ts";
import {storeToRefs} from "pinia";
import {onMounted} from "vue";

const taskStore = useTaskStore();
const { tasks } = storeToRefs(taskStore);

onMounted(() => {
  taskStore.fetchTasks();
})
</script>
