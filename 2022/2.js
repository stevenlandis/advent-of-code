import * as fs from "fs";

async function main() {
  let q = { r: 0, p: 1, s: 2 };
  let qi = Object.fromEntries(Object.entries(q).map(([a, b]) => [b, a]));
  let f = { l: -1, t: 0, w: 1 };
  let f2 = { l: 0, t: 3, w: 6 };
  let plays = (await fs.promises.readFile("2.txt", { encoding: "utf8" }))
    .split("\n")
    .map((x) => x.trim())
    .filter((x) => x !== "")
    .map((x) => x.split(" "))
    .map(([a, b]) => [
      { A: "r", B: "p", C: "s" }[a],
      { X: "l", Y: "t", Z: "w" }[b],
    ])
    .map(([a, b]) => q[qi[(q[a] + f[b] + 3) % 3]] + 1 + f2[b])
    .reduce((acc, x) => acc + x);
  console.log(plays);
}

main();
