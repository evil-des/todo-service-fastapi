<template>
  <div class="flex justify-between items-start gap-4 text-left rounded-2xl p-6 bg-white shadow-sm w-full">
    <div class="flex flex-col flex-1 min-w-0">
      <p class="text-sm">Дата создания: {{createdAtLabel}}</p>
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
    <div class="flex flex-col items-center gap-4 font-medium shrink-0 text-right">
      <p v-if="isModified" class="text-green-600 cursor-pointer" @click="saveChanges">Сохранить</p>
      <p class="text-red-500 cursor-pointer" @click="handleDelete">Удалить</p>
      <input
          type="checkbox"
          :checked="isCompleted"
          @change="toggleStatus"
          class="form-checkbox h-7 w-7 text-green-600"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import {computed, ref, watch} from "vue";
import { format } from 'date-fns';
import type { Task } from "@/entities/task/types";
import { useTaskStore } from "@/entities/task/store";
import {TaskStatus} from "@/entities/task/enums.ts";

const props = defineProps<{ task: Task }>();
const taskStore = useTaskStore();

const editedTask = ref({ ...props.task });
const isModified = ref(false);

const createdAtLabel = computed(() => {
  return format(new Date(props.task.createdAt), "dd MMM yyyy, HH:mm");
});
const isCompleted = computed({
  get: () => editedTask.value.status === TaskStatus.COMPLETED,
  set: (val: boolean) => {
    editedTask.value.status = val ? TaskStatus.COMPLETED : TaskStatus.NOT_COMPLETED;
    isModified.value = true;
  },
});

const onInputChange = () => {
  isModified.value = editedTask.value.name !== props.task.name ||
      editedTask.value.description !== props.task.description;
};

const toggleStatus = (event: Event) => {
  const target = event.target as HTMLInputElement;
  isCompleted.value = target.checked;
};

const saveChanges = async () => {
  if (editedTask.value.id < 0) {
    await taskStore.saveNewTask(editedTask.value);
    isModified.value = false;
    return
  }
  await taskStore.updateTask(editedTask.value.id, {
    name: editedTask.value.name,
    description: editedTask.value.description,
    status: editedTask.value.status,
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
