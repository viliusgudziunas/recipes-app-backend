import os

from project.app import create_app

app = create_app(os.environ.get("ENV") or "default")

if __name__ == "__main__":
    app.run(debug=True)
