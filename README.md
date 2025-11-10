# 📚 Bookstore API - DevOps Challenge

Welcome to the Bookstore API Challenge! A Flask-based REST API with issues that need to be identified and fixed through proper DevOps practices.

## 🎯 Challenges

Need a hint while working on the challenges? Check the Actions tab in this repository. Open your PR’s workflow run, click the step you’re stuck on, and review the logs for guidance.

### Challenge 1: CI/CD Pipeline & Branch Strategy
**The Problem**: Pipeline validation on pull requests

**Your Mission**: 
1. Create a new branch.
2. Change the debug mode in run.py (set debug=False → debug=True).
3. Open a pull request to main to trigger the CI/CD pipeline.
4. Ensure your branch passes the first-level pipeline validation.

---

### Challenge 2: Security Vulnerabilities
**The Problem**: Hard-coded sensitive information in the codebase

**Your Mission**:
1. Identify hard-coded passwords, API tokens, or other secrets.
2. Remove these credentials from the source code. (Note: Secrets are already securely stored elsewhere.)
3. Ensure no sensitive data remains so that the pipeline passes the security validation step.

---

### Challenge 3: Code Quality Issues
**The Problem**: Linting errors and logical issues in the code

**Your Mission**:
1. Identify deviations from best practices (Missing or inconsistent whitespace, Dead code / unused variables, Naming conventions / consistency, Trailing whitespace)
2. Fix or remove all deviations. (Hint: There is excatly one of each deviation in the source code)
3. Ensure branch validation passes and the pipeline confirms your code quality fixes.
   
---

### Challenge 4: Docker Build Failure
**The Problem**: Docker build process is failing

**Your Mission**:
1. Debug the Dockerfile to identify build issues
2. Fix any configuration or dependency problems preventing the container from building.
3. Ensure the container builds and runs successfully so that the CI/CD pipeline validates the build step.

---
