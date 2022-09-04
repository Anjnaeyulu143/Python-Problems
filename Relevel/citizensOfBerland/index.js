let n = parseInt(readline());
let arr = readline()
  .split(" ")
  .map((a) => parseInt(a));
let count = 0;
for (let i = 0; i < n - 1; i++) {
  if (arr[i] === 1 && arr[i - 1] === 0 && arr[i + 1] === 0) {
    arr[i + 1] = 1;
    count++;
  }
}

print(count);
