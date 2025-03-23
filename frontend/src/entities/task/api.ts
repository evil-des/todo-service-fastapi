import { apiBase } from '@/shared/api/axios';
import { z } from 'zod';
import type {Task, TaskCreate, TaskUpdate} from "@/entities/task/types.ts";
import {taskResponseSchema} from "@/entities/task/schemas.ts";

export const fetchTasks = async () => {
  const response = await apiBase.get<Task[]>('/v1/task');
  return z.array(taskResponseSchema).parse(response.data);
};

export const createTask = async (taskData: TaskCreate) => {
  const response = await apiBase.put<Task>('/v1/task', taskData);
  return taskResponseSchema.parse(response.data);
};

export const updateTask = async (taskId: number, taskData: TaskUpdate) => {
  const response = await apiBase.patch<Task>(`/v1/task/${taskId}`, taskData);
  return taskResponseSchema.parse(response.data);
};

export const deleteTask = async (taskId: number) => {
  await apiBase.delete(`/v1/task/${taskId}`);
};