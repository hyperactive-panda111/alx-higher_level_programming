#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (Number.isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0, x; i < arg; i++) {
    x = '';
    for (let j = 0; j < arg; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
