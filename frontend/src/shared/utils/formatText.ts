export const cutTheText = (
  text: string,
  maxLength: number,
  suffix: string = '..'
) => {
  const targetLength = maxLength - suffix.length;
  if (text.length > targetLength) return text.slice(0, targetLength) + suffix;
  return text;
};
