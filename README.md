# OpenHands Test Repository

This repository serves as a test environment for [OpenHands](https://github.com/All-Hands-AI/OpenHands), an AI-powered coding assistant that helps developers write, debug, and maintain code.

## Purpose

This repository is used to:
- Test OpenHands' capabilities in real-world scenarios
- Demonstrate how OpenHands can fix issues, improve documentation, and implement features
- Provide a sandbox environment for OpenHands development and testing

## How to Use This Repository

### For OpenHands Development Team
This repository is automatically used in the OpenHands CI/CD pipeline to test new features and bug fixes. When changes are made to the OpenHands codebase, automated tests will use this repository to verify functionality.

### For Contributors
If you're contributing to OpenHands, you can use this repository to:
1. Test your changes locally before submitting a pull request
2. Verify that OpenHands can successfully navigate and modify a real repository
3. Experiment with different prompts and see how OpenHands responds

### Testing OpenHands Locally
To test OpenHands with this repository:

```bash
# Clone this repository
git clone https://github.com/RHRolun/test-openhands.git

# Start OpenHands (assuming you have it installed)
OPENHANDS_TARGET_DIR=/path/to/test-openhands openhands

# Interact with OpenHands and ask it to make changes to this repository
```

## Repository Structure
- `.github/` - GitHub workflows and issue templates
- `.git/` - Git repository metadata
- `README.md` - This file, which should be kept up-to-date

## Contributing
While this is primarily a test repository for OpenHands, improvements to the README or test cases are welcome. Please submit a pull request with your changes.

## License
This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
