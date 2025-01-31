# Testing GLFW with conan

Use the following commands:

```
conan install -u -pr linux-wayland.profile .
cmake --preset conan-linux-release
./build/linux/Release/glfw_example
```

Everything under the `./src` folder is taken from the [glfw sources](https://github.com/glfw/glfw/).
Everything else is my own work and licensed under MIT.
