import { z } from 'zod';
import {TaskStatus} from "@/entities/task/enums.ts";
import {dateFromString} from "@utils/dates.ts";

export const taskBaseSchema = z.object({
  name: z.string(),
  description: z.string(),
});

export const taskResponseSchema = taskBaseSchema.extend({
  id: z.number(),
  status: z.nativeEnum(TaskStatus),
  createdAt: dateFromString,
  updatedAt: dateFromString,
});

export const taskPatchSchema = taskBaseSchema.extend({
  name: z.string().nullable(),
  description: z.string().nullable(),
  status: z.string().nullable(),
});