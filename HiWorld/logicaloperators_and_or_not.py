animation_training=True
boogaloo_training=False

if animation_training or boogaloo_training:
    years_popping=input('How long have you trained popping?')

if animation_training and boogaloo_training:
    print('Congratulations! You can start the accelerated program! ')

if animation_training and not boogaloo_training:
    input('Would you like to delve deeper into animation? ')
