from django.db import models
from member.models import Member

class SeqInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    taille = models.IntegerField(blank=False)
    phaseLecture = models.IntegerField(blank=True, null=True)
    espece = models.CharField(max_length=200, blank=False)
    gc_rate = models.FloatField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'



class Genome(SeqInfo):

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'


class CodantInfo(SeqInfo):
    #Blank -> If True, the field is allowed to be blank. Default is False.
    chromosome = models.ForeignKey('Genome', on_delete=models.RESTRICT)
    TYPE_CHOICES = (
      (1, 'CDS'),
      (2, 'Peptide'),
    )
    codant_type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, blank=False)
    gene = models.CharField(max_length=200, blank=True, null=True)
    start = models.IntegerField(blank=True, null=True)
    stop = models.IntegerField(blank=True, null=True)
    transcript = models.CharField(max_length=200, blank=True, null=True)
    gene_biotype = models.CharField(max_length=200, blank=True, null=True)
    transcript_biotype = models.CharField(max_length=200, blank=True, null=True)
    gene_symbol = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_plasmid = models.BooleanField(blank=True, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'

class Annotation(models.Model):
    #On suppose qu'un seul annotateur peut annoter -> d'où qu'un seul clé primaire et non double
    id = models.ForeignKey('CodantInfo', on_delete=models.RESTRICT, primary_key=True)
    gene = models.CharField(max_length=200, blank=True, null=True)
    gene_symbol = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    #On suppose qu'un seul annotateur peut annoter -> mais il nous faut toujours un foreign clé 
    annotateur = models.ForeignKey('member.Member', on_delete=models.RESTRICT)
    already_annotated = models.BooleanField(blank=True, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'


   


class SequenceBase(models.Model):
    sequence = models.TextField(blank=False)

    class Meta:
        abstract = True

class SequenceGenome(SequenceBase):
    id = models.ForeignKey('Genome', on_delete=models.RESTRICT, primary_key=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'

class SequenceCodant(SequenceBase):
    id = models.ForeignKey('CodantInfo', on_delete=models.RESTRICT, primary_key=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'