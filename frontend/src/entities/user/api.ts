import { apiBase } from '@/shared/api/axios';
import type {User, UserAuth} from '@/entities/user/types';
import {userSchema} from '@/entities/user/schemas';

export const fetchUserMe = async () => {
  const response = await apiBase.get<User>('/v1/user/me');
  return userSchema.parse(response.data);
};

export const loginUser = async (authData: UserAuth) => {
  const response = await apiBase.post('/v1/user/login', authData);
  return response.data;
};

export const registerUser = async (authData: UserAuth) => {
  const response = await apiBase.post('/v1/user/register', authData);
  return response.data;
};
