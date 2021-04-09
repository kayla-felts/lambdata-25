'''Basic unit test for lambdata package'''

from random import randint
import pytest
import lambdata as ld

#Testing init in lambdata
def test_increment_int():
    '''Making sure increment works for positive numbers'''
    x0 = 0
    y0 = ld.increment(x0) # 1
    assert y0 == 1

    x1 = 100
    y1 = ld.increment(x1) # 101
    assert y1 == 101

def test_increment_float():
    '''Making sure increment works for floats'''
    x0 =10.5
    y0 = ld.increment(x0) # 11.5
    assert y0 == 11.5

def test_increment_neg():
    '''Making sure increment works for negative numbers'''
    x0 = -1
    y0 = ld.increment(x0) # 0
    assert y0 == 0

def test_increment_neg_float():
    '''Making sure increment works for negative floats'''
    x0 = -1.5
    y0 = ld.increment(x0) # -0.5
    assert y0 == -0.5

def test_colors():
    '''Testing that COLORS contains correct items'''
    assert 'Cyan' in ld.COLORS
    assert 'Mauve' in ld.COLORS
    assert 'Blue' in ld.COLORS
    assert 'Brown' not in ld.COLORS
    assert 'Yellow' not in ld.COLORS

def test_num_colors():
    '''Testing the number of elements in colors'''
    assert len(ld.COLORS) == 4

#testing oop examples
user1 = ld.oop_examples.SocialMediaUser('Kayla', 'Indiana')
user2 = ld.oop_examples.SocialMediaUser('Jacob', 'Brazil', 350)

def test_smu_constructor():
    '''testing that constructor works properly'''
    #Testing name
    assert user1.name.lower() == 'kayla'
    assert user2.name.lower() == 'jacob'

    #testing location
    assert user1.location.lower() == 'indiana'
    assert user2.location.lower() == 'brazil'

    #testing upvotes
    assert user1.upvotes == 0 #checks default
    assert user2.upvotes == 350

def test_unpopular():
    '''testing to make sure 0 upvotes is unpopular'''
    assert isinstance(user1.is_popular(), bool)
    assert not user1.is_popular()

def test_popular():
    '''testing to make sure 350 votes is popular'''
    assert isinstance(user2.is_popular(), bool)
    assert user2.is_popular()

def test_constructor_types():
    '''testing constructor types'''
    assert isinstance(user1.name, str)
    assert isinstance(user1.location, str)
    assert isinstance(user1.upvotes, int)



