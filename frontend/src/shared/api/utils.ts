import type { InternalAxiosRequestConfig } from 'axios';
import { AxiosError } from 'axios';
import type {UserAuth} from "@/entities/user/types.ts";

export const ACCESS_TOKEN_SESSION_STORAGE_KEY = 'access_token';
export const ACCESS_TOKEN_HEADER_KEY = 'Access-Token';

export const getOriginalRequest = (
  error: AxiosError
): InternalAxiosRequestConfig & {
  _retry?: boolean;
} => {
  return error.config!;
};

export const authenticateAndStoreToken = async (
    authData: UserAuth,
    authMethod: (data: UserAuth) => Promise<string>
): Promise<string> => {
  const token = await authMethod(authData);
  sessionStorage.setItem(ACCESS_TOKEN_SESSION_STORAGE_KEY, token);
  return token;
};
