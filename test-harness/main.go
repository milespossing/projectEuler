package main

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"os/exec"
	"strconv"
	"strings"
)

type Language struct {
	Name    string
	Exe     string
	Params  []string
	WorkDir string
}

type Config struct {
	Languanges []Language `json:"Languages"`
	Test       string
}

type Answer struct {
	Problem int
	Answer  int
}

func get_answers(path string) []Answer {
	f, err := os.Open(path)

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	csv_reader := csv.NewReader(f)

	data, err := csv_reader.ReadAll()

	if err != nil {
		log.Fatal(err)
	}

	var answers []Answer

	for i, line := range data {
		if i > 0 {
			var answer Answer
			for j, field := range line {
				val, err := strconv.Atoi(field)
				if err != nil {
					log.Fatal(err)
				}
				if j == 0 {
					answer.Problem = val
				} else {
					answer.Answer = val
				}
			}
			answers = append(answers, answer)
		}
	}

	return answers
}

func main() {
	answers := get_answers("answers.csv")
	file, _ := ioutil.ReadFile("conf.json")
	var config Config
	err := json.Unmarshal(file, &config)
	if err != nil {
		fmt.Println("error:", err)
	} else {
		for _, lang := range config.Languanges {
			test_language(lang, answers)
		}
	}
}

func test_language(lang Language, answers []Answer) {
	fmt.Println("Language:", lang.Name)
	for _, answer := range answers {
		params := lang.Params
		params = append(params, "--problem", fmt.Sprint(answer.Problem))
		cmd := exec.Command(lang.Exe, params...)
		cmd.Dir = lang.WorkDir
		stdout, stderr := cmd.Output()
		if stderr != nil {
			log.Fatal(stderr.Error())
		} else {
			actual := Answer{
				Problem: answer.Problem,
			}

			val, err := strconv.Atoi(strings.Replace(string(stdout), "\n", "", -1))

			if err != nil {
				actual.Answer = -1
			} else {
				actual.Answer = val
			}

			check_answer(actual, answer)
		}
	}
}

func check_answer(actual Answer, expected Answer) {
	if actual.Answer == expected.Answer {
		fmt.Println(expected.Problem, "✅")
	} else {
		fmt.Println(expected.Problem, "❗")
	}
}
