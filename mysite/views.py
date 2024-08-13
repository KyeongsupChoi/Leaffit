# -*- encoding: utf-8 -*-

# Import necessary modules
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from docx import settings

# Import ReportLab modules for PDF generation
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet

# Import python-docx for Word document generation
from docx import *
from docx.shared import Inches

# Import custom form
from .forms import WendlerForm

from reportlab.pdfgen import canvas
import io

# Global variable to store Wendler workout data
global_wendler_list = {}

# Function to generate PDF view
def some_view(request):
    # Set up styles for PDF
    styles = getSampleStyleSheet()
    style = styles["BodyText"]

    # Create a buffer to store PDF
    buffer = io.BytesIO()
    canv = canvas.Canvas(buffer)

    # Prepare data for the table
    empty_list = []
    empty_list.append(['Week No.', 'Set 1', "Set 2", "Set 3", "Set 4"])
    for week in range(1, 5):
        empty_list.append([f'Week {week}'] + list(global_wendler_list[f'Week {week}'].values()))

    print(empty_list)

    # Create header
    header = Paragraph("<bold><font size=18>Wendler Exercise List</font></bold>", style)

    # Create table
    data = empty_list
    t = Table(data)
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                           ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))
    
    # Set alternating row colors
    data_len = len(data)
    for each in range(data_len):
        bg_color = colors.whitesmoke if each % 2 == 0 else colors.lightgrey
        t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

    # Draw header and table on the canvas
    aW, aH = 540, 720
    w, h = header.wrap(aW, aH)
    header.drawOn(canv, 72, 800)
    aH = aH - h
    w, h = t.wrap(aW, aH)
    t.drawOn(canv, 72, aH - h)
    canv.save()

    # Prepare response
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='WendlerSheet.pdf')

# Function to generate Word document view
def word_doc_view(request):
    document = Document()
    docx_title="WendlerSheet.docx"

    # Add content to the document
    document.add_paragraph("Wendler Exercise List")
    for week in range(1, 5):
        document.add_paragraph(f'Week {week}' + str(global_wendler_list[f'Week {week}'])[1:-1])

    document.add_page_break()

    # Prepare document for download
    f = io.BytesIO()
    document.save(f)
    length = f.tell()
    f.seek(0)
    response = HttpResponse(
        f.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename=' + docx_title
    response['Content-Length'] = length
    return response

# Main view function for Wendler calculator
def wendler_view(request):
    if request.method == 'POST':
        form = WendlerForm(request.POST)
        if form.is_valid():
            # Get the one rep max weight from the form
            number = int(request.POST['weight'])
            global global_wendler_list

            # Wendler 531 percentage list
            percentage_list = [0.40, 0.50, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

            # Calculate weights for each percentage
            calculated_dict = {}
            for num in percentage_list:
                calc_num = (number * num - 20) / 2
                # Round to nearest 2.5 kg
                if (calc_num % 2.5) < 1.25:
                    calc_num = calc_num - (calc_num % 2.5)
                else:
                    calc_num = calc_num + 2.5 - (calc_num % 2.5)
                calc_num = max(calc_num, 0)  # Ensure non-negative
                calculated_dict[num] = calc_num

            # Create exercise dictionary with sets for each week
            exercise_dict = {
                'Week 1': {'Set 1': f"{calculated_dict[0.4]}kgx5", 'Set 2': f"{calculated_dict[0.65]}kgx5",
                           'Set 3': f"{calculated_dict[0.75]}kgx5", 'Set 4': f"{calculated_dict[0.85]}kgx5"},
                'Week 2': {'Set 1': f"{calculated_dict[0.4]}kgx3", 'Set 2': f"{calculated_dict[0.7]}kgx3",
                           'Set 3': f"{calculated_dict[0.8]}kgx3", 'Set 4': f"{calculated_dict[0.9]}kgx3"},
                'Week 3': {'Set 1': f"{calculated_dict[0.4]}kgx5", 'Set 2': f"{calculated_dict[0.75]}kgx5",
                           'Set 3': f"{calculated_dict[0.85]}kgx3", 'Set 4': f"{calculated_dict[0.95]}kgx1"},
                'Week 4': {'Set 1': f"{calculated_dict[0.4]}kgx5", 'Set 2': f"{calculated_dict[0.4]}kgx5",
                           'Set 3': f"{calculated_dict[0.5]}kgx5", 'Set 4': f"{calculated_dict[0.6]}kgx5"},
            }

            global_wendler_list = exercise_dict

            return render(request, 'wendler.html',
                          {'form': form, 'number': number, 'calculated_dict': exercise_dict})
    else:
        form = WendlerForm()

    return render(request, 'wendler.html', {'form': form})

# Function to handle page routing
def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:wendler'))
        context['segment'] = load_template
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
