default test_number = 0
define next_sum = 0
define counter = 0
define question = 0
define result = 0

default correct = 0
default incorrect = 0

default persistent.grade = [0, 0, 0, 0, 0]

#Order is: A check, B check, C check
define test_questions = [
[False, True, False], #0 Test 1
[False, False, True], #1
[True, False, False], #2
[True, False, False], #3
[False, False, True], #4
[True, False, False], #5
[False, False, True], #6
[False, True, False], #7
[True, False, False], #8
[True, False, False], #9
[False, True, False], #10
[True, False, False], #11
[False, False, True], #12
[False, False, True], #13
[False, True, False], #14
[False, True, False], #15 Test 2
[False, True, False], #16
[True, False, False], #17
[True, False, False], #18
[True, False, False], #19
[False, True, False], #20
[False, False, True], #21
[True, False, False], #22
[True, False, False], #23
[True, False, False], #24
[True, False, False], #25
[True, False, False], #26
[True, False, False], #27
[False, False, True], #28
[False, True, False], #29
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

screen question_result():
    modal True
    $ renpy.transition(Dissolve(0.1))
    #add "bg_test"
    add "question_result_[result]"
    #text "CORRECT [correct] INCORRECT [incorrect] ACTUAL GRADE [persistent.test_result[1]]" size 50
    $ next_sum = renpy.random.randint(1, 2)
    timer 1.0 action [
        Hide("question_result"), Show("test"),
        If(counter == 6,
            [Hide("test"),
            Show("result"),
            SetDict(persistent.test_result, test_number, correct),
            If(correct > 3,
                [If(persistent.progress == 4 and correct > 3, SetVariable("persistent.progress", 5), NullAction()),
                If(persistent.progress == 7 and correct > 3, SetVariable("persistent.progress", 8), NullAction()),
                If(persistent.progress == 10 and correct > 3, SetVariable("persistent.progress", 11), NullAction()),
                If(persistent.progress == 13 and correct > 3, SetVariable("persistent.progress", 14), NullAction())],
            NullAction())],
        [Hide("question_result"), SetVariable("counter", counter + 1), SetVariable("question", question + next_sum)]),
    ]

screen result():
    add "bg_test"
    if persistent.test_result[test_number] > 3:
        add "screens/test/ui/result_0.png"
        imagemap:
            idle "screens/test/ui/result_button_0.png"
            alpha True
            hotspot (46, 1136, 631, 104) action [Hide("result"), Show("home")]
    else:
        add "screens/test/ui/result_1.png"
        imagemap:
            idle "screens/test/ui/result_button_1.png"
            alpha True
            hotspot (46, 1136, 631, 104) action [Hide("result"), Show("home")]


#default persistent.data = [
#[A, B, C],
#[D, E, F]
#]

#SetDict(persistent.data[0], 1, T) would change "B" to "T"