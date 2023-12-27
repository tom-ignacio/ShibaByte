default persistent.test_result = [0, 0, 0, 0, 0, 0]

screen grades():
    add "bg_grades"
    imagemap:
        idle "main_buttons_grades"
        alpha False
        hotspot (0, 1407, 240, 153) action [Hide("grades"), Show("home")] #Learn
        hotspot (480, 1407, 720, 1560) action [Hide("grades"), Show("settings")] #Settings

    grid 1 3 xpos 45 ypos 331 spacing 47:
        grid 2 2 spacing 47:
            add "test_1_[persistent.test_result[1]]"
            add "test_2_[persistent.test_result[2]]"
            add "test_3_[persistent.test_result[3]]"
            add "test_4_[persistent.test_result[4]]"
        add "test_5_[persistent.test_result[5]]":
            xalign 0.5