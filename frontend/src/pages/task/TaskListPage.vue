<template>
  <div class="flex flex-col items-center gap-4 px-4 py-3 text-center w-full md:w-1/2">
    <h2 class="text-xl">Список ваших задач</h2>
    <!-- Контролы фильтрации и сортировки -->
    <div class="flex gap-4 mb-4">
      <!-- Фильтр по статусу -->
      <select v-model="selectedStatus" class="p-2 border rounded">
        <option value="">Все статусы</option>
        <option value="NOT_COMPLETED">Не выполнено</option>
        <option value="COMPLETED">Выполнено</option>
      </select>
      <!-- Сортировка по дате создания -->
      <select v-model="selectedSort" class="p-2 border rounded">
        <option value="desc">Дата создания: по убыванию</option>
        <option value="asc">Дата создания: по возрастанию</option>
      </select>
    </div>
    <div class="flex flex-col gap-4 w-full">
      <p class="text-lg font-bold text-indigo-400 cursor-pointer" @click="addTask">Добавить задачу +</p>
      <task-card v-for="task in filteredTasks" :key="task.id" :task="task" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { storeToRefs } from 'pinia';
import TaskCard from '@/entities/task/ui/TaskCard.vue';
import { useTaskStore } from '@/entities/task/store';

const taskStore = useTaskStore();
const { tasks } = storeToRefs(taskStore);

const selectedStatus = ref("");
const selectedSort = ref("desc");

const filteredTasks = computed(() => {
  let filtered = tasks.value ? [...tasks.value] : [];
  if (selectedStatus.value) {
    filtered = filtered.filter(task => task.status === selectedStatus.value);
  }
  filtered.sort((a, b) => {
    const dateA = new Date(a.createdAt);
    const dateB = new Date(b.createdAt);
    return selectedSort.value === "asc"
        ? dateA.getTime() - dateB.getTime()
        : dateB.getTime() - dateA.getTime();
  });
  return filtered;
});

const addTask = () => {
  taskStore.addEmptyTask();
};

onMounted(() => {
  taskStore.fetchTasks();
});
</script>
