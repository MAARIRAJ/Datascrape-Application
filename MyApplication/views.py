from django.shortcuts import render  # type: ignore
import requests                        # type: ignore
from bs4 import BeautifulSoup          # type: ignore
from .models import ScrapedData
import pytesseract
from PIL import Image
from io import BytesIO
import logging

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def scrape_website(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text_elements = soup.find_all(string=True)

           
            text_content = [element.strip() for element in text_elements if element.strip()]

           
            data = '\n'.join(text_content)

            scraped_data = ScrapedData.objects.create(url=url, data=data)
            scraped_data.save()

            return render(request, 'result.html', {'data': data})
        else:
            error_message = "Failed to scrape the website. Please try again."
            return render(request, 'index.html', {'error_message': error_message})
    else:
        return render(request, 'index.html')




logger = logging.getLogger(__name__)

def scrape_image(request):
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        try:
            response = requests.get(image_url, timeout=20)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            content_type = response.headers.get('Content-Type')
            if 'image' not in content_type:
                error_message = f"The URL did not return an image. Content-Type: {content_type}"
                logger.error(error_message)
                return render(request, 'result.html', {'error_message': error_message})
        except requests.exceptions.RequestException as e:
            error_message = f"Failed to fetch image from the provided URL: {str(e)}"
            logger.error(error_message)
            return render(request, 'result.html', {'error_message': error_message})
        
        try:
            # Open the image from the response content
            image = Image.open(BytesIO(response.content))
            
            # Extract text from the image using pytesseract
            extracted_text = pytesseract.image_to_string(image)
            
            # Pass the extracted text to the template
            return render(request, 'result.html', {'image_data': extracted_text})
        except Exception as e:
            error_message = f"Failed to process image: {str(e)}"
            logger.error(error_message)
            return render(request, 'result.html', {'error_message': error_message})
    else:
        return render(request, 'result.html', {'error_message': 'Invalid request method'})

    
def results(request):
    
    data = {'key': 'value'}  
    return render(request, 'result.html', {'data': data})





#https://funteacherfiles.com/wp-content/uploads/2020/08/Slide2-46.jpg