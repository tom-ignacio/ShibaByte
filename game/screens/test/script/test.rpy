default test_number = 0
define next_sum = 0
define counter = 0
define question = 0
define result = 0

default correct = 0
default incorrect = 0

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
[True, False, False], #30 Test 3
[True, False, False], #31
[False, True, False], #32
[True, False, False], #33
[True, False, False], #34
[True, False, False], #35
[False, True, False], #36
[False, True, False], #37
[False, False, True], #38
[True, False, False], #39
[False, False, True], #40
[False, True, False], #41
[True, False, False], #42
[False, False, True], #43
[False, True, False], #44
[False, True, False], #45 Test 4
[False, False, True], #46
[False, True, False], #47
[True, False, False], #48
[True, False, False], #49
[True, False, False], #50
[False, True, False], #51
[False, True, False], #52
[False, False, True], #53
[True, False, False], #54
[False, True, False], #55
[False, True, False], #56
[True, False, False], #57
[False, False, True], #58
[False, True, False], #59
[True, False, False], #60 Test 5
[False, True, False], #61
[True, False, False], #62
[False, False, True], #63
[True, False, False], #64
[False, False, True], #65
[False, True, False], #66
[True, False, False], #67
[False, True, False], #68
[True, False, False], #69
[False, False, True], #70
[True, False, False], #71
[False, True, False], #72
[False, True, False], #73
[False, False, True], #74
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
            If(test_questions[question][0] == True, [SetVariable("correct", correct + 1), SetVariable("result", 0), Play("sound", "audio/correct.mp3")], [SetVariable("incorrect", incorrect + 1), SetVariable("result", 1), Play("sound", "audio/incorrect.mp3")])]
        hotspot (46, 975, 630, 170) action [
            Show("question_result"),
            If(test_questions[question][1] == True, [SetVariable("correct", correct + 1), SetVariable("result", 0), Play("sound", "audio/correct.mp3")], [SetVariable("incorrect", incorrect + 1), SetVariable("result", 1), Play("sound", "audio/incorrect.mp3")])]
        hotspot (46, 1191, 630, 170) action [
            Show("question_result"),
            If(test_questions[question][2] == True, [SetVariable("correct", correct + 1), SetVariable("result", 0), Play("sound", "audio/correct.mp3")], [SetVariable("incorrect", incorrect + 1), SetVariable("result", 1), Play("sound", "audio/incorrect.mp3")])]

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
                If(persistent.progress == 13 and correct > 3, SetVariable("persistent.progress", 14), NullAction()),
                Play("sound", "audio/win.mp3")],
                Play("sound", "audio/lose.mp3"))],
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