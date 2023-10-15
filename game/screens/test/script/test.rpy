define test_number = 0
define next_sum = renpy.random.randint(1, 2)
define counter = 0
define question = renpy.random.randint(0, 2)
define result = 0

define correct = 0
define incorrect = 0

default persistent.grade = [0, 0, 0, 0, 0]

#Order is: Read, A check, B check, C check
define test_questions = [
[True, False, False], #0
[False, True, False], #1
[False, False, True], #2
[False, False, True], #3
[False, False, True], #4
]

screen test():
    $ renpy.transition(Dissolve(0.1))
    add "bg_test"
    add "screens/test/ui/question_[test_number]_[question].png"
    imagemap:
        idle "screens/test/ui/answers_[test_number]_[question].png"
        alpha False
        hotspot (46, 760, 630, 170) action [
            Show("question_result"),
            If(test_questions[question][0] == True, [SetVariable("correct", correct + 1), SetVariable("result", 0)], [SetVariable("incorrect", incorrect + 1), SetVariable("result", 1)])]
        hotspot (46, 975, 630, 170) action [
            Show("question_result"),
            If(test_questions[question][1] == True, [SetVariable("correct", correct + 1), SetVariable("result", 0)], [SetVariable("incorrect", incorrect + 1), SetVariable("result", 1)])]
        hotspot (46, 1191, 630, 170) action [
            Show("question_result"),
            If(test_questions[question][2] == True, [SetVariable("correct", correct + 1), SetVariable("result", 0)], [SetVariable("incorrect", incorrect + 1), SetVariable("result", 1)])]

    text "Question: [question] List: [test_questions]" size 20 color "#000000" #Delete after

screen question_result():
    $ renpy.transition(Dissolve(0.1))
    #add "bg_test"
    add "question_result_[result]"
    $ next_sum = renpy.random.randint(1, 2)
    timer 1.0 action [
        Hide("question_result"), Show("test"),
        If(counter == 1, [Hide("test"), Show("home")], [Hide("question_result"), SetVariable("counter", counter + 1), SetVariable("question", question + next_sum)]),
    ]


#default persistent.data = [
#[A, B, C],
#[D, E, F]
#]

#SetDict(persistent.data[0], 1, T) would change "B" to "T"