from django.db import models

# Create your models here.

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 这个属性可以将多条条目使用Entries来表示，默认使用Entrys表示
        verbose_name_plural = 'entries' 

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."