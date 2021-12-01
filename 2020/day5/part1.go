package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func check(err error) {
	if err != nil {
		log.Fatalln(err)
	}
}

func main() {
	input, err := os.ReadFile("input.txt")
	check(err)
	sequences := strings.Split(strings.TrimSuffix(string(input), "\n"), "\n")

	largestSeatID := -1
	for _, sequence := range sequences {
		row := parse(sequence[0:7])
		col := parse(translate(sequence[7:10]))
		seatID := calcSeatID(row, col)
		//fmt.Println(row, col, seatID)

		if seatID > largestSeatID {
			largestSeatID = seatID
		}
	}

	fmt.Println("largest seat id:", largestSeatID)
}

func translate(sequence string) (result string) {
	result = strings.Replace(sequence, "L", "F", -1)
	result = strings.Replace(result, "R", "B", -1)

	return result
}

func parse(sequence string) int {
	b := byte(0)
	bit := len(sequence)

	for _, instruction := range sequence {
		switch instruction {
		case 'F':
			b |= (0 << (bit - 1))
			bit -= 1
		case 'B':
			b |= (1 << (bit - 1))
			bit -= 1
		default:
			log.Fatalln("illegal instruction:", string(instruction))
		}
	}

	return int(b)
}

func calcSeatID(row int, col int) int {
	return row*8 + col
}
