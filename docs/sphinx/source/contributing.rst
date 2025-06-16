Contributing
============

Thank you for considering contributing to !  
This guide outlines how to contribute, submit code, and follow best practices.

Ways to Contribute
------------------
You can help improveby:

- **Reporting Issues** → Found a bug or have a feature request? Open an issue.
- **Submitting Pull Requests** → Enhance existing code or add new features.
- **Improving Documentation** → Expand and refine Sphinx documentation.
- **Optimizing Performance** → Help improve modularity and scalability.
- **Enhancing Security** → Propose authentication or encryption improvements.

Setting Up Your Development Environment
---------------------------------------
Before contributing, ensure you have the necessary dependencies installed and the project is correctly built.

- **Install required dependencies** → See :doc:`dependencies`
- **Build the project** → Follow :doc:`building`
- **Run tests before submitting changes** → Refer to :doc:`testing`

Code Guidelines
---------------
Follow these conventions to maintain code quality:

- **C++17 Standard** → Use modern C++ practices.
- **Static Analysis** → Run `clang-tidy` and `cppcheck` before submitting.
- **Consistent Formatting** → Apply `.clang-format` for uniform styling.
- **Modular Design** → Keep components scalable and reusable.

Submitting a Pull Request (PR)
------------------------------

1. **Fork the repository** → Click "Fork" on GitHub.
2. **Create a new branch**:

   .. code-block:: bash

      git checkout -b feature/my-improvement

3. **Make changes and commit**:

   .. code-block:: bash

      git add .
      git commit -m "Improve authentication module"

4. **Push your branch**:

   .. code-block:: bash

      git push origin feature/my-improvement

5. **Open a pull request** on GitHub.

Security Considerations
-----------------------
- Avoid committing **sensitive credentials** or private keys.
- Use **OAuth2, JWT, or Kerberos authentication** securely.
- Follow **secure coding practices** to prevent injection attacks.

Resources
---------

- **Issue Tracker** → [GitHub Issues](https://github.com/<myproject>/<myproject>/issues)
- **Project Wiki** → [Wiki Documentation](https://github.com/<myproject>/<myproject>/wiki)
- **Contributor License Agreement (CLA)** → If applicable.

Thank you for contributing to ! 🚀  
Your support makes this project better for everyone.  
If you have any questions, feel free to reach out via GitHub discussions or issues.