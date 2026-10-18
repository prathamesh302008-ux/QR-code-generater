
import base64
import io

import qrcode
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def home(request):
    context = {
        "qr_image": None,
        "entered_text": "",
        "qr_size": "medium",
        "error": None,
    }

    if request.method == "POST":
        text = request.POST.get("qr_text", "").strip()
        size = request.POST.get("qr_size", "medium")

        context["entered_text"] = text
        context["qr_size"] = size

        if not text:
            context["error"] = "Please enter some text or a website URL."
        elif len(text) > 2000:
            context["error"] = "Maximum allowed length is 2000 characters."
        elif size not in ("small", "medium", "large"):
            context["error"] = "Please select a valid QR size."
            context["qr_size"] = "medium"
        else:
            box_sizes = {"small": 6, "medium": 10, "large": 14}

            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=box_sizes[size],
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)

            image = qr.make_image(
                fill_color="#111827",
                back_color="white",
            ).convert("RGB")

            buffer = io.BytesIO()
            image.save(buffer, format="PNG")
            encoded = base64.b64encode(buffer.getvalue()).decode("ascii")

            context["qr_image"] = f"data:image/png;base64,{encoded}"

    return render(request, "generator/index.html", context)
