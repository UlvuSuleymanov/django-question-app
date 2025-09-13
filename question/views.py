
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question, Variant

def add_question_page(request):
    return render(request, "question/add-question.html")


@login_required
def user_add_question(request):
    if request.method == "POST":
        question_text = request.POST.get("question_text")
        correct_letter = request.POST.get("correct_answer")

        if not question_text or not correct_letter:
            messages.error(request, "Please fill all fields and select the correct answer.")
            return redirect('add')

        # Create Question
        question = Question.objects.create(
            title=question_text,
            content=question_text,  # or separate content if needed
            created_by=request.user
        )

        # Create Variants
        for letter in 'ABCDE':
            text = request.POST.get(f"variant_{letter}")
            if not text:
                messages.error(request, f"Variant {letter} cannot be empty.")
                question.delete()
                return redirect('index')

            Variant.objects.create(
                question=question,
                option=letter,
                text=text,
                is_correct=(letter == correct_letter)
            )

        messages.success(request, "Question added successfully!")
        return redirect('index')

    return render(request, 'add_question.html')