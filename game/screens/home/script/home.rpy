default persistent.progress = 1

screen home():
    add "bg_home"
    add "tips_home"
    imagemap:
        idle "main_buttons_home"
        alpha False
        hotspot (240, 1407, 720, 1560) action [Hide("home"), Show("grades")] #Stats
        hotspot (480, 1407, 720, 1560) action [Hide("home"), Show("settings")] #Settings

    viewport:
        area (46, 722, 640, 678)
        draggable True
        vbox:
            spacing 45
            add "empty_space"
            #Unit 1
            frame:
                background "unit_1"
                imagebutton:
                    focus_mask True
                    if persistent.progress >= 1:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("unit"), 
                            SetVariable("unit", 1),
                            If(persistent.progress == 1, SetVariable("persistent.progress", 2), NullAction())]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Unit 2
            frame:
                background "unit_2"
                imagebutton:
                    focus_mask True
                    if persistent.progress >= 2:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("unit"),
                            SetVariable("unit", 2),
                            If(persistent.progress == 2, SetVariable("persistent.progress", 3), NullAction())]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Unit 3
            frame:
                background "unit_3"
                imagebutton:
                    focus_mask True
                    if persistent.progress >= 3:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("unit"), 
                            SetVariable("unit", 3),
                            If(persistent.progress == 3, SetVariable("persistent.progress", 4), NullAction())]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Test 1
            frame:
                background "test_1"
                imagebutton:
                    if persistent.progress >= 4:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("test"), 
                            SetVariable("test_number", 1), 
                            SetVariable("counter", 0),
                            SetVariable("correct", 0),
                            SetVariable("incorrect", 0),
                            SetVariable("question", renpy.random.randint(0, 2))]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Unit 4
            frame:
                background "unit_4"
                imagebutton:
                    focus_mask True
                    if persistent.progress >= 5:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("unit"), 
                            SetVariable("unit", 4),
                            If(persistent.progress == 5, SetVariable("persistent.progress", 6), NullAction())]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Unit 5
            frame:
                background "unit_5"
                imagebutton:
                    focus_mask True
                    if persistent.progress >= 6:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("unit"), 
                            SetVariable("unit", 5),
                            If(persistent.progress == 6, SetVariable("persistent.progress", 7), NullAction())]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Test 2
            frame:
                background "test_2"
                imagebutton:
                    if persistent.progress >= 7:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("test"), 
                            SetVariable("test_number", 2), 
                            SetVariable("counter", 0),
                            SetVariable("correct", 0),
                            SetVariable("incorrect", 0),
                            SetVariable("question", renpy.random.randint(15, 17))]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Unit 6
            frame:
                background "unit_6"
                imagebutton:
                    focus_mask True
                    if persistent.progress >= 8:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("unit"), 
                            SetVariable("unit", 6),
                            If(persistent.progress == 8, SetVariable("persistent.progress", 9), NullAction())]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Unit 7
            frame:
                background "unit_7"
                imagebutton:
                    focus_mask True
                    if persistent.progress >= 9:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("unit"), 
                            SetVariable("unit", 7),
                            If(persistent.progress == 9, SetVariable("persistent.progress", 10), NullAction())]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Test 3
            frame:
                background "test_3"
                imagebutton:
                    if persistent.progress >= 10:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("test"), 
                            SetVariable("test_number", 3), 
                            SetVariable("counter", 0),
                            SetVariable("correct", 0),
                            SetVariable("incorrect", 0),
                            SetVariable("question", renpy.random.randint(0, 2))]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Unit 8
            frame:
                background "unit_8"
                imagebutton:
                    focus_mask True
                    if persistent.progress >= 11:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("unit"), 
                            SetVariable("unit", 8),
                            If(persistent.progress == 11, SetVariable("persistent.progress", 12), NullAction())]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Unit 9
            frame:
                background "unit_9"
                imagebutton:
                    focus_mask True
                    if persistent.progress >= 12:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("unit"),
                            SetVariable("unit", 9), 
                            If(persistent.progress == 12, SetVariable("persistent.progress", 13), NullAction())]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Test 4
            frame:
                background "test_4"
                imagebutton:
                    if persistent.progress >= 13:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("test"), 
                            SetVariable("test_number", 4), 
                            SetVariable("counter", 0),
                            SetVariable("correct", 0),
                            SetVariable("incorrect", 0),
                            SetVariable("question", renpy.random.randint(0, 2))]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Unit 10
            frame:
                background "unit_4"
                imagebutton:
                    focus_mask True
                    if persistent.progress >= 14:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("unit"), 
                            SetVariable("unit", 10),
                            If(persistent.progress == 14, SetVariable("persistent.progress", 15), NullAction())]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Unit 11
            frame:
                background "unit_11"
                imagebutton:
                    focus_mask True
                    if persistent.progress >= 15:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("unit"), 
                            SetVariable("unit", 11),
                            If(persistent.progress == 15, SetVariable("persistent.progress", 16), NullAction())]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            #Test 5
            frame:
                background "test_5"
                imagebutton:
                    if persistent.progress >= 16:
                        idle "screens/home/ui/buttons/unit_unlocked.png"
                        action [
                            Hide("home"), 
                            Show("test"), 
                            SetVariable("test_number", 5), 
                            SetVariable("counter", 0),
                            SetVariable("correct", 0),
                            SetVariable("incorrect", 0),
                            SetVariable("question", renpy.random.randint(0, 2))]
                    else:
                        idle "screens/home/ui/buttons/unit_locked.png"

            add "empty_space"
    add "screens/home/ui/fade_effect.png"