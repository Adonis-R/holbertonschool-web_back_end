export default function appendToEachArrayValue(array, appendString) {
  const NewArray = [];

  for (const value of array) {
    NewArray.push(appendString + value);
  }

  return NewArray;
}
