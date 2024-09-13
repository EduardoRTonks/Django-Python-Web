from django.views import generic
from .modulo import PollService

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    service = PollService()

    def get_queryset(self):
        return self.service.get_latest_questions(limit=2)

class DetailView(generic.DetailView):
    template_name = "polls/detail.html"
    service = PollService()

    def get_object(self, queryset=None):
        question_id = self.kwargs.get('pk')
        return self.service.get_question(question_id)

class ResultsView(generic.DetailView):
    template_name = "polls/results.html"
    service = PollService()

    def get_object(self, queryset=None):
        question_id = self.kwargs.get('pk')
        return self.service.get_question(question_id)

# View de votação simplificada
def vote(request, question_id):
    service = PollService()
    return service.vote(request, question_id)
