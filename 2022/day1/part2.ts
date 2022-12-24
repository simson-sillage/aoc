#!/usr/bin/env node
import * as fs from 'fs';
import { openStdin } from 'process';

if (process.argv.length != 3) {
    console.log(`usage: ${process.argv[0]} <filename>`);
    process.exit(1);
}

const filename = process.argv[2];
const input = fs.readFileSync(filename, 'utf8');

const elves = input.split(/\r?\n\r?\n/).filter(e => e);
let summedCaloriesPerElf: number[] = [];

elves.forEach(elf => {
    const calories = elf.split(/\r?\n/).filter(e => e);
    const parsedCalories = calories.map(e => parseInt(e));
    const sum = parsedCalories.reduce((a, b) => a + b, 0);
    summedCaloriesPerElf.push(sum);
})
summedCaloriesPerElf.sort((a, b) => b - a);

if (summedCaloriesPerElf.length < 3) {
    console.log("error: less than 3 elves in input.");
    process.exit(2);
}

const answer = summedCaloriesPerElf[0] + summedCaloriesPerElf[1] + summedCaloriesPerElf[2];
console.log("sum of the 3 richest elves:", answer);
