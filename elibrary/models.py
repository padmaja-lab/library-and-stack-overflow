from django.db import models
from django.contrib.auth.models import User

class subject(models.Model):
	subject_name = models.CharField(blank=True, null=True, max_length=100)
	pdf_link1 = models.CharField(max_length = 200)
	pdf_link2 = models.CharField(max_length = 200)
	pdf_link3 = models.CharField(max_length = 200)
	pdf_link4 = models.CharField(max_length = 200)
	pdf_link5 = models.CharField(max_length = 200)

	content1 = models.TextField()
	content2 = models.TextField()
	content3 = models.TextField()
	content4 = models.TextField()
	content5 = models.TextField()

	def __str__(self):
		return self.subject_name

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    detail = models.TextField()
    tags = models.TextField(default='')
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

class Comment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    comment = models.TextField(default='')
    add_time = models.DateTimeField(auto_now_add=True)

class UpVote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvote_user')
    

class DownVote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvote_user')
    
