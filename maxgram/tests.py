from django.test import TestCase
from .models import  Profile,Image,Comment
from .forms import EditProfileForm,UploadForm,CommentForm


class ImageTestClass(TestCase):
   def setUp(self):
       self.user = User.objects.create_user('Max')
       self.image = Image.objects.create(image ='uploads/ban-yido-536186-unsplash.jpg')
   def test_instance(self):
       self.image.save()
       self.assertTrue(isinstance(self.Image,Image))


Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profilePic('Pass'),bio('Max is awesome'),user('Max')



def test_save_method(self):
    self.james.save_editor()
    editors = Editor.objects.all()
    self.test_save_method()
    self.pass()



class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))


    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class PostTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_post= Post(title = 'Test Post',post = 'This is a random test Post',editor = self.james)
        self.new_post.save()

        self.new_post.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Post.objects.all().delete()


    def test_get_news_today(self):
        today_news = Post.todays_news()
        self.assertTrue(len(today_news)>0)


    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Post.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
#
