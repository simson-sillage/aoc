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
scoring.set('A', 1)
scoring.set('B', 2)
scoring.set('C', 3)

let score = 0;
rounds.forEach(round => {
    const [enemy, result] = round.split(' ');
    let shape = undefined;
    switch(result) {
        case 'X': /* we need to lose */
            shape = scoring.get(enemy) - 1;
            if (shape < 1) {
                shape = 3;
            }
            score += shape;
            break;
        case 'Y': /* we need to draw */
            score += scoring.get(enemy) + 3;
            break;
        case 'Z': /* we need to win */
            shape = scoring.get(enemy) + 1;
            if (shape > 3) {
                shape = 1;
            }
            score += shape + 6;
            break;
        default:
            console.log(`unexpected value in switch: ${result}.`);
            process.exit(2);
    }
});

console.log('total score:', score);
