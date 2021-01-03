from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


from admission.models import Admission
from admission.forms import AdmissionForm
from campus.models import Campus, Category
from taggit.models import Tag


def index(request, tag_slug=None):
    campus_lists = Campus.published.all()
    categories = Category.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        campus_lists = campus_lists.filter(tag__in=[tag])

    return render(request, 'home/index.html', {
        'tag': tag,
        'campus_lists': campus_lists,
        'categories': categories
    })


@login_required
def campus_detail(request, year, month, day, slug):
    campus = get_object_or_404(Campus, slug=slug, publish__month=month,
                               publish__year=year, publish__day=day, status='published')
    if request.method == "POST":
        print("POSTED")
        admission_form = AdmissionForm(request.POST)
        student = request.user
        # request.user.info_personnel
        # print(request.user.adresse)
        Admission.objects.create(user=student, campus=campus, student_infos=student.info_personnel,
                                 student_adresse=student.adresse, student_bac=student.baccalaureat, student_file=student.student_file)
    else:
        admission_form = AdmissionForm()
    return render(request, 'home/campus_detail.html', {
        'campus': campus,
        'admission_form': admission_form
    })


def campus_per_pays(request, slug, id):
    pays_campus = Campus.published.filter(pays_id=id)
    categories = Category.objects.all()

    return render(request, 'home/index.html', {
        'campus_lists': pays_campus,
        'categories': categories
    })
