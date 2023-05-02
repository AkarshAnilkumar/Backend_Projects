from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import TemplateView
# from .models import Member
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404, redirect
# from .models import Task
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def hi(request):
    return render(request, 'base.html')

# def pie_chart(A,B,C):
def pie_chart(request):

    labels = ['Apples', 'Bananas', 'Oranges']
    data = [30, 40, 20]
    # data = [A,B,C]

    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%')
    ax.set_title('Fruit Distribution')

    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    image = buffer.getvalue()

    encoded_image = base64.b64encode(image).decode('utf-8')

    context = {'chart': encoded_image}
    # return context
    return render(request, 'pie_chart.html', context)

# def forms(request):
#     if request.method == 'POST':
#         A = request.POST.get('A')
#         B = request.POST.get('B')
#         C = request.POST.get('C')
        
#         # pass the data to another function for processing
#         context = pie_chart(A,B,C)
        
#         # render a response template with the result
#         # context = {'result': result}
#         # return HttpResponse(request, forms.html)
#         return render(request, 'forms.html', context)
