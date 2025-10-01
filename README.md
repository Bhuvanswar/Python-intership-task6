# Portfolio Flask Application

A dynamic Flask web application serving Adi Bhuvaneswar's portfolio website with API endpoints and contact form functionality.

## Features

🌟 **Core Features:**
- Responsive portfolio website
- Contact form with backend processing
- RESTful API endpoints
- Resume download functionality
- Real-time message handling
- Health check endpoints

🛠️ **Technical Features:**
- Flask web framework
- JSON API responses
- Contact message logging
- Error handling
- CORS support ready
- Production-ready structure

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd "c:\Users\bhuva\OneDrive\Desktop\projects\Python-intership\Python-internship-task6"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python flask.py
   ```

4. **Access the portfolio:**
   - Portfolio: http://localhost:5000
   - API Documentation: See endpoints below

## API Endpoints

### 📄 **Portfolio Data**
- `GET /api/portfolio` - Complete portfolio data
- `GET /api/projects` - All projects
- `GET /api/projects/<id>` - Specific project
- `GET /api/skills` - Skills data
- `GET /api/education` - Education information
- `GET /api/certifications` - Certifications

### 📧 **Contact & Utilities**
- `POST /api/contact` - Submit contact form
- `GET /download/resume` - Download resume
- `GET /api/stats` - Portfolio statistics
- `GET /health` - Health check

## Contact Form

The contact form supports the following fields:
- **Name** (required)
- **Email** (required)
- **Message** (required)

Messages are logged to `contact_messages.json` for review.

## File Structure

```
├── flask.py              # Main Flask application
├── Portfolio.html        # Portfolio website
├── requirements.txt      # Python dependencies
├── contact_messages.json # Contact form submissions
└── README.md             # This file
```

## Configuration

### Environment Variables (Optional)
- `FLASK_ENV=development` - Set development mode
- `FLASK_DEBUG=1` - Enable debug mode
- `SECRET_KEY` - Set in flask.py for production

### Production Setup
1. Set `DEBUG=False` in flask.py
2. Use a proper WSGI server (gunicorn, uWSGI)
3. Set up proper logging
4. Use environment variables for sensitive data

## Development

### Adding New Projects
Edit the `portfolio_data['projects']` list in `flask.py`:

```python
{
    'id': 7,
    'title': 'New Project',
    'description': 'Project description',
    'technologies': ['Tech1', 'Tech2'],
    'github_url': 'https://github.com/username/repo',
    'demo_url': 'https://demo.com',  # Optional
    'image': 'project.jpg'           # Optional
}
```

### Customizing Contact Form
Modify the `/api/contact` endpoint in `flask.py` to:
- Send emails
- Save to database
- Add validation
- Integrate with email services

## Deployment

### Local Development
```bash
python flask.py
```

### Production (with Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 flask:app
```

### Docker (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "flask.py"]
```

## Security Considerations

⚠️ **Important for Production:**
- Change the default SECRET_KEY
- Implement rate limiting for contact form
- Add CSRF protection
- Use HTTPS
- Validate all inputs
- Set up proper logging
- Use environment variables

## License

This project is personal portfolio software for Adi Bhuvaneswar.

## Contact

- **GitHub:** https://github.com/Bhuvanswar
- **LinkedIn:** https://www.linkedin.com/in/bhuvaneswar-adi-6ba43426a/
- **Email:** your.email@example.com