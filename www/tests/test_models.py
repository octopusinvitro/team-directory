from django.test import TestCase
from www.models import Person


class PersonTest(TestCase):
    def test_persons_have_a_name(self):
        Person.objects.create(
            name='name1', email='email1', title='title1', image='image1')
        person1 = Person.objects.get(name='name1')
        self.assertEqual(str(person1), 'name1')
