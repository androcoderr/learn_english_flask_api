from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)
# Görsellerin bulunduğu klasör (proje dizininde "images" klasörü oluşturmayı unutma!)
IMAGE_FOLDER = os.path.join(os.getcwd(), 'images')

@app.route('/image/<word>', methods=['GET'])
def get_image(word):
    filename = f"{word.lower()}.png"  # Örneğin: 'apple' -> 'apple.png'
    file_path = os.path.join(IMAGE_FOLDER, filename)
    if os.path.exists(file_path):
        return send_from_directory(IMAGE_FOLDER, filename)
    else:
        abort(404, description="Image not found")

if __name__ == '__main__':
    app.run(debug=True)
