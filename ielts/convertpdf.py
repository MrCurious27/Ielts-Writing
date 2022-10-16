from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from xhtml2pdf import pisa

import os

from django.contrib.staticfiles import finders

def link_callback(uri, rel):
    sUrl = settings.STATIC_URL
    sRoot = settings.STATIC_ROOT

    if uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))

    if not os.path.isfile(path):
        raise Exception('media URI must start with %s or %s' % (sUrl))
    return path

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result,  link_callback=link_callback)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
