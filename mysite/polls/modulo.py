from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Question, Choice

class PollService:

    def get_latest_questions(self, limit=2):
        """Recupera as últimas perguntas publicadas."""
        return Question.objects.order_by("-pub_date")[:limit]

    def get_question(self, question_id):
        """Recupera uma pergunta por ID."""
        return get_object_or_404(Question, pk=question_id)

    
    def vote(self, request, question_id):
        """Processa o voto e retorna a resposta apropriada (redirecionamento ou erro)."""
        question = self.get_question(question_id)
        choice_id = request.GET.get("choice")  # Obtém a escolha via GET
        
        try:
            selected_choice = question.choice_set.get(pk=choice_id)
        except (KeyError, Choice.DoesNotExist):
            # Renderiza a página de erro diretamente se a escolha for inválida
            return render(
                request,
                "polls/detail.html",
                {
                    "question": question,
                    "error_message": "Você não selecionou uma opção válida.",
                },
            )

        # Incrementa o voto e salva a escolha
        selected_choice.votes += 1
        selected_choice.save()

        # Redireciona para a página de resultados
        return redirect(reverse('polls:results', args=(question.id,)))
