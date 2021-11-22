# Test with pygame controllers

This repo demonstrates a coupe of tests with pygame joysticks.

The `main.py` file uses the Pygame Joystick API, the default API used by pygame. This can be a hassle to work with, because you have to map controllers manually, or create a file with a database of controllers.

The `main.py` file uses the Pygame SDL2 Controller API that unifies controller buttons, making less of a hassle to work with, since the SDL2 database already includes many controller mappings, and you don't have to map them yourself.