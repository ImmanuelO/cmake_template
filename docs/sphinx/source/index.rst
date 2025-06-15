cmake_template Documentation
============================

Welcome to the documentation for **cmake_template**, a C++ Best Practices GitHub template for fast and structured development.

.. toctree::
   :maxdepth: 2
   :caption: 📖 Contents

   about
   installation
   usage
   dependencies
   building
   docker
   testing
   fuzz_testing
   contributing

About cmake_template
---------------------
**cmake_template** is designed to help developers quickly set up **modern C++ projects** with best practices.  
It includes:
- **Developer Mode** (Address Sanitizer, Undefined Behavior Sanitizer, warnings as errors)
- **Static Analysis** (clang-tidy, cppcheck)
- **Dependency Management** via CPM
- **Preconfigured Testing & CI**
- **Integration with FTXUI** for CLI applications

For a detailed overview, see :doc:`about`.

Getting Started
---------------
1. **Use the GitHub template** → Follow [GitHub’s guide](https://github.com/cpp-best-practices/cmake_template/generate)
2. **Clone your project**:
   ```bash
   git clone https://github.com/<user>/<your_new_repo>.git
   cd <your_new_repo>
