export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const int8 = new Int8Array(buffer);
  if (position < length) {
    int8[position] = value;
  } else {
    throw new Error('Position outside range');
  }
  return int8;
}
