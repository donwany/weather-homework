## 📘 Homework: Build & Publish a Python Weather App

### 🎯 Objective
 In this assignment, you will take a simple Python weather application and turn it into a real-world, installable Python package that others can use.

By the end, you will:
 - Work with virtual environments using UV
- Use environment variables securely
- Package Python projects (.whl)
- Publish to PyPI
- Share your project with others

### 🧩 Starter Code
 - `v15_demoy.py`
  
## 📝 Tasks
-  ✅ 1. Create a Virtual Environment (Using UV) and Activate it.
-  🔑 2. Get API Key & Use .env
-  🏗️ 3. Structure Your Project Properly
-  📦 4. Build Your Package (.whl)
-  🚀 5. Publish to PyPI
-  🌍 6. Install Your Package
   -  `pip install your-project-name`
   -  `from weather_app import OpenWeatherMap`
- 🧑‍💻 7. Push to GitHub
- 👥 8. Share With Others


## 🏗️ Structure Your Project Properly
```
weather-app/
│
├── src/
│   └── weather_app/
│       ├── __init__.py
│       └── client.py
│
├── .env
|-- main.py
├── pyproject.toml
├── README.md
└── .gitignore
```

## 🧠 Grading Criteria

| Criteria                  | Points  |
| ------------------------- | ------- |
| Virtual environment setup | 10      |
| API key + `.env` usage    | 15      |
| Project structure         | 15      |
| Package build (`.whl`)    | 20      |
| PyPI deployment           | 20      |
| GitHub repo               | 10      |
| Sharing/testing           | 10      |
| **Total**                 | **100** |
