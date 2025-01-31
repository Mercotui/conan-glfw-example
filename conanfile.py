from conan import ConanFile
from conan.tools.cmake import cmake_layout


class RaylibWasm(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("glfw/3.4")
        # Workaround to fix Wayland EGL Window creation
        self.requires("wayland/1.23.0", override=True)

    def layout(self):
        cmake_layout(self)
