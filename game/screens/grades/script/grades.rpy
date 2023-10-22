screen grades():
    add "bg_grades"
    imagemap:
        idle "main_buttons_grades"
        alpha False
        hotspot (0, 1407, 240, 153) action [Hide("grades"), Show("home")] #Learn
        #hotspot (240, 1407, 720, 1560) action [Hide("home"), Show("main_menu")] #Stats
        hotspot (480, 1407, 720, 1560) action [Hide("home"), Show("main_menu")] #Settings

    grid 1 3 xpos 45 ypos 331 spacing 47:
        grid 2 2 spacing 47:
            add "test_1_0"
            add "test_2_0"
            add "test_3_0"
            add "test_4_0"
        add "test_5_0":
            xalign 0.5