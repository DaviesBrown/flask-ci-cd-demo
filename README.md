# Flask CI/CD Demo

A demonstration Flask application with a complete CI/CD pipeline using GitHub Actions, Docker, and GitHub Container Registry.

## 🚀 Features

- **Automated Testing**: Runs pytest with coverage reporting
- **Code Linting**: Enforces code quality with flake8
- **Docker Support**: Containerized application ready for deployment
- **Multi-version Testing**: Tests against Python 3.10 and 3.11
- **Automated Deployment**: Simulated staging deployment pipeline
- **Container Registry**: Automatically pushes images to GitHub Container Registry (ghcr.io)

## 📁 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD pipeline configuration
├── app.py                  # Flask application
├── test_app.py             # Unit tests
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container image definition
└── README.md               # This file
```

## 🛠️ Local Development

### Prerequisites

- Python 3.10 or 3.11
- pip
- Docker (optional, for container testing)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-ci-cd-demo.git
   cd flask-ci-cd-demo
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```
   Visit `http://localhost:5000` in your browser

4. **Run tests**
   ```bash
   pytest
   # or with coverage
   coverage run -m pytest
   coverage report -m
   ```

5. **Run linting**
   ```bash
   flake8 .
   ```

## 🐳 Docker

### Build the image
```bash
docker build -t flask-ci-cd-demo:latest .
```

### Run the container
```bash
docker run -p 5000:5000 flask-ci-cd-demo:latest
```

### Pull from GitHub Container Registry
```bash
docker pull ghcr.io/yourusername/flask-ci-cd-demo:latest
docker run -p 5000:5000 ghcr.io/yourusername/flask-ci-cd-demo:latest
```

## 🔄 CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) automatically:

### On Push/Pull Request to `main`:

1. **Build, Lint & Test** (Matrix: Python 3.10, 3.11)
   - Checks out code
   - Sets up Python environment
   - Installs dependencies
   - Runs flake8 linting
   - Executes tests with coverage
   - Uploads coverage reports as artifacts

2. **Docker Build & Push**
   - Builds Docker image
   - Pushes to GitHub Container Registry (ghcr.io)
   - Tags with `latest`

3. **Simulated Deployment**
   - Deploys to staging environment (simulated)
   - Runs in GitHub Actions environment: `staging`

## 🔐 Setup Instructions

### For Your Own Repository:

1. **Fork/Clone this repository**

2. **Configure GitHub Actions Permissions**
   - Go to Repository Settings → Actions → General
   - Under "Workflow permissions", enable "Read and write permissions"
   - Check "Allow GitHub Actions to create and approve pull requests"

3. **Set up GitHub Container Registry** (Optional)
   - Create a Personal Access Token (PAT) with `write:packages` scope
   - Add it as a repository secret named `CR_PAT`
   - Or use the default `GITHUB_TOKEN` (requires workflow permissions)

4. **Create Staging Environment** (Optional)
   - Go to Repository Settings → Environments
   - Create a new environment named `staging`
   - Add protection rules if needed

5. **Push to main branch**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

## 📊 Workflow Status

![CI/CD Pipeline](https://github.com/yourusername/flask-ci-cd-demo/actions/workflows/ci.yml/badge.svg)

## 🧪 Testing

Tests are written using pytest and located in `test_app.py`. Coverage reports are generated automatically in the CI pipeline.

Run tests locally:
```bash
pytest -v
coverage run -m pytest
coverage report -m
coverage html  # Generate HTML report
```

## 📝 Requirements

See `requirements.txt` for Python dependencies:
- Flask
- pytest
- coverage
- flake8

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🙋 Troubleshooting

### Docker push fails with "denied: installation not allowed"
- Ensure workflow has `packages: write` permission
- Verify repository settings allow Actions to write packages
- Check that `CR_PAT` token has correct scopes

### Linting fails
- Run `flake8 .` locally to see issues
- Fix code style issues or update `.flake8` config

### Tests fail locally but pass in CI
- Ensure you're using the same Python version
- Check that all dependencies are installed
- Clear pytest cache: `pytest --cache-clear`

## 📧 Contact

Your Name - [@yourusername](https://github.com/yourusername)

Project Link: [https://github.com/yourusername/flask-ci-cd-demo](https://github.com/yourusername/flask-ci-cd-demo)