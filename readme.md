<p align="center">
  <img src="blog/media/django-blog-bg.png" alt="Django Blog Logo" width="400">
</p>

This is a minimalistic blog built using Django Admin for content management and Bootstrap for styling.

## Features

- User-friendly Django Admin interface for managing blog content.
- Bootstrap for a clean and responsive design.
- Simple and lightweight structure for easy customization.

<p align="center">
  <img src="blog/media/preview.gif" alt="Django Blog Preview">
</p>

## Getting Started

### Prerequisites

- Python (3.6 or higher)
- Django (3.x)
- Bootstrap (5.x)

### Installation

1. Clone the repository:

    ```
    git clone https://github.com/roderiano/django-blog.git
    ```

2. Create and activate a virtual environment:

    ```
    python -m venv venv
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```
    python manage.py migrate
    ```

5. Create a superuser for accessing the Django Admin:

    ```
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```
    python manage.py runserver
    ```

7. Open your browser and navigate to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to log in and start managing your blog content.


### Running Tests

To run the tests, use the following command:

```
python manage.py test
```

## Usage

1. Access the Django Admin interface to create, edit, and delete blog posts.
2. Customize the Bootstrap templates in the `templates` directory to modify the appearance of your blog.
3. Extend the functionality by adding additional Django apps, models, or views as needed.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to discuss new features, please open an issue to start a discussion.

For implementing new features or fixing bugs:

1. Fork the repository.

2. Create a new branch from the `develop` branch:

    ```bash
    git checkout -b feature/your-feature-name
    ```

3. Make your changes and ensure the code follows the project's coding standards.

4. Test your changes thoroughly.

5. Commit your changes:

    ```bash
    git commit -m "Add your concise and meaningful commit message"
    ```

6. Push your branch to your fork:

    ```bash
    git push origin feature/your-feature-name
    ```

7. Open a pull request against the `develop` branch, describing your changes and referencing the related issue.

8. Your pull request will be reviewed, and once approved, it will be merged.

Thank you for contributing to DevReport!

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
