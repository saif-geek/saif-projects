from cx_Freeze import setup, Executable

setup(
    name = "projet1",
    version = "1.0",
    description = "mon premer projet ambicieux",
    executables = [Executable("projet v1.py")]
)