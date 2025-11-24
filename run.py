from app import create_app

app = create_app()                    # 1) build the app using the factory

if __name__ == "__main__":            # 2) run only when we execute this file directly
    app.run(debug=True)               # 3) start Flask’s dev server on port 5000
