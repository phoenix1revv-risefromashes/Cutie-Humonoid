# Cutie System Requirements

## Purpose

This document defines the first engineering requirements for Cutie as a personality-first humanoid robot platform.

## Current Phase

Cutie begins as the Phoenix Lab assistant head. The first version focuses on interaction, expression, awareness, and reliability before future mobility and full humanoid expansion.

## Core Requirements

### REQ-001 — Human-Robot Interaction

Cutie must make robotic interaction feel more natural, comfortable, engaging, and memorable through an extremely witty and funny personality.

### REQ-002 — Lab Assistant Role

Cutie must serve as the Phoenix Lab assistant by helping explain projects, lab systems, robot status, and development context.

### REQ-003 —  Interaction

Cutie must support camera and microphone input, speech recognition, response generation, and speaker output.

### REQ-004 — Expressive Face Behavior

Cutie must show clear face states such as idle, listening, thinking, speaking, happy, confused, and error.

### REQ-005 — Runtime State Management

Cutie must use a robot state system to coordinate listening, thinking, speaking, errors, and future motion behavior.

### REQ-006 — Self-Speech Prevention

Cutie must avoid treating her own speaker output as user speech.

### REQ-007 — System Health Awareness

Cutie must monitor important system components such as microphone, speaker, camera, display, compute status, and future battery or mobility systems.

### REQ-008 — Modular ROS2 Architecture

Cutie must be built with modular ROS2 packages so each subsystem has a clear responsibility.

### REQ-009 — Future Mobility

Cutie’s architecture must support future wheeled mobility, navigation, docking, and emergency stop behavior.

### REQ-010 — Future Humanoid Expansion

Cutie’s architecture must support future torso, arms, manipulation, gestures, and whole-body humanoid coordination.

## Engineering Rule

Every major feature should connect back to at least one requirement.