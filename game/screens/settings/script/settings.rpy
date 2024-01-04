default persistent.sound = True

screen settings():
    add "bg_settings"
    imagemap:
        idle "main_buttons_settings"
        alpha False
        hotspot (0, 1407, 240, 153) action [Hide("settings"), Show("home"), Play("sound", "audio/click_2.mp3")] #Learn
        hotspot (240, 1407, 720, 1560) action [Hide("settings"), Show("grades"), Play("sound", "audio/click_2.mp3")] #Stats

    viewport:
        area (46, 240, 640, 678)
        draggable True
        vbox:
            spacing 45
            add "empty_space"

            #Sound
            frame:
                background "sound"
                imagebutton:
                    focus_mask True
                    if persistent.sound == True:
                        idle "screens/settings/ui/buttons/on.png"
                        action [SetVariable("persistent.sound", False), Play("sound", "audio/click.mp3"), Preference("all mute", "toggle")]
                    else:
                        idle "screens/settings/ui/buttons/off.png"
                        action [SetVariable("persistent.sound", True), Play("sound", "audio/click.mp3"), Preference("all mute", "toggle")]

            #Delete data
            frame:
                background "delete"
                imagebutton:
                    focus_mask True
                    idle "screens/settings/ui/buttons/delete.png"
                    action [Hide("settings"), Show("confirm_delete"), Play("sound", "audio/click.mp3")]

screen confirm_delete():
    #Change assets
    #Add hotspot for cancel confirmation
    add "bg_test"
    add "screens/settings/ui/buttons/settings_confirm_ground.png"
    imagemap:
        idle "screens/settings/ui/buttons/settings_confirm_button.png"
        alpha True
        hotspot (45, 1136, 293, 104) action [
            SetField(persistent, "sound", True),
            SetField(persistent, "test_result", [0, 0, 0, 0, 0, 0]),
            SetField(persistent, "progress", 1),
            Hide("confirm_delete"),
            Show("main_menu"),
            Play("sound", "audio/click_2.mp3")
        ]
        hotspot (384, 1136, 293, 104) action [
            Hide("confirm_delete"),
            Show("settings"),
            Play("sound", "audio/click.mp3")
        ]