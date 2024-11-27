#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()

# Test the Author class
try:
    # Create a valid author
    valid_author = Author("Jane Austen")
    print("Valid author created:", valid_author.name)  # Expected: "Jane Austen"

    # Create an invalid author with an empty string
    invalid_author = Author("")  # Should raise a ValueError
except ValueError as e:
    print("Error creating author with empty name:", e)

try:
    # Create an invalid author with a non-string name
    invalid_author = Author(123)  # Should raise a ValueError
except ValueError as e:
    print("Error creating author with non-string name:", e)

try:
    # Try modifying the name property
    valid_author.name = "New Name"  # Should raise an AttributeError
except AttributeError as e:
    print("Error modifying author name:", e)

# Test the Magazine class
try:
    # Valid magazine
    valid_magazine = Magazine("Vogue", "Fashion")
    print("Valid magazine created:", valid_magazine.name, "-", valid_magazine.category)

    # Invalid magazine with short name
    invalid_magazine = Magazine("V", "Fashion")
except ValueError as e:
    print("Error creating magazine with short name:", e)

try:
    # Invalid magazine with empty category
    invalid_magazine = Magazine("Vogue", "")
except ValueError as e:
    print("Error creating magazine with empty category:", e)

try:
    # Test mutability of name
    valid_magazine.name = "Elle"
    print("Updated magazine name:", valid_magazine.name)

    # Test invalid name update
    valid_magazine.name = "A"
except ValueError as e:
    print("Error updating magazine name:", e)

try:
    # Test mutability of category
    valid_magazine.category = "Lifestyle"
    print("Updated magazine category:", valid_magazine.category)

    # Test invalid category update
    valid_magazine.category = ""
except ValueError as e:
    print("Error updating magazine category:", e)

# Test the Article class
print("\nTesting Article class...")
try:
    # Create valid instances
    valid_author = Author("Jane Austen")
    valid_magazine = Magazine("Vogue", "Fashion")
    valid_article = Article(valid_author, valid_magazine, "How to Wear a Tutu with Style")
    print("Valid article created:", valid_article.title)  # Expected: "How to Wear a Tutu with Style"

    # Invalid article with non-Author instance
    invalid_article = Article("Not an Author", valid_magazine, "This Should Fail")
except ValueError as e:
    print("Error creating article with non-Author instance:", e)

try:
    # Invalid article with non-Magazine instance
    invalid_article = Article(valid_author, "Not a Magazine", "This Should Fail")
except ValueError as e:
    print("Error creating article with non-Magazine instance:", e)

try:
    # Invalid article with short title
    invalid_article = Article(valid_author, valid_magazine, "1234")  # Title too short
except ValueError as e:
    print("Error creating article with short title:", e)

try:
    # Invalid article with long title
    invalid_article = Article(valid_author, valid_magazine, "This title is way too long and should definitely fail validation since it exceeds 50 characters.")
except ValueError as e:
    print("Error creating article with long title:", e)

    print("\nTesting Article properties...")

try:
    # Test author property
    print("Initial author:", valid_article.author.name)  # Expected: "Jane Austen"
    new_author = Author("Charles Dickens")
    valid_article.author = new_author
    print("Updated author:", valid_article.author.name)  # Expected: "Charles Dickens"

    # Test invalid author update
    valid_article.author = "Not an Author"  # Should raise ValueError
except ValueError as e:
    print("Error updating author:", e)

try:
    # Test magazine property
    print("Initial magazine:", valid_article.magazine.name)  # Expected: "Vogue"
    new_magazine = Magazine("Elle", "Fashion")
    valid_article.magazine = new_magazine
    print("Updated magazine:", valid_article.magazine.name)  # Expected: "Elle"

    # Test invalid magazine update
    valid_article.magazine = "Not a Magazine"  # Should raise ValueError
except ValueError as e:
    print("Error updating magazine:", e)

