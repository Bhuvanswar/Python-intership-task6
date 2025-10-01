from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from datetime import datetime
import json

app = Flask(__name__, static_folder='.')

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['DEBUG'] = True

# Portfolio data
portfolio_data = {
    'personal_info': {
        'name': 'Adi Bhuvaneswar',
        'title': 'Software Developer & AI Enthusiast',
        'email': 'your.email@example.com',
        'phone': '+91 9876543210',
        'linkedin': 'https://www.linkedin.com/in/bhuvaneswar-adi-6ba43426a/',
        'github': 'https://github.com/Bhuvanswar',
        'location': 'India'
    },
    'skills': {
        'programming': ['Python', 'JavaScript', 'Java', 'C++', 'C', 'Kotlin'],
        'web_development': ['React', 'Node.js', 'HTML5', 'CSS3', 'Flask'],
        'data_science': ['Pandas', 'NumPy', 'Matplotlib', 'OpenCV', 'Scikit-learn'],
        'tools': ['Git', 'GitHub', 'MongoDB', 'MySQL', 'Docker', 'VS Code']
    },
    'projects': [
        {
            'id': 1,
            'title': 'Number Plate Recognition System',
            'description': 'An AI-powered system for automatic number plate recognition using computer vision and machine learning techniques.',
            'technologies': ['Python', 'OpenCV', 'Machine Learning'],
            'github_url': 'https://github.com/Bhuvanswar/Numberplate_recognition',
            'demo_url': None,
            'image': None
        },
        {
            'id': 2,
            'title': 'Machine Learning Projects',
            'description': 'Collection of machine learning projects including data analysis, model building, and visualization techniques.',
            'technologies': ['Python', 'Jupyter Notebook', 'Machine Learning'],
            'github_url': 'https://github.com/Bhuvanswar/ml',
            'demo_url': None,
            'image': None
        },
        {
            'id': 3,
            'title': 'SIH Project',
            'description': 'Smart India Hackathon project developed using Kotlin for innovative mobile solutions.',
            'technologies': ['Kotlin', 'Android', 'Mobile App'],
            'github_url': 'https://github.com/Bhuvanswar/SIH',
            'demo_url': None,
            'image': None
        },
        {
            'id': 4,
            'title': 'Personality Prediction',
            'description': 'Machine learning project for predicting personality traits (Extrovert/Introvert) using data analysis.',
            'technologies': ['Python', 'Machine Learning', 'Data Analysis'],
            'github_url': 'https://github.com/Bhuvanswar/Extrovert-Introvert',
            'demo_url': None,
            'image': None
        },
        {
            'id': 5,
            'title': 'Garment Classification',
            'description': 'Deep learning project for automated garment classification using computer vision and neural networks.',
            'technologies': ['Python', 'Deep Learning', 'Computer Vision'],
            'github_url': 'https://github.com/Bhuvanswar/garment-classification',
            'demo_url': None,
            'image': None
        },
        {
            'id': 6,
            'title': 'Java Development Projects',
            'description': 'Collection of Java programming projects demonstrating object-oriented programming and software development skills.',
            'technologies': ['Java', 'OOP', 'Software Development'],
            'github_url': 'https://github.com/Bhuvanswar/CODSOFT-java-',
            'demo_url': None,
            'image': None
        }
    ],
    'education': [
        {
            'degree': 'Bachelor of Technology in Computer Science',
            'institution': 'NRI INSTITUTE OF TECHNOLOGY',
            'year': '2025',
            'specialization': 'AIML (ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING)',
            'coursework': ['Machine Learning', 'Deep Learning', 'Data Structures and Algorithms', 
                          'Object-Oriented Programming', 'Database Management Systems', 
                          'Software Engineering', 'Web Development', 'Computer Networks']
        },
        {
            'degree': 'Higher Secondary Education',
            'institution': 'SIR C R REDDY POLYTECHNIC',
            'year': '2022',
            'specialization': 'Computer Science Engineering',
            'coursework': ['Java Programming', 'Python Programming', 'HTML,CSS,JS', 
                          'Data Structures and Algorithms', 'Object-Oriented Programming', 
                          'Database Management Systems']
        }
    ],
    'certifications': [
        {
            'title': 'Python Programming',
            'institution': 'Your Institution',
            'description': 'Completed comprehensive Python programming course covering core concepts, data structures, and practical applications.',
            'certificate_url': '#'
        },
        {
            'title': 'Data Science Fundamentals',
            'institution': 'Your Institution',
            'description': 'Learned data analysis, visualization techniques, and machine learning basics using Python libraries.',
            'certificate_url': '#'
        },
        {
            'title': 'Web Development',
            'institution': 'Your Institution',
            'description': 'Full-stack web development training covering HTML, CSS, JavaScript, and modern frameworks.',
            'certificate_url': '#'
        },
        {
            'title': 'AI & Machine Learning',
            'institution': 'Your Institution',
            'description': 'Advanced course in artificial intelligence and machine learning algorithms and applications.',
            'certificate_url': '#'
        }
    ]
}

@app.route('/')
def index():
    """Render the main portfolio page"""
    return send_from_directory('.', 'Portfolio.html')

@app.route('/images/<path:filename>')
def serve_images(filename):
    """Serve image files"""
    return send_from_directory('.', filename)

@app.route('/<path:filename>')
def serve_static_files(filename):
    """Serve static files like images, CSS, JS"""
    # Check if file exists to avoid serving non-existent files
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/api/portfolio')
def get_portfolio_data():
    """API endpoint to get portfolio data as JSON"""
    return jsonify(portfolio_data)

@app.route('/api/projects')
def get_projects():
    """API endpoint to get all projects"""
    return jsonify(portfolio_data['projects'])

@app.route('/api/projects/<int:project_id>')
def get_project(project_id):
    """API endpoint to get a specific project"""
    project = next((p for p in portfolio_data['projects'] if p['id'] == project_id), None)
    if project:
        return jsonify(project)
    return jsonify({'error': 'Project not found'}), 404

@app.route('/api/skills')
def get_skills():
    """API endpoint to get skills data"""
    return jsonify(portfolio_data['skills'])

@app.route('/api/education')
def get_education():
    """API endpoint to get education data"""
    return jsonify(portfolio_data['education'])

@app.route('/api/certifications')
def get_certifications():
    """API endpoint to get certifications data"""
    return jsonify(portfolio_data['certifications'])

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field.capitalize()} is required'}), 400
        
        # Here you would typically:
        # 1. Save to database
        # 2. Send email notification
        # 3. Send confirmation email to user
        
        # For now, we'll just log the message and return success
        contact_message = {
            'name': data['name'],
            'email': data['email'],
            'message': data['message'],
            'timestamp': datetime.now().isoformat(),
            'ip_address': request.remote_addr
        }
        
        # Log the contact message (in production, save to database)
        print(f"New contact message: {contact_message}")
        
        # You can save to a file for now
        try:
            with open('contact_messages.json', 'a') as f:
                f.write(json.dumps(contact_message) + '\n')
        except Exception as e:
            print(f"Error saving contact message: {e}")
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.'
        })
    
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your message'}), 500

@app.route('/api/stats')
def get_stats():
    """API endpoint to get portfolio statistics"""
    stats = {
        'total_projects': len(portfolio_data['projects']),
        'total_skills': sum(len(skills) for skills in portfolio_data['skills'].values()),
        'total_certifications': len(portfolio_data['certifications']),
        'total_education': len(portfolio_data['education']),
        'last_updated': datetime.now().isoformat()
    }
    return jsonify(stats)

@app.route('/download/resume')
def download_resume():
    """Serve resume file for download"""
    # Check if resume file exists
    resume_files = ['resume.pdf', 'Resume.pdf', 'CV.pdf', 'cv.pdf']
    for filename in resume_files:
        if os.path.exists(filename):
            return send_from_directory('.', filename, as_attachment=True)
    
    return jsonify({'error': 'Resume file not found'}), 404

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create contact messages file if it doesn't exist
    if not os.path.exists('contact_messages.json'):
        with open('contact_messages.json', 'w') as f:
            pass
    
    print("\n" + "="*60)
    print("🚀 PORTFOLIO FLASK APP STARTING")
    print("="*60)
    print(f"📱 Portfolio URL: http://localhost:5000")
    print(f"🔗 API Endpoints:")
    print(f"   • GET  /api/portfolio - Full portfolio data")
    print(f"   • GET  /api/projects - All projects")
    print(f"   • GET  /api/skills - Skills data")
    print(f"   • POST /api/contact - Contact form")
    print(f"   • GET  /download/resume - Download resume")
    print(f"   • GET  /health - Health check")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)