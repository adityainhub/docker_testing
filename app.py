from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
products = [
    {
  "name": "Aditya",
  "age": 22,
  "location": "Bengaluru, India",
  "education": {
    "degree": "Computer Science Engineering",
    "semester": 5
  },
  "skills": {
    "programming_languages": ["C++", "Python", "JavaScript"],
    "frontend": ["HTML", "CSS", "React"],
    "backend": ["Spring Boot", "Flask"],
    "databases": ["MySQL", "MongoDB"],
    "security": ["JWT"],
    "machine_learning": ["Decision Trees", "Multilayer Perceptrons"],
    "networking": ["ARP", "ICMP", "DHCP", "NAT"]
  },
  "projects": [
    {
      "name": "E-commerce Application",
      "description": "A full-stack e-commerce app with JWT authentication and MySQL database.",
      "technologies": ["HTML", "CSS", "JavaScript", "MySQL", "JWT"]
    },
    {
      "name": "Traffic Light Control Model",
      "description": "A model to adjust traffic light duration based on incoming traffic volume.",
      "technologies": ["Python", "OpenCV"]
    },
    {
      "name": "GenAI Tool for E-commerce",
      "description": "A system that converts social media posts into Amazon product listings.",
      "technologies": ["MongoDB", "Machine Learning", "OpenCV"]
    },
    {
      "name": "Plagiarism Detection System",
      "description": "A tool using JPlag to detect plagiarism in code submissions from LeetCode.",
      "technologies": ["Spring Boot", "React", "AWS S3", "JPlag"]
    }
  ],
  "internship": {
    "company": "VISA",
    "role": "Intern"
  },
  "goals": {
    "short_term": "Prepare for placements and improve communication skills.",
    "long_term": "Gain 2 years of job experience and pursue a master's degree abroad."
  },
  "socials": {
    "instagram": {
      "posts": 1,
      "followers": 0,
      "following": 15
    }
  }
}
]

# GET all products
@app.route('/intro', methods=['GET'])
def get_products():
    print("Hello users.. I am Aditya the developer")

    return jsonify(products)

# GET single product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return jsonify(product) if product else ('', 404)

# POST a new product
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify(new_product), 201

# DELETE a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
