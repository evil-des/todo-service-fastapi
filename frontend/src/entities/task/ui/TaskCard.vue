<template>
  <div class="flex justify-between items-start gap-4 text-left rounded-2xl p-6 bg-white shadow-sm w-full">
    <div class="flex flex-col flex-1 min-w-0">
      <input
          type="text"
          class="text-xl font-semibold mb-2 w-full"
          v-model="editedTask.name"
          placeholder="Введите название задачи"
          @input="onInputChange"
      >
      <textarea
          class="text-sm resize-none w-full h-auto min-h-[100px] max-h-[400px] overflow-y-auto"
          v-model="editedTask.description"
          placeholder="Описание задачи"
          @input="onInputChange"
      />
    </div>
    <div class="flex flex-col gap-2 font-medium shrink-0 text-right">
      <p v-if="isModified" class="text-green-600 cursor-pointer" @click="saveChanges">Сохранить</p>
      <p class="text-red-500 cursor-pointer" @click="handleDelete">Удалить</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import type { Task } from "@/entities/task/types";
import { useTaskStore } from "@/entities/task/store";

const props = defineProps<{ task: Task }>();

const editedTask = ref({ ...props.task });
const isModified = ref(false);

const onInputChange = () => {
  isModified.value = editedTask.value.name !== props.task.name ||
      editedTask.value.description !== props.task.description;
};

const taskStore = useTaskStore();

const saveChanges = async () => {
  if (editedTask.value.id < 0) {
    await taskStore.saveNewTask(editedTask.value);
    isModified.value = false;
    return
  }
  await taskStore.updateTask(editedTask.value.id, {
    name: editedTask.value.name,
    description: editedTask.value.description,
  });
  isModified.value = false;
};

const handleDelete = async () => {
  await taskStore.deleteTask(props.task.id);
};

watch(
    () => props.task,
    (newTask) => {
      editedTask.value = { ...newTask };
    }
);
</script>
