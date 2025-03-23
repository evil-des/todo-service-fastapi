import { z } from 'zod';
import {userAuthSchema, userSchema,} from '@/entities/user/schemas.ts';

export type User = z.infer<typeof userSchema>;
export type UserAuth = z.infer<typeof userAuthSchema>;

export interface UserStore {
  user: User | undefined;
  isAuthenticated: boolean;
}
