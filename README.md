# Cutie Humoinoid

[![Repo Hygiene](https://github.com/phoenix1revv-risefromashes/Cutie-Humonoid/actions/workflows/repo_hygiene.yml/badge.svg?branch=main)](https://github.com/phoenix1revv-risefromashes/Cutie-Humonoid/actions/workflows/repo_hygiene.yml)
[![ROS2 Build](https://github.com/phoenix1revv-risefromashes/Cutie-Humonoid/actions/workflows/ros2_build.yml/badge.svg?branch=main)](https://github.com/phoenix1revv-risefromashes/Cutie-Humonoid/actions/workflows/ros2_build.yml)

Cutie is an extremely witty and funny humanoid robot assistant engineered to bring robotic interaction closer to natural human interaction.

Cutie is a witty humanoid robot assistant being engineered from the ground up as a serious ROS2 robotics platform.
The purpose is to make Human-Robot-Interaction feel more natural, comfortabale and memorable. 

In the short term, Cutie will serve as the Phoenix Lab assistant, helping with project explanations, lab interaction, system awareness, and playful human-robot communication. In the long term, however, she will evolve into a full humanoid robot platform capable of moving, perceiving, assisting, expressing emotion, and interacting naturally with people across labs, public spaces, events, education, and other real-world environments.


## CI/CD

Cutie-Humonoid uses GitHub Actions to protect the repository and verify ROS2 workspace health.

Current checks:

- **Repo Hygiene** — blocks generated ROS2 folders, logs, recordings, secret-like files, and large model files from being committed.
- **ROS2 Build** — builds the ROS2 workspace on a clean Ubuntu 22.04 GitHub runner using ROS2 Humble and `colcon build`.

These checks help confirm that the project is not only working locally, but can also build from a clean environment.