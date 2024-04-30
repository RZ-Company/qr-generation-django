from django.shortcuts import render
from .forms import LinkForm
import qrcode
from django.http import HttpResponse

def generate_qr(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            response = HttpResponse(content_type="image/png")
            img.save(response, "PNG")
            return response
    else:
        form = LinkForm()
    
    return render(request, 'qrapp/qr_form.html', {'form': form})
