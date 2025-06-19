About
============

This template is designed to help developers quickly set up **modern C++ projects** with best practices. It includes:

  - **Developer Mode** (Address Sanitizer, Undefined Behavior Sanitizer, warnings as errors)
  - **Static Analysis** (clang-tidy, cppcheck)
  - **Dependency Management** via CPM/Conan
  - **CMake** as the build system
  - **Preconfigured Testing & CI**
  - **Integration with FTXUI** for CLI applications
  - **Documentation** with Doxygen and Sphinx
  - **Fuzz Testing** with libFuzzer
  - **Docker** support for consistent builds

Getting Started
---------------
1. **Use the GitHub template** → For more details, visit `cpp-best-practice-template <https://github.com/cpp-best-practices/cmake_template/generate>`__.

2. **Clone your project**

   .. code-block:: bash

      git clone https://github.com/<user>/<your_new_repo>.git
      cd <your_new_repo>

Other
---------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   dependencies
   contributing
   

For more information on contributing to the project, see :doc:`contributing`.