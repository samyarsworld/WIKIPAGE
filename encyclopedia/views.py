from django.shortcuts import render, redirect
from markdown import Markdown
from random import randrange

from . import util

def md_to_html(entry):
    content = util.get_entry(entry)
    # convert mardown to HTML
    markdowner = Markdown()

    if content == None:
        return None
    return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request, entry):
    html_content = md_to_html(entry)

    if html_content == None:
        return render(request, 'encyclopedia/error.html')

    return render(request, 'encyclopedia/entry.html', {
        'entry': entry,
        'content': html_content
    })

def search(request):
    title = request.POST['q']
    html_content = md_to_html(title)
    if html_content is not None:
        return render(request, 'encyclopedia/entry.html', {
            'entry': title,
            'content': html_content
        })
    else:
        query_set = []
        all_entries = util.list_entries()
        for entry in all_entries:
            if title.lower() in entry.lower():
                query_set.append(entry)

        return render(request, 'encyclopedia/search.html', {
            'query_set': query_set
        })




def newPage(request):
    if request.method == 'POST':
        content = request.POST['description']
        title = request.POST['title']
        
        if title in util.list_entries():
            message = 'The title you entered already exists. Please try using another title.'
            return render(request, 'encyclopedia/newPage.html', {
                'title': title,
                'message': message,
                'content': content
            })

        else:
            util.save_entry(title, content)
            return redirect('wiki/' + title)

    title = ''
    content = ''
    message = ''
    return render(request, 'encyclopedia/newPage.html', {
        'title': title,
        'message': message,
        'content': content
    })


def editPage(request):
    if request.method == 'POST':
        title = request.POST['entry']
        entry = util.get_entry(title)
        return render(request, 'encyclopedia/editPage.html', {
            'title': title,
            'content': entry
        })

def savePage(request):
     if request.method == 'POST':
        content = request.POST['description']
        title = request.POST['title']

        util.save_entry(title, content)
        return redirect('wiki/' + title)


def randomPage(request):
    all_entries = util.list_entries()
    rand_idx = randrange(len(all_entries))
    entry = all_entries[rand_idx]
    return redirect('wiki/' + entry)