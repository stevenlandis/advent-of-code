import * as fs from "fs";

async function main() {
  let txt = await fs.promises.readFile("1.txt", { encoding: "utf8" });
  let best = 0;
  let acc = 0;
  for (let line of txt.split("\n")) {
    line = line.trim();
    if (line === "") {
      best = Math.max(best, acc);
      acc = 0;
    } else {
      acc += parseInt(line);
    }
  }
  best = Math.max(best, acc);

  console.log(best);

  let groups = fs
    .readFileSync("1.txt", { encoding: "utf8" })
    .split("\n\n")
    .map((group) =>
      group
        .split("\n")
        .map((x) => x.trim())
        .filter((x) => x !== "")
        .map((x) => parseInt(x))
        .reduce((acc, x) => acc + x)
    );
  best = fs
    .readFileSync("1.txt", { encoding: "utf8" })
    .split("\n\n")
    .map((group) =>
      group
        .split("\n")
        .map((x) => x.trim())
        .filter((x) => x !== "")
        .map((x) => parseInt(x))
        .reduce((acc, x) => acc + x)
    )
    .sort((a, b) => b - a)
    .slice(0, 3)
    .reduce((acc, x) => acc + x);
  console.log(best);
}

main();
