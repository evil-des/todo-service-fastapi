import { defineStore } from 'pinia';
import type {Task, TaskCreate, TaskStore, TaskUpdate} from './types';
import {createTask, deleteTask, fetchTasks, updateTask} from "@/entities/task/api.ts";
import {TaskStatus} from "@/entities/task/enums.ts";

export const useTaskStore = defineStore('taskData', {
  state: (): TaskStore => ({
    tasks: undefined,
  }),
  actions: {
    async fetchTasks() {
      this.tasks = await fetchTasks();
    },
    async updateTask(taskId: number, patchSchema: TaskUpdate) {
      if (taskId < 0) return;
      const updatedTask = await updateTask(taskId, patchSchema);
      if (this.tasks) {
        const index = this.tasks.findIndex(t => t.id === taskId);
        if (index !== -1) {
          this.tasks.splice(index, 1, updatedTask);
        }
      }
    },
    async deleteTask(taskId: number) {
      if (taskId > 0) await deleteTask(taskId);
      if (this.tasks) {
        this.tasks = this.tasks.filter(t => t.id !== taskId);
      }
    },
    addEmptyTask() {
      const tempTask: Task = {
        id: -Date.now(),
        name: "",
        description: "",
        status: TaskStatus.NOT_COMPLETED,
        createdAt: new Date(),
        updatedAt: new Date(),
      };
      const tasks = this.tasks ?? [];
      tasks.unshift(tempTask);
      this.tasks = tasks;
    },
    async saveNewTask(task: Task) {
      const { name, description } = task;
      const taskCreateData: TaskCreate = { name, description };

      const savedTask = await createTask(taskCreateData);
      if (this.tasks) {
        const index = this.tasks.findIndex(t => t.id === task.id);
        if (index !== -1) {
          this.tasks.splice(index, 1, savedTask);
        }
      }
    },
  },
});
