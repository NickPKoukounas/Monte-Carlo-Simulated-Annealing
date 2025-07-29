# Optimal Rectangle Fitting Over Implicit Functions

This project implements a hybrid **Simulated Annealing** and **Monte Carlo Integration** algorithm to find the optimal placement and rotation of a rectangle that **maximizes area inside a region defined by an implicit function**, such as a clover-shaped curve.

## Overview

The algorithm:
- Defines a rectangle with variable translation `(Dx, Dy)` and rotation `r` by translating into polar coordinates
- Evaluates how much of the rectangle lies inside a region defined by an implicit function (e.g., a clover shape)
- Uses **Monte Carlo sampling** to approximate the overlap area
- Applies **Simulated Annealing** to optimize the rectangle’s position and rotation for maximum overlap

## Problem Statement

> Given a fixed-size rectangle and a 2D region defined implicitly by a function  
> (e.g.,  \\( (x^2 + y^2)^3 - 4x^2y^2 < 0 \\)), find the translation and rotation  
> that maximizes the rectangle's area within this region.

## How It Works

1. **Rectangle Definition**: A unit-width rectangle with height \\( \frac{1}{\sqrt{2}} \\) is defined and translated/rotated.
2. **Monte Carlo Integration**: Random points are generated within a bounding box to estimate what fraction of the rectangle lies inside the implicit region.
3. **Cost Function**: This overlap area is used as the objective function.
4. **Simulated Annealing**: The algorithm iteratively checks local moves of the rectangle's parameters and accepts changes based on improvement or probabilistic tolerance of worse states.

