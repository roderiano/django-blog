<p align="center">
  <img src="blog/media/django-blog-bg.png" alt="Django Blog Logo" width="400">
</p>

This is a minimalistic blog built using Django Admin for content management and Bootstrap for styling.

## Features

- User-friendly Django Admin interface for managing blog content.
- Bootstrap for a clean and responsive design.
- Simple and lightweight structure for easy customization.

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

Contributions are welcome! Feel free to open issues, create pull requests, or suggest improvements.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
