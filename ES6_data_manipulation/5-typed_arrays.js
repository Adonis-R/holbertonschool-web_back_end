export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const int8Array = new Int8Array(buffer);
  if (position < 0 || position >= int8Array.length) {
    throw new Error('Position outside range');
  }
  int8Array[position] = value;
  return buffer;
}
