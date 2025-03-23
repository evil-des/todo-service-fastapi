import { AxiosError, type InternalAxiosRequestConfig } from 'axios';
import {
  ACCESS_TOKEN_HEADER_KEY,
  ACCESS_TOKEN_SESSION_STORAGE_KEY,
  getOriginalRequest,
} from '@/shared/api/utils.ts';
import {userLoginRoute} from "@/pages/user/routes.ts";
import {goTo} from "@utils/navigation.ts";

export const setSessionStorageTokenToHeaders = (
  config: InternalAxiosRequestConfig
): InternalAxiosRequestConfig => {
  const token = sessionStorage.getItem(ACCESS_TOKEN_SESSION_STORAGE_KEY);
  if (token) config.headers[ACCESS_TOKEN_HEADER_KEY] = token;
  return config;
};

const handleUnauthorized = async (error: AxiosError) => {
  sessionStorage.removeItem(ACCESS_TOKEN_SESSION_STORAGE_KEY);
  await goTo(userLoginRoute);
};

export const handleErrorResponse = async (error: AxiosError) => {
  const originalRequest = getOriginalRequest(error);
  if (!originalRequest._retry) {
    originalRequest._retry = true;
    if (error.response?.status === 401) await handleUnauthorized(error);
  }
  return Promise.reject(error);
};
