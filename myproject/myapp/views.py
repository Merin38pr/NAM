from django.shortcuts import render
from django.http import JsonResponse

# Sample stories for different genres
STORIES = {
    "fantasy": "Once upon a time in a magical land, there was a brave little unicorn.",
    "thriller": "It was a dark and stormy night when the detective received an anonymous call.",
    "fiction": "In a small town, a young boy discovered a mysterious book that could talk.",
    "adventure": "On a sunny morning, two friends set out to find the hidden treasure.",
    "fairytale": "Long ago in a kingdom far away, there lived a kind-hearted princess."
}

def index(request):
    genrelist = ["fantasy", "thriller", "fiction", "adventure", "fairytale"]
    return render(request, 'index.html',{'genrelist': genrelist})

def story(request, genre):
    story_text = STORIES.get(genre, "Sorry, no stories available for this genre.")
    return render(request, 'story.html', {'genre': genre, 'story': story_text})

def get_story(request, genre):
    story_text = STORIES.get(genre, "Sorry, no stories available for this genre.")
    return JsonResponse({'story': story_text})
