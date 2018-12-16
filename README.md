# Code Companion for "Overview and Comparison of Gate Level Quantum Software Platforms"

Code used in the paper [Overview and Comparison of Gate Level Quantum Software Platforms](https://arxiv.org/abs/1807.02500), also featured on [Quantum Computing Report](https://quantumcomputingreport.com/) and translated into Russian [at this link](https://habr.com/post/418505/).

This code is updated to work with newer versions of the software platforms. The code in the paper is relevant for Forest v1.9.0, QISKit v0.5.4, ProjectQ v0.3.6, and QDK v0.2.1802.2202 (pre-release). The code in the repository is relevant for the following versions:

* [Forest](https://github.com/rigetti) v2.1.1.
* [QISKit](https://github.com/QISKit) v0.6.1.
* [ProjectQ](https://github.com/ProjectQ-Framework/ProjectQ) v0.4.1.
* [QDK](https://github.com/Microsoft/Quantum) v0.2.1802.2202 (pre-release).

The current versions of each platform can be determined by following the links above. 

# Version Control
To check what version of each platform is installed using `pip` and `grep` (standard on most linux OS's), one can do `pip freeze | grep <program>`. For example, `pip freeze | grep pyquil` will return `pyquil==2.1.1` if this version is installed. To upgrade to the latest release of a program using `pip`, one can do `pip install --upgrade <program>`. (See appropriate documentation if this fails.)
