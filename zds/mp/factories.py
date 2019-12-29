import factory

from zds.mp.models import PrivateTopic, PrivatePost


class PrivateTopicFactory(factory.DjangoModelFactory):
    class Meta:
        model = PrivateTopic

    title = factory.Sequence('Mon Sujet No{0}'.format)
    subtitle = factory.Sequence('Sous Titre du sujet No{0}'.format)


class PrivatePostFactory(factory.DjangoModelFactory):
    class Meta:
        model = PrivatePost

    text = 'Bonjour, je me présente, je m\'appelle l\'homme au texte bidonné'

    @factory.post_generation
    def privatetopic(self, create, extracted, **kwargs):
        ptopic = extracted or kwargs.pop('privatetopic', None)
        if ptopic:
            ptopic.last_message = self
            ptopic.save()
        return ptopic
