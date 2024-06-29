from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='sender'
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='receiver'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['sender', 'receiver'], ['receiver', 'sender']

    def __str__(self):
        return f'Message {self.receiver}'


class Message(models.Model):
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE,
        related_name='messages'
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='sender_messages'
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.sender} sent a message to {self.chat.receiver}.'

    def get_receiver(self):
        return self.chat.receiver

    def get_receiver_username(self):
        return self.chat.receiver.username
