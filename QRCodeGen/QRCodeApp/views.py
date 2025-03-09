from django.shortcuts import render, redirect
from .models import QRCode
import qrcode as qr
import datetime
import os
import io
from django.core.files import File
from django.core.files.images import ImageFile
from UserApp.models import Profile
from django.core.files.storage import FileSystemStorage
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask
from django.http import FileResponse, HttpRequest
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def show_qrcodegen(request: HttpRequest):
    image_file = None
    user = request.user
    profile = Profile.objects.get(user = user)
    
    if request.method == "POST":
        if request.POST.get("button") == "gen":
            name = request.POST.get("name")
            url = request.POST.get("url")
            description = request.POST.get("description") 
            logo = request.FILES.get("logo")

            if profile.subscription == "free":
                logo = None
                bg_color = (255, 255, 255)
                qrcode_color = (0, 0, 0)
            else:
                bg_color = tuple(int(request.POST.get("bg_color").lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                qrcode_color  = tuple(int(request.POST.get("qrcode_color").lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

            record = QRCode.objects.create(name = name, description = description, url = url, expire_date = datetime.datetime.now() + datetime.timedelta(weeks=4))

            qrcode = qr.QRCode(version = 1, box_size = 10, border = 4, error_correction= qr.ERROR_CORRECT_H)
            qrcode.add_data(f"http://127.0.0.1:8000/qrcode/reroute/{record.id}")
            qrcode.make(fit=True)
            
            fss = FileSystemStorage()
            logo_path = os.path.join("logo", "logo.png")
            
            if logo != None:
                
                logo_name = fss.save(name = logo_path, content = logo)
                qrcode_img = qrcode.make_image(image_factory = StyledPilImage, embeded_image_path = f"media/{logo_name}", color_mask = SolidFillColorMask(back_color = bg_color, front_color = qrcode_color))
            else:
                qrcode_img = qrcode.make_image(image_factory = StyledPilImage, color_mask = SolidFillColorMask(back_color = bg_color, front_color = qrcode_color))
       
            fss.delete(name = logo_path)
            
            img_name = os.path.join("images", "qrcode.png")
            blob = io.BytesIO()
            qrcode_img.save(blob, "PNG")

            record.image.save(name = img_name, content = File(blob))
            
            return render(request, "QRCodeApp/qrcodegen2.html", context = {"record": record, "sub": profile.subscription})
            
        elif request.POST.get("button") == "save": 
            prems = {"free": 1, "standart": 10, "pro":100}
            qrcodes = QRCode.objects.filter(owner = profile)
            
            if qrcodes.__len__() < prems[profile.subscription]:
                record = request.POST.get('record')
                record = record.split(" ")[-1].replace("(", "").replace(")", "")

                save_record = QRCode.objects.get(id=record)
                print(save_record)
                save_record.owner = profile
                save_record.save()
        
    return render(request, "QRCodeApp/qrcodegen2.html", context = {"record": None, "sub": profile.subscription})

@login_required
def show_qrcodeview(request: HttpRequest):
    user = request.user
    profile = Profile.objects.get(user = user)
    qrcodes = QRCode.objects.filter(owner = profile)
    
    if request.method == "POST":
        id = request.POST.get("id")
        if request.POST.get("button") == "save":
            qrcode = QRCode.objects.get(id = id)
            return FileResponse(qrcode.image.open(), as_attachment = True)
        elif request.POST.get("button") == "delete":
            QRCode.objects.get(id = id).delete()
    
    
    return render(request, "QRCodeApp/qrcodeview.html", context = {"qrcodes": qrcodes, "sub": profile.subscription, "qrc_count": qrcodes.__len__})


def qrcode_reroute(request, id):
    qrcode = QRCode.objects.get(id = id)
    if timezone.now() < qrcode.expire_date:
        return redirect(qrcode.url)
    else:
        return render(request, template_name = "QRCodeApp/rerouteerror.html")
    