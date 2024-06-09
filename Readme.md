# Project Name

## Overview

This project is a web application built with Python and the Django framework. It features a dynamic interface using HTML, CSS, and JavaScript to update the website without refreshing. Stripe is used for the checkout and payment system, and Django Allauth is used for user authentication.

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- Stripe API
- Django Allauth

## Setup Instructions

### Prerequisites

Ensure you have the following installed on your system:

- Python (>= 3.x)
- pip (Python package installer)
- virtualenv (optional, but recommended for creating a virtual environment)

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/implaymo/16--Ecommerce.git
    cd 16--Ecommerce
    ```

2. **Create a virtual environment (optional but recommended)**

    ```bash
    virtualenv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

### Environment Variables

Create a `.env` file in the root directory of your project and add the following environment variables. These are required for the project to run correctly.

    STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
    STRIPE_SECRET_KEY=your_stripe_secret_key
    FIELD_ENCRYPTION_KEY=your_field_encryption_key
    EMAIL_HOST_USER=your_email_host_user
    EMAIL_HOST_PASSWORD=your_email_host_password

**Note:** Replace `your_stripe_publishable_key`, `your_stripe_secret_key`, `your_field_encryption_key`, `your_email_host_user`, and `your_email_host_password` with your actual credentials.

### Running the Project

1. **Apply database migrations**

    ```bash
    python manage.py migrate
    ```

2. **Create a superuser**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create your admin user.

3. **Run the development server**

    ```bash
    python manage.py runserver
    ```

4. Open your web browser and navigate to `http://127.0.0.1:8000` to view the website.

## Features

- User authentication, registration and Multi-factor authentication using Django Allauth
- Dynamic content updates without page refresh using JavaScript
- Stripe integration for secure payment processing
- Admin panel for managing users and orders

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

For any questions or suggestions, please reach out to [playmolegion@gmail.com].