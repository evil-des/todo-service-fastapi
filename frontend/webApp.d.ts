import 'telegram-web-app';

declare global {
  interface Window {
    Telegram: Telegram;
  }
}
