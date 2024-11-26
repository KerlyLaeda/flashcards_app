from django.db import models

NUM_BOXES = 5  # number of boxes for spaced repetition
BOXES = range(1, NUM_BOXES + 1)  # user-friendly repr of boxes (1-5)


class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)  # to show newest first

    def __str__(self):
        return self.question
