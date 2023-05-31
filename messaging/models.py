from django.db import models

# from django.db.models import Model
from django.contrib.auth.models import User


class Chat(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sender_chat"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="receiver_chat"
    )
    content = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.receiver.username


# class Room(models.Model):
# user1 = models.ForeignKey(User, on_delete=models.CASCADE)
# user2 = models.ForeignKey(User, on_delete=models.CASCADE)
# chats = models.ManyToManyField()
