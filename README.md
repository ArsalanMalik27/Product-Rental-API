# CINCH - Product Rental API

## Overview

APIs for a Product Rental Service. You are able to add and get Products, Attribute, Attribute Values, Region, Rental Periods and Pricing according to Rental Period and Region.  

## Prerequisites

Ensure you have the following installed on your system:

* Python 3.8+

* Poetry

* PostgreSQL

Installation

### 1. Clone the Repository

`git clone https://github.com/ArsalanMalik27/Product-Rental-API.git`
`cd Product-Rental-API`

### 2. Install Dependencies

`poetry install`

### 3. Configure Environment Variables

copy `.env.example` to `.env`

### 4. Initialize Alembic Migrations

`poetry run alembic init migrations`

### 5. Run Database Migrations
`poetry run alembic upgrade head`


## Usage

### Run the application using:

`poetry run uvicorn app.server:main_app --reload`

### To generate a new Alembic migration:

`poetry run alembic revision --autogenerate -m "Describe changes"`

### Apply migrations:

`poetry run alembic upgrade head`

### Rollback the last migration:

`poetry run alembic downgrade -1`

## Deployment

For production, install dependencies without development packages:

`poetry install`