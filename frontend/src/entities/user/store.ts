import { defineStore } from 'pinia';
import type {UserAuth, UserStore} from './types';
import {fetchUserMe, loginUser, registerUser} from "@/entities/user/api.ts";
import {authenticateAndStoreToken} from "@/shared/api/utils.ts";

export const useUserStore = defineStore('userData', {
  state: (): UserStore => ({
    user: undefined,
    isAuthenticated: false,
  }),
  actions: {
    async fetch() {
      this.user = await fetchUserMe();
    },
    async auth(type: "login" | "register", authData: UserAuth) {
      const apiMethod = type === "login" ? loginUser : registerUser;
      await authenticateAndStoreToken(authData, apiMethod);
      this.isAuthenticated = true;
    },
  },
});
