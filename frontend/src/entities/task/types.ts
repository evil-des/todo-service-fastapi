import { z } from 'zod';
import {taskBaseSchema, taskPatchSchema, taskResponseSchema} from "@/entities/task/schemas.ts";

export type Task = z.infer<typeof taskResponseSchema>;
export type TaskCreate = z.infer<typeof taskBaseSchema>;
export type TaskUpdate = z.infer<typeof taskPatchSchema>;

export interface TaskStore {
  tasks: Task[] | undefined;
}
