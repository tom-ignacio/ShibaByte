default persistent.read_time = 0
define unit = 0

screen unit():
    $ renpy.transition(Dissolve(0.1))
    add "bg_units"
    imagemap:
        idle "main_button_units"
        alpha False
        hotspot (10, 70, 158, 158) action [Hide("unit"), Show("home")] #Back

    viewport:
        area (0, 228, 720, 1332)
        draggable True
        vbox:
            add "content_unit_[unit]"