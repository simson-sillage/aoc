#!/usr/bin/env node
import * as fs from 'fs';

if (process.argv.length != 3) {
    console.log(`usage: ${process.argv[0]} <filename>`);
    process.exit(1);
}

const filename = process.argv[2];
const input = fs.readFileSync(filename, 'utf8');
const rounds = input.split(/\r?\n/).filter(e => e);

const scoring = new Map();
scoring.set('X', 1);
scoring.set('Y', 2);
scoring.set('Z', 3);
scoring.set('A', 1)
scoring.set('B', 2)
scoring.set('C', 3)

let score = 0;
rounds.forEach(round => {
    const [enemy, self] = round.split(' ');
    score += scoring.get(self);
    const diff = scoring.get(self) - scoring.get(enemy);
    switch(diff) {
        case 1: /* we won */
        case -2:
            score += 6;
            break;
        case 2: /* we lost */
        case -1:
            break;
        case 0: /* draw */
            score += 3;
            break;
        default:
            console.log(`unexpected value in switch: ${diff}.`);
            process.exit(2);
    }
});

console.log('total score:', score);
