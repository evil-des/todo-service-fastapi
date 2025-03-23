import { z } from 'zod';

export const userSchema = z.object({
  id: z.number(),
  username: z.string(),
});

export const userAuthSchema = z.object({
  username: z.string(),
  password: z.string(),
});
