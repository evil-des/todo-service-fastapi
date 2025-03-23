import axios from 'axios';
import {
  handleErrorResponse,
  setSessionStorageTokenToHeaders,
} from '@/shared/api/interceptors.ts';

export const apiBase = axios.create({
  baseURL: '/api',
});

apiBase.interceptors.request.use(setSessionStorageTokenToHeaders);
apiBase.interceptors.response.use(undefined, handleErrorResponse);
