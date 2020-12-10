while True:
    if input.light_level() > 75 :
        light.set_all(light.rgb(255,255,255))
else:
    light.clear()
