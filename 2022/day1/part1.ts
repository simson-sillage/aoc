#!/usr/bin/env node
import * as fs from 'fs';

if (process.argv.length != 3) {
    console.log(`usage: ${process.argv[0]} <filename>`);
    process.exit(1);
}

const filename = process.argv[2];
const input = fs.readFileSync(filename, 'utf8');

const elves = input.split(/\r?\n\r?\n/).filter(e => e);
var biggest = -1;

elves.forEach(elve => {
    const calories = elve.split(/\r?\n/).filter(e => e);
    const parsedCalories = calories.map(e => parseInt(e));
    const sum = parsedCalories.reduce((a, b) => a + b, 0);
    if (sum > biggest) {
        biggest = sum;
    }
})

console.log("biggest sum of calories on a elf:", biggest);

