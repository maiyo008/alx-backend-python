# Python Generators: Memory-Efficient Data Processing

This repository contains tasks and examples of how to use Python generators for memory-efficient data processing. Each task demonstrates practical use cases of generators, including batch processing, pagination, and calculating aggregate functions on large datasets.

## Table of Contents

- [Overview](#overview)
- [Tasks](#tasks)
  - [Task 1: Batch Processing Large Data](#task-1-batch-processing-large-data)
  - [Task 2: Simulate Pagination](#task-2-simulate-pagination)
  - [Task 3: Calculate Average Age](#task-3-calculate-average-age)
- [How to Run](#how-to-run)
- [Examples](#examples)
- [Technologies Used](#technologies-used)

---

## Overview

This project focuses on implementing Python generator functions to handle large datasets without loading everything into memory. Generators are used to:
- Lazily load data in batches or pages.
- Calculate aggregate functions efficiently.
- Process user data based on various criteria.

---

## Tasks

### Task 1: Batch Processing Large Data

**Objective**: Create a generator to fetch and process user data in batches.

**Key Components**:
- `stream_users_in_batches(batch_size)`: A generator function to fetch rows in batches from the database.
- `batch_processing(batch_size)`: Filters users over the age of 25 in each batch.

**Features**:
- Fetches data lazily.
- Efficient filtering using Python generators.

---

### Task 2: Simulate Pagination

**Objective**: Implement a lazy pagination system using a generator.

**Key Components**:
- `paginate_users(page_size, offset)`: Fetches a specific page of users from the database.
- `lazy_paginate(page_size)`: A generator function to lazily load data pages.

**Features**:
- Only loads the required page into memory.
- Supports customizable page sizes.

---

### Task 3: Calculate Average Age

**Objective**: Use a generator to compute the average age of users efficiently.

**Key Components**:
- `stream_user_ages()`: Yields user ages one by one.
- `calculate_average_age()`: Computes the average age of users using the generator.

**Features**:
- Avoids loading the entire dataset into memory.
- Implements a memory-efficient approach to calculate aggregates.

---

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>

