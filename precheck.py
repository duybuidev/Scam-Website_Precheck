from flask import Flask, render_template, request
from scraper import get_page_content, extract_links, extract_titles # Import các hàm từ scraper.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        return "Vui lòng nhập một URL hợp lệ!", 400

    # Gọi hàm từ file scraper.py
    soup = get_page_content(url)

    if soup:
        # Sử dụng các hàm từ scraper.py để lấy dữ liệu
        titles = extract_titles(soup)
        links = extract_links(soup)
        return render_template('results.html', url=url, titles=titles, links=links)
    else:
        return "Không thể cào dữ liệu từ URL này.", 500

if __name__ == '__main__':
    app.run(debug=True)
