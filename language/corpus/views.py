from django.shortcuts import render_to_response
from models import Word
from django.views.decorators.csrf import csrf_exempt
from .forms import TagForm
from django.http import HttpResponse
# Create your views here.
all_words_marked='No words to mark'
@csrf_exempt
def main(request):
    current_word=''
    if request.method=='POST':
        if len(request.FILES)!=0:
	    with open('text.txt', 'wb+') as destination:
                for chunk in request.FILES['myfile'].chunks():
                    destination.write(chunk)
	        destination.close()
	    f=open('text.txt',"r")
            text=f.readlines()
            word_list=list()
            for line in text:
                words=line.split()
                word_list.extend(words)
            request.session['word_list']=word_list
            index=0
            request.session['length']=len(word_list)
	    current_word=word_list[0]
	    while Word.objects.filter(name=current_word).exists():
                index+=1
		if index>=request.session['length']:
		    current_word=all_words_marked
                    break
		else:
		    current_word=text[index]
	    request.session['index']=index

    else:
	if 'word_list' in request.session:
	    text=request.session['word_list']
            index=request.session['index']
	    if index>=len(text):
                current_word=all_words_marked
	    else:
	        current_word=text[index]
    return render_to_response('main.html', {'word': current_word})

@csrf_exempt
def set_tag(request):
    text=request.session['word_list']
    index=request.session['index']
    if index>=request.session['length']:
	current_word=all_words_marked
    else:
	current_word=text[index]
        if request.method == 'POST':
            form = TagForm(request.POST) 
            if form.is_valid():
		if not Word.objects.filter(name=current_word).exists():                
		    tag=form.cleaned_data['tag']
		    case=form.cleaned_data['case']
		    verb=form.cleaned_data['verb']
		    pronoun=form.cleaned_data['pronoun']
		    person=form.cleaned_data['person']
		    number=form.cleaned_data['number']
		    poss=form.cleaned_data['poss']
		    tag=tag+" "+verb+" "+pronoun+" "+" "+person+" "+number+" "+poss+" "+case
		    tag_list=tag.split()
		    sum_tag=' '.join(tag_list)
		    print sum_tag
		    word=Word(name=current_word,tag=sum_tag)
                    word.save()
                while Word.objects.filter(name=current_word).exists():
                    index+=1
		    if index>=request.session['length']:
		        current_word=all_words_marked
                        break
		    else:
		        current_word=text[index]
	        request.session['index']=index
    return render_to_response('main.html', {'word': current_word})

@csrf_exempt
def download_file(request):
    if request.method=='POST':
	with open('words.csv', 'wb+') as csv:
            for obj in Word.objects.values():
		line=str(obj.get('id'))+";"+obj.get('name')+";"+obj.get('tag')+"\n"
                csv.write(line.encode('utf-8'))
	    csv.close()
	with open('words.csv', 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=words.csv'
        return response
    else:
	response = HttpResponse("Method not allowed.")
	return response
