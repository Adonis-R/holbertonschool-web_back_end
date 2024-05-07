export default function appendToEachArrayValue(array, appendString) {
  const NewArray = [];

  for (const idx of array) {
    const value = array[idx];
    NewArray.push(appendString + value);
  }

  return NewArray;
}
